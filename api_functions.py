import argparse
import zipfile
import time
import shutil
import ntpath
import numpy as np
import cv2
import os


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
            os.rename(os.path.join(output_folder, 'bundle_files', file),
                      os.path.join(output_folder, 'bundle_files', new_file_name))

    # make archive from bundle_files
    shutil.make_archive(os.path.join(output_folder, 'bundle'), "zip", os.path.join(output_folder, 'bundle_files'))

    # delete the images, keep the zip only
    shutil.rmtree(os.path.join(output_folder, 'bundle_files'))


def add_api_results(path_to_zip, path_to_dataset, num_images, num_augments):
    # work in progress - waiting to see how the file structure of the output looks like
    pass
    # zip_file = zipfile.ZipFile(path_to_zip)
    #
    # zip_file.extractall('E:\\zip_junk')  # todo: replace this path with something reasonable


