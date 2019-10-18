import os

import numpy as np
from PIL import Image


def to_numpy(dirname: str):
    labels = []
    for _, _, files in os.walk(dirname):
        if files:
            labels.append(int(files[0][:4]))
    minlabel = min(labels)
    nlabel = len(labels)
    images = np.empty((nlabel, 20, 105, 105), dtype=np.bool)
    labels = np.empty((nlabel, 20), dtype=np.int)
    for root, _, files in os.walk(dirname):
        for name in files:
            # name format: XXXX_YY.png
            # XXXX: character index (1 ~ 1623)
            # YY: sample index (1 ~ 20)
            label = int(name[:4]) - minlabel    # XXXX - 1
            index = int(name[5:7]) - 1          # YY - 1
            path = os.path.join(root, name)
            image = np.asarray(Image.open(path, 'r'))
            images[label, index] = image
            labels[label, index] = label
    np.savez_compressed(dirname + '.npz', images=images, labels=labels)


if __name__ == "__main__":
    to_numpy('images_background')
    to_numpy('images_evaluation')
