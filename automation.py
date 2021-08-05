#%%
import sys
import os

## Need to get the dataset name
## file path
## tensorboard run directory
## Number of max epochs (test with 1 to make sure it works before doing anything larger)
## file_name() is unnecessary, just name the files train.laz and validation.laz respectively

def file_location():
    user_location = input("Enter the location of the training data (directory/folder, not file): \n")
    assert os.path.exists(user_location), "I did not find the location at, " + str(user_location)
    return str(user_location)

def file_name(): #this might be unnecessary
    user_name = input("Enter the name of the training data file (file only, not directory): \n")
    assert os.path.exists(user_name), "I did not find the file named " + str(user_name)
    return str(user_name)

def tensorboard_directory():
    tens_dirc = input("Enter the name of the tensorboard directory/folder: \n")
    assert os.path.exists(tens_dirc), "I did not find the directory named" + str(tens_dirc)
    return str(tens_dirc)

def epochs_num():
    num = int(input("Enter the maximum number of epochs you want to run: \n"))
    return num

