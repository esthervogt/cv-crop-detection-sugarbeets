# Author: Esther Vogt
# Creation Date: 30.05.2021
# Purpose: Contains functions used to assess directory structure/files and load/pre-process image data


def getListOfFiles(dirName):
    """
    dirName: str for directory path from which the list of contained files should be returned
    returns: list of all filenames in directory
    """

    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles


def generate_id_col(list_, col1, col2):
    """
    list_: row of dataframe
    col1: first column to be included in id
    col2: second column to be included in id
    returns: unique id generated from (set of) col1/col2
    """
    if isinstance(list_[col1], str):
        return list_[col1]
    elif isinstance(list_[col2], str):
        return list_[col2]
    return []
