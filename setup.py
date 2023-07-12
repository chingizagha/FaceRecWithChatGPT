from distutils.core import setup
import numpy as np
import py2exe

setup(
    options = {'py2exe': {'bundle_files': 1, 'packages': 'cv2'}},
    windows = {"main.py"},
    package_dir= {"": "Images", "": "Videos", "": "Resources"},
)