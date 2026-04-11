import shutil
import os 


def copy_static(curr_directory, target):
    if not os.path.exists(target):
        os.mkdir(target)
    for current in os.listdir(curr_directory):
        joint_current = os.path.join(curr_directory, current)
        if os.path.isfile(joint_current):
            shutil.copy(joint_current, os.path.join(target, current))
        else:
            copy_static(os.path.join(curr_directory, current), os.path.join(target, current))
