from pathlib import Path
import numpy as np
import cv2

TAG_FLOAT = 202021.25


def read_optical_flow(path: str):
    path = Path(path)
    assert (path.exists())

    with path.open() as f:
        tag = float(np.fromfile(f, np.float32, count=1)[0])
        assert (tag == TAG_FLOAT)

        w = np.fromfile(f, np.int32, count=1)[0]
        h = np.fromfile(f, np.int32, count=1)[0]

        flow = np.fromfile(f, np.float32, count=h * w * 2)
        flow.resize((h, w, 2))

    return flow


def write_optical_flow(flow: np.ndarray, path: str):
    path = Path(path)
    if not path.parent.exists():
        path.parent.mkdir(parents=True)

    with path.open('wb') as f:
        np.array(TAG_FLOAT, dtype=np.float32).tofile(f)
        height, width = flow.shape[:2]
        np.array(width, dtype=np.uint32).tofile(f)
        np.array(height, dtype=np.uint32).tofile(f)
        flow.astype(np.float32).tofile(f)


def flow_to_image(flow: np.ndarray):
    h, w, _ = flow.shape
    hsv = np.zeros((h, w, 3), dtype=np.uint8)
    hsv[..., 1] = 255
    mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    hsv[..., 0] = ang * 180 / np.pi / 2
    hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
    rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return rgb


if __name__ == '__main__':
    opt_flow = read_optical_flow('/Users/beherabimalananda/Desktop/flaredata/demo_dataset/flow/vid_26_img_9.flo')
    img = flow_to_image(opt_flow)
    cv2.imshow('flow', img)
    cv2.waitKey(0)
    flow2 = cv2.resize(opt_flow, (4600, 2400))
    # flow2 = resize(flow, (720, 480))
    img = flow_to_image(flow2)
    cv2.imshow('flow', img)
    cv2.waitKey(0)
