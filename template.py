import os
from pathlib import Path # / and \ slash problems would be resolved using this library.
import logging

# creating and defining logger
logging.basicConfig(filename= 'logging.log',
    level = logging.INFO,
    format="[%(asctime)s : %(levelname)s]: %(message)s"
)

# create a project name
while True:
    project_name = input("Ente the Project name: ")
    if project_name != '':
        break

logging.info(f"Creating project by name: {project_name}")

# list of files:
list_of_files = [
    ".github/workflows/.gitkeep", # this is a dummy file that is cerated to keep the structure intact
    f"src/{project_name}/__init__.py", # this will let me know that this is project
    f"tests/__init__.py", # these are for testing the program with unit test and intigration test
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    "init_setup.sh", # it will allow to do the basic environment setup
    "requirements.txt", # it will import all the required files
    "requirements_dev.txt", # this is to keep the requirements for testing such as pytest and others
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(Path(filepath))
    if filedir != "":
        os.makedirs(filedir, exist_ok = True) # This will create a dir
        logging.info(f"Creating a directory at: {filedir} for file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): 
        with open(filepath, "w") as f: # this will creaing a new empty file with the file name
            pass
            logging.info(f"Creating a new file: {filename} for path: {filepath}")
    else:
        logging.info(f"File is already exists at: {filepath}")