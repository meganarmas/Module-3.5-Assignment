# Objective: The goal of this assignment is to deepen your understanding 
# of the OS module in Python.
# Task 1: Directory Inspector:

# Problem Statement: Create a Python script that lists all 
# files and subdirectories in a given directory. Your script 
# should prompt the user for the directory path and then display the contents.

# Code Example:
    # import os

   # def list_directory_contents(path):
        # List and print all files and subdirectories in the given path

# Expected Outcome: The script should correctly 
# list all files and subdirectories in the specified directory. 
# Handle exceptions for invalid paths or inaccessible directories

import os

user_path = input("Enter pathway: ")

def list_directory_contents(path):
    try:
        if os.path.exists(path):
            contents = os.listdir(path)
            print(f"Directory contents: {contents}")
        else:
            print("Files were not found. Please add proper folder name.")
    except FileNotFoundError:
        print("Files were not found.")


list_directory_contents(user_path)