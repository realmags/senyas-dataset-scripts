import cv2
import os
# import ipyplot

def bottomCrop(img, width, height):
    assert img.shape[0] >= height
    assert img.shape[1] >= width
    h, _, _ = img.shape
    
    img = img[ h - height : height + h, : width, :]
    return img


class_name = 'teka'

folder_path = os.path.join(os.getcwd(), class_name)
parent_path = os.path.dirname(os.getcwd())
folder_destination = os.path.join(parent_path, 'classification', class_name)
count = 0

if not os.path.exists(folder_path):
    print('PATH DOES NOT EXIST', folder_path)
    raise Exception('ERR: NO PATH')

print('WORKING ON SOURCE DIRECTORY', folder_path)

if not os.path.exists(folder_destination):
    print('CREATING DESTINATION DIRECTORY', folder_destination)
    os.mkdir(folder_destination)


for file in os.scandir(folder_path):
    print('READING IMAGE ', file.name, '........')
    file_destination = os.path.join(folder_destination, file.name)
    
    if not file.is_file(): continue

    img = cv2.imread(file.path)
    cropped_image = bottomCrop(img, 3880, 3880)
    cv2.imwrite(file_destination, cropped_image)
    print('SUCCESSFULLY CROPPED IMAGE', file.name)
    count = count + 1
    # raise Exception('End...')

print(f'ALL ({count}) IMAGES CROPPED')
