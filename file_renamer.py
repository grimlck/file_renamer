#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
This program replaces special characters in a file with the following naming scheme
    01-Interpret-Titel.ext
NOTE: only works on operating systems which handle their file names case sensitiv
"""


import os
import sys


section_delimiter="-"
word_delimiter=" "
new_word_delimiter="_"

# dictionary of character replacements
replacement=[
    ["'","_"],
    [" ","_"],
    [".",""],
    ["ß","ss"],
    ["[","("],
    [",",""],
    ["]",")"],
    ["!",""],
    ["?",""]
]

def replace_chars(string,replacement_dict):
    """
    replace the characters in a string according to a dictionary
    """
    if string and replacement_dict:
        for item in replacement_dict:
            string = string.replace(item[0],item[1])
            
    return string

def rename_files(directory):
    """
    rename a file, after replacing spacial characters
    """

    if os.path.exists(directory) and os.path.isdir(directory):
        os.chdir(directory)
        cwd = os.getcwd()
        # iterate over files in the given directory
        for file in os.listdir(cwd):
            if os.path.isfile(file):
                # split the file name into extension and the name
                extension = os.path.splitext(file)[-1]
                file_name = os.path.splitext(file)[0]

                # split the file name into sections 
                splitted_file_name = file_name.split("-")

                # add 0 to the beginning of the filename
                if len(splitted_file_name[0]) == 1:
                    splitted_file_name[0] = "0"+splitted_file_name[0]
                
                # join the sections
                file_name = "-".join(item.strip() for item in splitted_file_name)
                    
                # replace special chars and rebuild the file name
                file_name = replace_chars(file_name,replacement)
                file_name = file_name+extension
                file_name = file_name.lower()
                if file_name != file:
                    if not os.path.exists(file_name):
                        os.renames(file,file_name)
                    else:
                        print file_name+" already exists"
        
        return 0
    else:
        return 1

def main():    
    if len(sys.argv) > 1:
        directory = os.path.abspath(sys.argv[1])
        rename_files(directory)
 
        sys.exit(0)
    else:
        print "No directory specified."
        sys.exit(1)
            

if __name__ == "__main__":
     main()
