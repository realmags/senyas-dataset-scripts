import cv2
import os
import math
import winsound

# ratio from the top
def cropByPercentage(img, dims, ratio):
    h, _, _ = img.shape
    height, width = dims
    offset = math.ceil(h * ratio)

    img = img[offset : height + offset, : width, :]
    return img

def main():
    working_dir = os.path.join(os.path.dirname(os.getcwd()), 'REDO')
    dims = (3880, 3880)
    ratio = 0.10
    # ratio = 0.15

    print('WORKING ON SOURCE DIRECTORY', working_dir)
    for file in os.scandir(working_dir):
        _, ext = os.path.splitext(file.name)
        file_destination = os.path.join(working_dir, 'CROPPED', file.name)

        if not file.is_file(): continue
        if ext != '.jpg': continue

        print('CROPPING IMAGE', file.name, '...........')
        img = cv2.imread(file.path)
        cropped_img = cropByPercentage(img, dims, ratio)
        cv2.imwrite(file_destination, cropped_img)
        print('NEW IMAGE SAVED', file.name)
        
    print('## SUCCESSFULLY CROPPED ALL IMAGES ##')
    winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS)


if __name__ == '__main__':
    main()