#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author: huanzhiqiang  
@file: exp-gameops-salt.py  
@time: 2019/10/18 13:59
"""
import os
files_list=[]

def find_files_in_dir(search_name,dir_path):
    dirname_path=os.path.abspath(dir_path)
    print("###",dirname_path)
    if os.path.exists(dirname_path) and os.path.isdir(dir_path):
        if search_name in os.listdir(dirname_path):
            files_list.append(dirname_path)
        for line in os.listdir(dirname_path):
            path=os.path.join(dirname_path,line)
            if os.path.isdir(path):
                find_files_in_dir(search_name,path)
            else:
                current_file_name=os.path.split(line)[1]
                # print("##########################",path)
                file_path=os.path.join(path,path)
                print(file_path)


def read_file(file_name):
    with open(file_name,'rb') as f:
        file_content=f.readline()
        return file_content

def write_bytes_to_file(filename,write_content):
    with open(filename,'w') as f:
        f.write(write_content)

def write_list_to_file(file_name,write_content):
    with open(file_name,'w') as f:
        f.writelines(write_content)

def append_bytes_to_file(file_name, write_content):
    with open(file_name, "a") as f:
        f.write(write_content)


def append_list_to_file(file_name, write_content):
    with open(file_name, "a") as f:
        f.writelines(write_content)

def make_dir(dir_name):
    os.mkdir(dir_name)

def rm_dir(dir_name):
    os.rmdir(dir_name)

def split_path(path):
    return os.path.split(path)

def rename_file_or_dir(old_name,new_name):
    os.rename(old_name,new_name)

def remove_file(file_name):
    os.remove(file_name)

if __name__ == '__main__':
    find_files_in_dir("cmd.txt","E:\develop-project\eanju-drill-exp1")
    print(files_list)




# eval('{"name":"赵四","password":"123"}')
# eval('{"hzq":123,"ee":34}')
# eval('{"h":"12","q":"12"}')