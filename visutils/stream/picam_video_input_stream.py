from visutils.stream import VideoInputStream
from picamera.array import PiRGBArray
from picamera import PiCamera
from threading import Thread


class PicamVideoInputStream(VideoInputStream):
    def __init__(self, src: int, resolution=(320, 240), framerate=32, **kwargs):
        # initialize the camera
        self._camera = PiCamera(src)

        # set camera parameters
        self._camera.resolution = resolution
        self._camera.framerate = framerate

        # set optional camera parameters (refer to PiCamera docs)
        for (arg, value) in kwargs.items():
            setattr(self._camera, arg, value)

        # initialize the stream
        self._rawCapture = PiRGBArray(self._camera, size=resolution)
        self._stream = self._camera.capture_continuous(self._rawCapture,
                                                       format="bgr", use_video_port=True)

        # initialize the frame and the variable used to indicate
        # if the thread should be stopped
        self._frame = None
        self._stopped = False

    def start(self):
        # start the thread to read frames from the video stream
        t = Thread(target=self._update, args=())
        t.daemon = True
        t.start()
        return self

    def _update(self):
        # keep looping infinitely until the thread is stopped
        for f in self._stream:
            # grab the frame from the stream and clear the stream in
            # preparation for the next frame
            self._frame = f.array
            self._rawCapture.truncate(0)

            # if the thread indicator variable is set, stop the thread
            # and resource camera resources
            if self._stopped:
                self._stream.close()
                self._rawCapture.close()
                self._camera.close()
                return

    def read(self):
        # return the frame most recently read
        return self._frame

    def stop(self):
        # indicate that the thread should be stopped
        self._stopped = True
