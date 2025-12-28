#this file is required to install the local package ie. QASystem in our virtual  environment. 
#to know a package is a local package , that file would have "__init__.py" file in it. 

from setuptools import find_packages, setup

setup(

    name="QAsystem with haystack", #package name.
    version="0.0.1",
    author="nikita",
    author_email="nikitaarora4521@gmail.com",
    packages=find_packages(),
    install_requires=["pinecone-haystack","haystack-ai","fastapi","uvicorn","python-dotenv","pathlib"] #all the requirements.txt installs come here. 


)