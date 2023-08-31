from setuptools import setup
from typing import List


#DECLARING VARIABLES
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Ryan Mathew"
DESCRIPTION="This my first ml project"
PACKAGES=["housing"]
REQUIREMENTS_FILE_NAME="requirements.txt"
# the below function will returrn requirements list in requirements.txt  which contain name of libraries
def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()

)

