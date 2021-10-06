import os
def makedirectory(directory):
    try:
        os.mkdir(directory)
    except Exception as e:
        print(e)
        print('error while creating diectory. Is directory already created? Continuing with the existing directory.')