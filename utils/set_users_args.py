import datetime

from data_structures.test_verion import TestVersion
from utils.colors import ColorPalette

# TODO: change the structure - not the best practice to use global variables

class UserArgs:
    OUTPUT_FOLDER = ""
    V1_COLOR = 'turquoise'
    V2_COLOR = 'orange'
    V2_IDENTIFIER = '2'


def set_output_folder(folder_name):
    if folder_name == "":
        return
    UserArgs.OUTPUT_FOLDER = folder_name

def get_output_folder():
    if UserArgs.OUTPUT_FOLDER == "":
        return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")

    return UserArgs.OUTPUT_FOLDER

def set_v2_identifier(identifier):
    if identifier == "":
        return
    UserArgs.V2_IDENTIFIER = identifier[0]

def set_colors(colors):
    if colors is None or len(colors) != 2:
        return
    if colors[0] in ColorPalette.COLORS_FOR_GRADIENT and colors[1] in ColorPalette.COLORS_FOR_GRADIENT:
        UserArgs.V1_COLOR = colors[0]
        UserArgs.V2_COLOR = colors[1]

def get_color_by_version(version):
    if version == TestVersion.V1:
        return UserArgs.V1_COLOR
    else:
        return UserArgs.V2_COLOR

def determine_version(file_name):
    if UserArgs.V2_IDENTIFIER in file_name:
        print("Detected v2 file")
        return TestVersion.V2
    else:
        return TestVersion.V1