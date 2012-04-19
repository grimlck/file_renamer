#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import sys


section_delimiter="-"
word_delimiter=" "
new_word_delimiter="_"
#extension = None
replacement=[
             ["'",""],
             [" ","_"],
             [".",""],
             ["ß","ss"],
             ["[","("],
             ["]",")"]
             ]

def replace_chars(string,replacement_list):
    if string and replacement_list:
        for item in replacement_list:
            string = string.replace(item[0],item[1])
            
    return string

def rename_files(directory):
    if os.path.exists(directory) and os.path.isdir(directory):
        os.chdir(directory)
        cwd = os.getcwd()
        for file in os.listdir(cwd):
            if os.path.isfile(file):
                extension = os.path.splitext(file)[-1]
                file_name = os.path.splitext(file)[0]
                splitted_file_name = file_name.split("-")
                if len(splitted_file_name[0]) == 1:
                    splitted_file_name[0] = "0"+splitted_file_name[0]
                    
                file_name = "-".join(item.strip() for item in splitted_file_name)
                    
                
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
        
        
    
    
 