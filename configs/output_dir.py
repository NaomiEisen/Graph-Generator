import datetime

OUTPUT_FOLDER = ""


def set_output_folder(folder_name):
    global OUTPUT_FOLDER
    if folder_name == "":
        return
    OUTPUT_FOLDER = folder_name

def get_output_folder():
    if OUTPUT_FOLDER == "":
        return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")

    return OUTPUT_FOLDER