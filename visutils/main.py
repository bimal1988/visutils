import multiprocessing
from stream import StreamCreator, AsyncMode
import cv2
from common import Timer
import numpy as np

if __name__ == '__main__':
    print("Hello world ", multiprocessing.cpu_count())
    st = StreamCreator.create_stream(async_mode=AsyncMode.MULTI_THREADING)
    st.start()
    timer = Timer()
    timer.start()
    i = 0
    last_frame = None
    while True:
        frame = st.read()
        i += 1
        if frame is not None:
            if not np.array_equal(last_frame, frame):
                timer.tick()
            cv2.imshow('Webcam', frame)
            last_frame = np.copy(frame)
        if cv2.waitKey(20) == ord('q'):
            st.stop()
            timer.stop()
            print(timer.ticks_per_second())
            break
        # import time
        # time.sleep(5)
        # print(i)
        # if i == 8000:
        #     st.stop()

