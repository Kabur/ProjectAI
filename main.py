import pickle
import io
import zipfile
import urllib.request

from api_functions import *
from dataset_functions import *
from stargan_functions import *
import os
import time

if __name__ == '__main__':
    # replace your paths
    # comment or uncomment whatever you want to run


    """ Create the reduced dataset """
    # input_folder = os.path.join('E:\\', 'vggface2_train', 'train')  # make sure to point to 'train'
    # output_folder = os.path.join('E:\\', 'vggface2_train_20')
    #
    # reduce_dataset(input_folder, output_folder, 20)
    """"""""""""""""""""""""""""""""""""

    """ Create the zip for the API"""
    # input_folder = os.path.join('E:\\', 'vggface2_train', 'train')  # make sure to point to 'train'
    # output_folder = os.path.join('E:\\', 'projectAI_bundles_3_8')
    #
    # create_zip_from_dataset(input_folder, output_folder, num_images=3, bundle_size=8)  # last param is the number of images per person
    """"""""""""""""""""""""""""""""""""

    """ query the API for each bundle and pickle the dictionary of responses for each bundle """
    # input_folder = os.path.join('E:\\', 'projectAI_bundles_3_8')
    input_folder = os.path.join("C:\\", "Users", "Kabur", "Desktop", "ProjectAI", "projectAI_bundles_3_8")

    bundles = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]
    responses = []
    bundle_dict = {}

    for bundle in bundles:
        start_time = time.time()
        print("Querying bundle: " + bundle)
        bundle_path = os.path.join(input_folder, bundle)
        response = query_api(yaw=[-15, 15, 15], pitch=0, roll=0, bundle_path=bundle_path, email='tomasfabry1@gmail.com')
        bundle_dict[bundle] = response
        print(str(response) + "|" + response.text + ' | Time: ' + str(time.time() - start_time))

        responses.append(response)
        # time.sleep(10)

    pickle.dump(bundle_dict, open('pickled_bundle_dict.pkl', 'wb'))
    pickle.dump(responses, open('pickled_responses.pkl', 'wb'))
    """"""""""""""""""""""""""""""""""""


    """ Once you have the API result, use this to merge the result with our datasset(the reduced one) """
    # path_to_zip = os.path.join('C:\\', 'Users', 'Kabur', 'Desktop', 'ProjectAI', 'batch_processed_testing.zip')
    # path_to_dataset = os.path.join('E:\\', 'vggface2_train_testing', 'train')
    # num_images = 1  # how many images per person were used in the query
    # num_augments = 3  # how many augments per image
    #
    # add_api_results(path_to_zip, path_to_dataset, num_images, num_augments)
    """"""""""""""""""""""""""""""""""""
