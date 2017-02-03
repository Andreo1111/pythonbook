import tarfile


object = raw_input('Please input tar file name :')
file_list = tarfile.open(object)
file_list.extractall(path="/")
file_list.close()

