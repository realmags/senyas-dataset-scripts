import os
import splitfolders

# split percentage
# training cohort: 60%
# validation cohort: 20%
# test cohort: 20%
ratio = (0.6, 0.2, 0.2)
base_path = os.path.join(os.path.dirname(os.getcwd()))
input_folder = os.path.join(base_path, 'fsl-signs')
output_folder = os.path.join(base_path, 'fsl-signs-split')

splitfolders.ratio(input_folder, output=output_folder, ratio=ratio)

print('### DATA SPLITTING COMPLETE ###')