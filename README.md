# Backdoor
This is a command line-based backdoor which will take control of the system on which it is run also it is written in python.

This zip file contains 2 files: - 

Document.doc: This file is what you are reading. This file has all Instructions related to how to Execute this code.

backdoor.py: - It is a file that contains our main code which is a client model use to take control over others machines.

Netcat: - A tool that will listens our backdoor take the connection back to our machines.

Requirements

To run this project, we need to install the following Software’s.

Python3 : Python3 Programming Language that is used to develop/write the programs.

Pycharm IDE : Pycharm Integrated Development Environment is used to develop the Code.

Ubuntu(any linux Distribution) : Any distribution of Linux is fine, however this time we are using Ubuntu

Steps to Use the Files.

Step 1: Unzip the zip file.

Unzip program.zip -d destination_folder

Step 2: Change the directory to the Unzipped Folder

cd /Backdoor

Step 3: Give permissions to the Python Files which makes them Executable

chmod +x *.py

Step 4: We Run this Python file on victims’ machine by using the Terminal

Python bakcdoor.py

Step 5: Now run the netcat tool nc -lvnp 1234 to take the connection back.

Step 6: Now we can control the victim’s machine
