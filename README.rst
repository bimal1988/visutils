Visutils
========
Computer vision utility library to perform common vision operations for deep learning faster and better.

Getting Started
===============

.. code-block:: python

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

Installation
============
You can install it with pip::

    pip install visutils

Authors
=======

Bimalananda Behera

Licence
=======
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

Acknowledgments
===============
Inspiration
1. https://github.com/jrosebr1/imutils
2. https://github.com/abhiTronix/vidgear

