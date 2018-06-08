import helpers
import argparse
import ntpath
import numpy as np
import cv2
import os

if __name__ == '__main__':
    # run like this: python--input_folder path_to_images --output_folder path_to_img_output --number_of_splits 5 --labels Black_Hair Blond_Hair Brown_Hair Male Young
    parser = argparse.ArgumentParser()

    parser.add_argument('--input_folder', type=str)
    parser.add_argument('--output_folder', type=str)
    parser.add_argument('--number_of_splits', type=int)
    parser.add_argument('--labels', '--list', nargs='+', default=None)

    config = parser.parse_args()


    image_path = os.path.join('images', 'image.jpg')
    output_path = os.path.join('images_output')
    labels = config.labels
    num_splits = config.number_of_splits


    # helpers.replicate_folder_structure(config.input_folder, config.output_folder)
    helpers.split_image(image_path, output_path, num_splits, labels)

