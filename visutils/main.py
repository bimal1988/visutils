import multiprocessing
from visutils.stream import StreamCreator
import cv2
from visutils.common import Timer

if __name__ == '__main__':
    print("Hello world ", multiprocessing.cpu_count())
    # st = StreamCreator.create_stream('/Users/beherabimalananda/miniconda3/pkgs/torchvision-0.6.0-py38_cpu/info/test/test/assets/videos/v_SoccerJuggling_g24_c01.avi')
    # st = StreamCreator.create_stream('/Users/beherabimalananda/Desktop/FaceMaskDetection_480p.mov')
    st = StreamCreator.create_stream('rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov')
    # st = StreamCreator.create_stream()
    st.start()
    timer = Timer()
    timer.start()
    i = 0
    last_frame = None
    while True:
        frame = st.read()
        if frame is None:
            print('broke')
            break
        i += 1
        timer.tick()
        cv2.imshow('Webcam', frame)
        # last_frame = np.copy(frame)
        if cv2.waitKey(2000) == ord('q'):
            st.stop()
            timer.stop()
            print(timer.ticks_per_second())
            break
        # import time
        # time.sleep(5)
        # print(i)
        # if i == 8000:
        #     st.stop()

