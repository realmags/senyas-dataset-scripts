import winsound
import cv2
import os
import utils

def main():
    scale_ratio = 0.6

    # change dir to 'classification'
    classname = 'teka'
    class_code = utils.get_class_code(classname)
    base_dir = os.path.join(os.path.dirname(os.getcwd()), 'classification')
    source_dir = os.path.join(base_dir, classname)
    destination_dir = os.path.join(os.path.dirname(os.getcwd()), 'fsl-signs', classname)

    # resize image according to custom dimesion
    dims = (224, 224)

    # count number of items
    counter = 0

    if class_code is None:
        print('INVALID CLASS NAME', classname)
        raise Exception('ERRO: INVALID CLASSNAME')

    if not os.path.exists(base_dir):
        print('BASE PATH DOES NOT EXIST', base_dir)
        raise Exception('ERRO: NO PATH')

    if not os.path.exists(source_dir):
        print('SOURCE FOLDER DOES NOT EXIST', source_dir)
        raise Exception('ERRO: NO PATH')

    if not os.path.exists(destination_dir):
        print('CREATING DESTINATION FOLDER', destination_dir)
        os.mkdir(destination_dir)

    # iterate through each directory
    print('WORKING ON', source_dir)

    for file in os.scandir(source_dir):
        print('READING IMAGE', file.name, '...................')
        counter = counter + 1
        _, ext = os.path.splitext(file.name)
        filename = os.path.join(destination_dir, f'{class_code}_{counter}{ext}')

        img = cv2.imread(file.path)
        resized_img = cv2.resize(img, dims, interpolation=cv2.INTER_LINEAR)
        cv2.imwrite(filename, resized_img)
        print('SUCCESSFULLY RESIZED IMAGE', file.name)
        
    # resized_img = cv2.resize(img, None, fx=scale_ratio, fy=scale_ratio, interpolation=cv2.INTER_LINEAR)
    
    print(f"## SUCCESSFULLY RESIZED ALL {counter} IMAGES OF CLASS '{classname.upper()}' ##")
    winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS)


if __name__ == '__main__':
    main()