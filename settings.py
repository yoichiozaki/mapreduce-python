default_input_dir = "input_files"

default_map_dir = "temp_map_files"

default_output_dir = "output_files"

default_n_mappers = 4
default_n_reducers = 4

def get_input_file(input_dir = None, extension = ".ext"):
    if not (input_dir is None):
        return input_dir + "/file" + extension
    return default_input_dir + "/file" + extension

def get_input_split_file(index, input_dir = None, extension = ".ext"):
    if not(input_dir is None):
        return input_dir+"/file_"+ str(index) + extension
    return default_input_dir + "/file_" + str(index) + extension

def get_temp_map_file(index, reducer, output_dir = None, extension = ".ext"):
    if not(output_dir is None):
        return output_dir + "/map_file_" + str(index)+"-" + str(reducer) + extension
    return default_output_dir + "/map_file_" + str(index) + "-" + str(reducer) + extension

def get_output_file(index, output_dir = None, extension = ".out"):
    if not(output_dir is None):
        return output_dir+"/reduce_file_"+ str(index) + extension
    return default_output_dir + "/reduce_file_" + str(index) + extension

def get_output_join_file(output_dir = None, extension = ".out"):
    if not(output_dir is None):
        return output_dir +"/output" + extension
    return default_output_dir + "/output" + extension