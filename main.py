from api_functions import create_zip_from_dataset
from api_functions import add_api_results
from dataset_functions import reduce_dataset
from dataset_functions import replicate_folder_structure
from stargan_functions import split_image
import os

if __name__ == '__main__':
    # replace your paths
    # comment or uncomment whatever you want to run

    input_folder = os.path.join('E:\\', 'vggface2_train', 'train') # make sure to point to 'train'

    """ Create the reduced dataset """
    output_folder = os.path.join('E:\\', 'vggface2_train_20')

    reduce_dataset(input_folder, output_folder, 20)
    """"""""""""""""""""""""""""""""""""

    """ Create the zip for the API"""
    # output_folder = os.path.join('E:\\', 'bundle')
    #
    # create_zip_from_dataset(input_folder, output_folder, 1) # last param is the number of images per person
    """"""""""""""""""""""""""""""""""""

    """ Once you have the API result, use this to merge the result with our datasset(the reduced one) """
    # path_to_zip = os.path.join('C:', 'Users', 'Kabur', 'Desktop', 'ProjectAI', 'batch_processed_testing.zip')
    # path_to_zip = "C:\\Users\\Kabur\\Desktop\\ProjectAI\\batch_processed_testing.zip"




    # path_to_zip = os.path.join('C:\\', 'Users', 'Kabur', 'Desktop', 'ProjectAI', 'batch_processed_testing.zip')
    #
    # path_to_dataset = os.path.join('E:\\', 'vggface2_train_testing', 'train')
    # num_images = 1  # how many images per person were used in the query
    # num_augments = 3  # how many augments per image
    #
    # add_api_results(path_to_zip, path_to_dataset, num_images, num_augments)
    """"""""""""""""""""""""""""""""""""
