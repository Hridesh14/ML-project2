from setuptools import setup,find_packages
import os
from typing import List
hypen_e_dot ='_e .'

def get_requirements(file_path:str)->list[str]:
    '''This function will reture the list of string as requirements '''
    requirments =[]
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments =[req.replace('\n','')for req in requirments]
        if hypen_e_dot in requirments:
            requirments.remove(hypen_e_dot)
            return requirments
setup(
    name='MlProject_2_student_scorePred',
    version='0.0.0.1',
    author='Hridesh Maithani',
    packages= find_packages(),
    install_reuires =get_requirements('requirements.txt')
)