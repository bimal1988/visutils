from queue import Empty, Queue
from threading import Thread

from picamera import PiCamera
from picamera.array import PiRGBArray

from visutils.video import VideoInputStream


class PicamVideoInputStream(VideoInputStream):
    def __init__(self, src: int, is_live=False, buffer_size=128,
                 resolution=(320, 240), framerate=32, **kwargs):
        # initialize the camera
        self._camera = PiCamera(src)

        # set camera parameters
        self._camera.resolution = resolution
        self._camera.framerate = framerate

        # set optional camera parameters (refer to PiCamera docs)
        for (arg, value) in kwargs.items():
            setattr(self._camera, arg, value)

        # initialize the video
        self._rawCapture = PiRGBArray(self._camera, size=resolution)
        self._stream = self._camera.capture_continuous(self._rawCapture,
                                                       format="bgr",
                                                       use_video_port=True)
        self._is_live = is_live
        self._buffer = Queue(maxsize=buffer_size)
        self._thread = Thread(target=self._update, args=())
        self._thread.daemon = True

        self._frame = None
        self._stopped = False

    def start(self):
        self._thread.start()

    def _update(self):
        while not self._stopped:
            stream = next(self._stream)
            frame = stream.array

            if self._is_live:
                self._clear_buffer()

            self._buffer.put(frame)

            # grab the frame from the video and clear the video in
            # preparation for the next frame
            self._rawCapture.seek(0)
            self._rawCapture.truncate()

        self._stream.close()
        self._rawCapture.close()
        self._camera.close()

    def read(self):
        return self._buffer.get()

    def _shutdown(self):
        self._stopped = True
        self._clear_buffer()
        self._buffer.put(None)

    def _clear_buffer(self):
        while not self._buffer.empty():
            try:
                self._buffer.get_nowait()
            except Empty:
                pass

    def stop(self):
        self._shutdown()
        self._thread.join()
