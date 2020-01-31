import os

import numpy as np
from PIL import Image


def to_numpy(dirname: str):
    labels = []
    for _, _, files in os.walk(dirname):
        if files:
            labels.append(int(files[0][:4]))
    nlabel = len(labels)
    images = np.empty((nlabel, 20, 105, 105), dtype=np.bool)
    labels = np.empty((nlabel, 20), dtype=np.int)
    label_idx = 0
    for root, _, files in os.walk(dirname):
        for index, name in enumerate(files):
            # XXXX_YY.png
            label = int(name[:4]) - 1
            path = os.path.join(root, name)
            image = np.asarray(Image.open(path, 'r'))
            images[label_idx, index] = image
            labels[label_idx, index] = label
        if files:
            label_idx += 1
    np.savez_compressed(dirname + '.npz', images=images, labels=labels)


if __name__ == "__main__":
    to_numpy('images_background')
    to_numpy('images_validation')
    to_numpy('images_evaluation')
