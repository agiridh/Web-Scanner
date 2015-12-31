import os

# create a directory if it does not exist already
def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# writing data to a file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()
