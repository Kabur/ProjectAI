import argparse
import time
import shutil
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


def reduce_dataset(input_folder, output_folder, num_images):
    # folders = os.listdir(input_folder)

    folders = [f for f in os.listdir(input_folder) if os.path.isdir(os.path.join(input_folder, f))]

    for folder in folders:
        print(folder)
        folder_path = os.path.join(input_folder, folder)
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

        selected_files = files[:num_images]

        for file in selected_files:
            shutil.copy2(os.path.join(input_folder, folder, file), os.path.join(output_folder, folder))


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


def create_zip_from_dataset(input_folder, output_folder, num_images):
    if not os.path.isdir(output_folder):
        os.mkdir(output_folder)
    if not os.path.isdir(os.path.join(output_folder, 'bundle_files')):
        os.mkdir(os.path.join(output_folder, 'bundle_files'))

    # get all folders in root
    folders = [f for f in os.listdir(input_folder) if os.path.isdir(os.path.join(input_folder, f))]

    for folder in folders:
        print(folder)
        folder_path = os.path.join(input_folder, folder)
        # get all files in each folder, take only a specified number of them
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        selected_files = files[:num_images]

        # copy each file to the output folder and rename it to the form foldername_i.jpg
        for i, file in enumerate(selected_files):
            shutil.copy2(os.path.join(input_folder, folder, file), os.path.join(output_folder, 'bundle_files'))
            new_file_name = folder + '_' + str(i) + '.jpg'
            os.rename(os.path.join(output_folder, 'bundle_files', file), os.path.join(output_folder, 'bundle_files', new_file_name))

    # make archive from bundle_files
    shutil.make_archive(os.path.join(output_folder, 'bundle'), "zip", os.path.join(output_folder, 'bundle_files'))




if __name__ == '__main__':
    # replace your paths
    # comment or uncomment whatever you want to run

    input_folder = os.path.join('E:', 'vggface2_train_testing', 'train')

    """ Create the reduced dataset """
    # output_folder = os.path.join('E:', 'vggface2_train_less', 'train')

    # replicate_folder_structure(input_folder, output_folder)
    # reduce_dataset(input_folder, output_folder, 3)
    """"""""""""""""""""""""""""""""""""

    """ Create the zip for the API"""
    output_folder = os.path.join('E:', 'bundle')

    # last param is the number of images per person
    create_zip_from_dataset(input_folder, output_folder, 1)
    """"""""""""""""""""""""""""""""""""

    



