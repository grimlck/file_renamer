#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import sys


section_delimiter="-"
word_delimiter=" "
new_word_delimiter="_"
extension = None

def split_file_name(file_name):
    global extension
    second_split=[]
    pure_file_name = os.path.splitext(file_name)[0]
    extension = os.path.splitext(file_name)[-1]
    first_split = pure_file_name.split(section_delimiter)
    if len(first_split[0]) == 1:
        first_split[0]="0"+first_split[0]
    if len(first_split) > 1:
        for item in first_split:
            second_split.append(item.strip().lower().split(word_delimiter))
    
    return second_split

def join_file_name(split_list):
    first_join = []
    new_file_name=""
    
    try:
        if len(split_list) > 1:
            for item in split_list:
                first_join.append(new_word_delimiter.join(item))
                
        if len(first_join) > 1:
            new_file_name = section_delimiter.join(first_join)+extension
        else:
            new_file_name = first_join[0]+extension
            
        return new_file_name
    except IndexError:
        return new_file_name
    #return first_join
            
def main():    
    if len(sys.argv) > 1:
        directory = os.path.abspath(sys.argv[1])
        if os.path.exists(directory) and os.path.isdir(directory):
            os.chdir(directory)
            cwd = os.getcwd()
            for file in os.listdir(cwd):
                if os.path.isfile(file):
                    if split_file_name(file):
                        joined = join_file_name(split_file_name(file))
                        if joined != file:
                            if not os.path.exists(joined):
                                os.renames(file, joined)
                            else:
                                print joined+" already exists!"
                        else:
                            print file+" already sane!"
            

if __name__ == "__main__":
     main()
        
        
    
    
 