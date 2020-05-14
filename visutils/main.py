import multiprocessing
from visutils.stream import StreamCreator
import cv2
from visutils.common import Timer

if __name__ == '__main__':
    print("Hello world ", multiprocessing.cpu_count())
    # st = StreamCreator.create_video_input_stream('/Users/beherabimalananda/miniconda3/pkgs/torchvision-0.6.0-py38_cpu/info/test/test/assets/videos/v_SoccerJuggling_g24_c01.avi')
    # st = StreamCreator.create_video_input_stream('/Users/beherabimalananda/Desktop/FaceMaskDetection_480p.mov')
    # st = StreamCreator.create_video_input_stream('rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov')
    # st = StreamCreator.create_video_input_stream('https://www.youtube.com/watch?v=FeJKJ5MoCHY')
    # st = StreamCreator.create_video_input_stream()
    st = StreamCreator.create_video_input_stream('lalu')
    st.start()
    # st = cv2.VideoCapture('videotestsrc ! video/x-raw,framerate=20/1 ! videoscale ! videoconvert ! appsink', cv2.CAP_GSTREAMER)

    timer = Timer()
    timer.start()
    i = 0
    last_frame = None
    while True:
        frame = st.read()
        # print(frame)
        if frame is None:
            break
        i += 1
        timer.tick()
        cv2.imshow('Webcam', frame)
        # last_frame = np.copy(frame)
        if cv2.waitKey(33) == ord('q'):
            st.stop()
            timer.stop()
            print(timer.ticks_per_second())
            break
        # import time
        # time.sleep(5)
        # print(i)
        # if i == 8000:
        #     st.stop()

