import os
import pprint


def count_files_cwd(path):
    # directory path
    # working_dir = os.getcwd()

    # count total subdirectories
    total_files_per_dir = [[root, len(files)] for root, _, files in os.walk(path)]

    # display total
    pprint.pprint(total_files_per_dir)
    return
    

# get class code of current path
def get_class_code(classname):
    class_codes = {
        'ako': 1,
        'araw': 2,
        'deaf': 3,
        'hearing': 4,
        'hindi': 5,
        'ikaw': 6,
        'ingat': 7,
        'kamusta': 8,
        'konti': 9,
        'mabuhay': 10,
        'mabuti': 11,
        'mahal-kita': 12,
        'mali': 13,
        'oo': 14,
        'pakisuyo': 15,
        'pakiulit': 16,
        'pasensya': 17,
        'salamat': 18,
        'tama': 19,
        'teka': 20
    }
    return class_codes.get(classname, None)