import os
from traceback import print_tb

# get class code of current path
def get_class_code(pwd):
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
    return class_codes.get(pwd, None)

# current path
dir = os.getcwd()
print(f'WORKING DIR: {dir}')


# rename all files in each subdirectory
for subdir in os.scandir(dir):
    if subdir.is_dir():
        index = 1 # index for number of files
        class_code = get_class_code(subdir.name)
        if class_code is None: raise Exception('Invalid class name')
        for file in os.scandir(subdir.path):
            _, ext = os.path.splitext(file.name)
            filename = os.path.join(subdir.path, f'{class_code}_{index}{ext}')
            index = index + 1
            os.rename(file.path, filename)

        print(f'SUCCESSFULLY RENAMED FILES IN /{subdir.name}')


# rename subdirectories in RAW DATASET
# for file in os.scandir(dir):
#     if file.is_dir():
#         _, classname = file.name.split('raw ')
#         dirname = os.path.join(dir, classname)
#         os.rename(file.path, dirname)