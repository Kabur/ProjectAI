import argparse
from zipfile import ZipFile
import shutil
import ntpath
import requests
import json
import math
import numpy as np
import cv2
import os


def create_zip_from_dataset(input_folder, output_folder, num_images=3, bundle_size=16):
    if num_images * bundle_size > 50:
        print("You're using more than 50 images per bundle, API will probably reject this")
        return
    if not os.path.isdir(output_folder):
        os.mkdir(output_folder)

    # get all folders in input_folder
    print("Reading folders...")
    folders = [f for f in os.listdir(input_folder) if os.path.isdir(os.path.join(input_folder, f))]

    # iterate through bundles, assign name and folder
    for bundle_index in range(int(math.ceil(len(folders) / bundle_size))):

        bundle_name = 'bundle' + '_' + str(bundle_index)
        image_dump_folder = os.path.join(output_folder, bundle_name)
        os.mkdir(image_dump_folder)

        # for each folder belonging to this bundle
        for folder in folders[bundle_index * bundle_size:bundle_index * bundle_size + bundle_size]:
            print(folder)
            # get all files in each folder, take only a specified number of them
            folder_path = os.path.join(input_folder, folder)
            files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
            selected_files = files[:num_images]

            # copy each file to the image_dump_folder and rename it to the form foldername_i.jpg
            for i, file in enumerate(selected_files):
                shutil.copy2(os.path.join(input_folder, folder, file), image_dump_folder)
                new_file_name = folder + '_' + str(i) + '.jpg'
                os.rename(os.path.join(image_dump_folder, file), os.path.join(image_dump_folder, new_file_name))

        # make archive from the images
        shutil.make_archive(os.path.join(output_folder, bundle_name), "zip", image_dump_folder)

        # delete the images, keep the zip only, then go to the next bundle
        shutil.rmtree(image_dump_folder)


def add_api_results(path_to_zip, path_to_dataset, num_images, num_augments):
    print("this function is not done yet")
    # todo: just finish this function xD
    # responses = pickle.load(open('pickled_responses.pkl', 'rb'))
    # file_found = []
    #
    # for r in responses:
    #     print("*" * 50)
    #     r_json = json.loads(r.text)
    #     process_id = r_json['processId']
    #     print('text: ', r.text)
    #     print('r: ', r)
    #     print('processId: ', process_id)
    #
    #     # build the download link using processId
    #     url = "http://yourface.3duniversum.com/uploaded/" + process_id + "/batch_processed.zip"
    #     res = requests.get(url)
    #     if not res.ok:
    #         print("File not found!")
    #         file_found.append(False)
    #         continue
    #     else:
    #         file_found.append(True)
    #
    #     zip_file = zipfile.ZipFile(io.BytesIO(res.content))
    #
    #     folder = "batch_processed_testing_" + process_id
    #     if not os.path.isdir(folder):
    #         os.mkdir(folder)
    #
    #     zip_file.extractall(folder)
    #     zip_file.close()
    pass


def query_api(yaw, pitch, roll, bundle_path, email):
    url = 'http://yourface.3duniversum.com/api/faceGen/upload'
    file = open(bundle_path, 'rb')  # flat structure zip file

    files = {'images': (bundle_path, file)}
    payload = {
        "glasses": {
            "models": ["HazzBerry"],  # available glasses model
            "materials": [
                {
                    "name": "Obsidian Black",  # tag name
                    "frame": {"color": "rgb(0,0,0)"},  # frame color
                    "glass": {"color": "rgb(255, 255, 255)", "opacity": 0.3}  # glass may have shader issue
                }
            ]
        },
        "poses": [
            {
                "yaw": yaw,  # it can be range (min, max, interval)
                "pitch": pitch,
                "roll": roll  # or just a single value
            }
        ]
    }

    data = {
        "variants": json.dumps(payload),
        "email": email,
    }

    r = requests.post(url, files=files, data=data)
    file.close()

    # r_json = json.loads(r.text)
    # print(r)
    # print(type(r_json))
    # print(r_json['processId'])
    return r


def query_api_testing():
    import requests
    import json
    import os

    url = 'http://yourface.3duniversum.com/api/faceGen/upload'
    file = open('bundle_0.zip', 'rb')  # flat structure zip file

    files = {'images': ('bundle_0.zip', file)}
    payload = {
        "glasses": {
            #         "models": ["HazzBerry", "GerretLight", "Enzo", "M14", "M10"],                # available glasses model
            "models": ["HazzBerry"],  # available glasses model
            "materials": [
                {
                    "name": "Obsidian Black",  # tag name
                    "frame": {"color": "rgb(0,0,0)"},  # frame color
                    "glass": {"color": "rgb(255, 255, 255)", "opacity": 0.3}  # glass may have shader issue
                }
                #             {
                #                 "name": "Glamour Red",
                #                 "frame": { "color": "rgb(168, 32, 26)" },
                #                 "glass": { "color": "rgb(255, 255, 255)", "opacity": 0.3 }
                #             },
                #             {
                #                 "name": "Gold Potato",
                #                 "frame": { "color": "rgb(255, 242, 0)" },
                #                 "glass": { "color": "rgb(255, 255, 255)", "opacity": 0.3 }
                #             },
                #             {
                #                 "name": "Tornado Blue",
                #                 "frame": { "color": "rgb(66, 134, 244)" },
                #                 "glass": { "color": "rgb(255, 255, 255)", "opacity": 0.3 }
                #             },
                #             {
                #                 "name": "Lush Green",
                #                 "frame": { "color": "rgb(59, 173, 46)" },
                #                 "glass": { "color": "rgb(255, 255, 255)", "opacity": 0.3 }
                #             }
            ]
        },
        "poses": [
            {
                "yaw": [-30, 30, 30],  # it can be range (min, max, interval)
                #             "pitch": [-15, 15, 15],
                #             "yaw": 0,                     # it can be range (min, max, interval)
                "pitch": 0,
                #             "yaw": 0,
                #             "pitch": 0,
                "roll": 0  # or just a single value
            }
        ]
    }

    data = {
        "variants": json.dumps(payload),
        "email": "tomasfabry1@gmail.com",
    }

    r = requests.post(url, files=files, data=data)
    file.close()

    print(r)
