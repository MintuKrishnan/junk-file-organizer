# Junk File Organizer with Python


Junk File Organizer helps to organize all your files by moving files into folders based on their name, type, size and year created. This application is written in Python3 and can be used as either a stand-alone python script that can be run within the python terminal or a Mac OX executable app version which is ready-to-run available.


## Contents
    - Introduction
    - Main functionality of this code
    - Setup
    - How to use this
    - What I used
    - Future improvement


## Main functionality of this code

    * Organize by extension
    * Organize by size
    * Organize by year
    * Organize by type
    * Organize by date


## Setup

    1.	Clone this repo

    2.	Install Python 3

    3.	Install Flake8 library
                1.	pip install flake8
                2.	Run python -m flake8 command and check for any errors

    4.	Run python3 main.py -h
                1.	There you can see all the details of the project
                2.	-p/--path is the flag for specifying the path
                3.	-o/--order is the flag for specifying the order
                4.	-h/--help is the flag to get help
                5.	Path is mandatory to specify
                6.	Order is optional, by default the sorting order will be of type

    5.	After running the program you will get a successful message 

    6.	Go to the path and look the folder the organized or not



## How to use this


### 1. Organize by extension

By using this option user can organize their files by their file extension in a given folder, folder will be created according to file extension and finally all files will be moved to a created folder.

        python3 main.py -p /Users/mintukrishnan/Downloads -o extension


### 2. Organize by size

By using this option user can organize their files by their file size, B, KB, MB,GB etc used

        python3 main.py -p /Users/mintukrishnan/Downloads -o size


### 3. Organize by date

By using this option user can organize their files by last modified date. random folders will be created according to file's last used date and files will be moved to them.

        python3 main.py -p /Users/mintukrishnan/Downloads -o date

### 4. Organize by type

By using this option user can organize their files by their type of the file. if its a .pdf, it will move to the Document folder, if its a .jpg file it will move to the Image folder

        python3 main.py -p /Users/mintukrishnan/Downloads -o type


### 5. Organize by year

By using this option user can organize their files by year. if a file is created in 2018, it will move to a 2018 folder

        python3 main.py -p /Users/mintukrishnan/Downloads -o year`


### For running mac executible file

Go to path `mac application/main-prompt.app/Contents/MacOS/main-prompt` and run it. 


## What I Used :
    
    I used many built-in libraries like- shutil for file movement,datetime for get the date of the files,argparse for the command line parsing and etc.


## Future Improvement:
    
    We can design the ui for the program so a normal user can easily interact with it.
    We can add more features like deleting the junk files after a certain period of time.

