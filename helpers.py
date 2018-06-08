import argparse
import ntpath
import numpy as np
import cv2
import os


def split_image(image_path, output_path, num_splits, labels=None):
    img = cv2.imread(image_path)
    head, tail = os.path.split(image_path)

    (height, width, depth) = img.shape
    width_split = int(width / num_splits)
    print(img.shape, img.dtype)

    for i in range(num_splits):
        img_split = img[:, i * width_split: (i + 1) * width_split, :]
        if not labels:
            filename = str(tail.split('.')[0]) + str(i) + '.jpg'
        else:
            filename = str(tail.split('.')[0]) + '_' + labels[i] + '.jpg'

        cv2.imwrite(os.path.join(output_path, filename), img_split)


def replicate_folder_structure(input_folder, output_folder):
    if not os.path.isdir(output_folder):
        os.mkdir(output_folder)

    for dirpath, dirnames, filenames in os.walk(input_folder):
        for dir in dirnames:
            path = os.path.join(output_folder, dir)
            if not os.path.isdir(path):
                os.mkdir(path)
            else:
                print("Folder already exists, skipping...")

