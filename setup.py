from setuptools import find_packages,setup
from typing import List

def get_requirments(file_path:str)->List[str]:
    requirments = []
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments=[rec.replace('/n','') for rec in requirments]
        
        if '-e .' in requirments:
            requirments.remove('-e .')
    return requirments
        

setup(
    name='mlproject',
    version='0.0.1',
    author='sankalp',
    author_email='sankalp.makol16@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments('requirements.txt')
)