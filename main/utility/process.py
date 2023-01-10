# process.py 
# Functions to help process files

import os
import sys

def txt_to_list(filepath: str) -> list:
    file = open(filepath, 'r')
    fileLines = file.readlines()
    file.close()

    list = []

    for fileLine in fileLines:
        line = fileLine.rstrip()
        if not line or '#' in line:
            continue
        list.append(line)

    file.close()
    return list

def preference_file_location_list(preferencePath: str) -> list:
    preferenceOptionFiles = next(os.walk(preferencePath))[2]
    preferenceOptionFileLocations = ['%s/%s' % (preferencePath, file) for file in preferenceOptionFiles]
    return preferenceOptionFileLocations

def name_from_file_path(filePath: str) -> str:
    file = os.path.basename(filePath)
    name = file.split('.')[0]
    return name

def curl_download(link: str, filepath: str) -> None:
    download_command = 'curl %s --output %s' % (link, filepath)
    os.system(download_command)

def filter_code(filepath: str, line: str) -> None:
    file = open(filepath, 'r')
    fileLines = file.readlines()
    file.close()

    file = open(filepath, 'w')
    for fileLine in fileLines:
        if line not in fileLine:
            file.write(fileLine)
    file.close()

def check_prompt() -> bool:
    if sys.argv.pop() == 'y':
        return True
    return False