# Visutils

Computer vision utility library to perform common vision operations for deep learning faster and better.
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
from visutils.video import StreamCreator
import cv2

st = StreamCreator.create_video_input_stream()
st.start()

while True:
    frame = st.read()
    if frame is None:
        break
    cv2.imshow('Webcam', frame)
    if cv2.waitKey(33) == ord('q'):
        st.stop()
```

### Installing

```
pip install visutils
```

## Authors

* **Bimalananda Behera**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Inspiration
1. https://github.com/jrosebr1/imutils
2. https://github.com/abhiTronix/vidgear

