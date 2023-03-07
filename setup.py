from setuptools import find_packages, setup
from typing import List

#the next line is written so that "-e" doesn't get called when requirements.txt is called
hyphen_minue_e =  '-e .'

def get_requirements(file_path:str) -> List[str]:
    # this function will return the list of requirements
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if hyphen_minue_e in requirements:
            requirements.remove(hyphen_minue_e)

    return requirements


setup(
name = 'mlopsproject_test',
version = '0.0.1',
author = 'Abhilash',
author_email = 'abhilashgadepalli@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)

