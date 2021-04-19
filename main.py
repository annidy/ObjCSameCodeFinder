# coding: utf-8

import sys
import re
import os
from simhash import Simhash, SimhashIndex
from functools import cmp_to_key
from filehash import FileHash
import simplejson as json

gb_detail  = 0
gb_max_dis = 20 
gb_min_linecount = 3
gb_output = "out.json"


def main(argv):
    global gb_output
    root_path= argv[1]

    for arg in argv:
        if arg == "--help":
            print_help()
            return
        elif arg == "--detail":
            gb_detail = 1
        elif arg == "--functions":
            funciton_standard = 1
        elif arg.startswith("--max-distance="):
            arg_arr = arg.split("=")
            gb_max_dis = int(arg_arr[1])
        elif arg.startswith("--min-linecount="):
            arg_arr = arg.split("=")
            gb_min_linecount = int(arg_arr[1])
        elif arg.startswith("--output="):
            arg_arr = arg.split("=")
            gb_output = arg_arr[1]


    if not os.path.isdir(root_path):
        print("You must assign a dir as first input")
        return 


    hashed_arr  = hash_funcs(root_path)

    print("Ranking all the hash results...")
    ranked_arr  = rank_hash(hashed_arr)

    print("Sorting all the ranked results...")
    sorted_arr = sorted(ranked_arr, key=cmp_to_key(lambda x,y:x[2]-y[2]))

    output_file = open(gb_output, 'w+')
    print(json.dumps(sorted_arr), file=output_file)

    print("Finishd")


def hash_funcs(root_path):
    hashed_arr = []

    for file_path in scan_files(root_path):
        filehash = FileHash(file_path)
        for func in filehash.funcList:
            if func.lineCount >= gb_min_linecount:
                func.hashSource()
                hashed_arr.append(func)

    return hashed_arr

def rank_hash(hashed_arr):
    global gb_detail
    global gb_max_dis

    ranked_arr = []
    count = len(hashed_arr)
    for i in range(0, count):
        obj1 = hashed_arr[i]
        min_distance = 1000
        best_match = None

        for j in range(i + 1, count):
            obj2 = hashed_arr[j]
            distance = obj1.distance(obj2)
            if distance < min_distance:
                min_distance = distance
                best_match = obj2
        
        if best_match != None:
            if min_distance < gb_max_dis:
                ranked_arr.append((obj1, best_match, min_distance))
    
    return ranked_arr

#############################################
############### File Processor ##############
def scan_files(directory,prefix=None,postfix=".m"):  
    files_list=[]  
      
    for root, sub_dirs, files in os.walk(directory):  
        for special_file in files:  
            if postfix:  
                if special_file.endswith(postfix):  
                    files_list.append(os.path.join(root,special_file))  
            elif prefix:  
                if special_file.startswith(prefix):  
                    files_list.append(os.path.join(root,special_file))  
            else:  
                files_list.append(os.path.join(root,special_file))  
                            
    return files_list 

def file_name(file_path):
    name_arr=file_path.split("/")
    file_name=name_arr[len(name_arr) - 1]
    return file_name

##########################################
############ Help ########################
def print_help(): 
    print("Usage:\n")
    print("\tpython SameFileFinder.python [arg0]\n")
    print("Args:\n")
    print("\t[arg0] - Target Directory of files should be scan")
    print("\t--max-distance=[input] - max hamming distance to keep, default is 20")
    print("\t--min-linecount=[input] - for function scan, the function would be ignore if the total line count of the function less than min-linecount")
    print("\t--detail    - Show the detail of process\n")
    print("\t--output=[intput] - Customize the output file, default is \"out.json\"")

if __name__ == '__main__':
    main(sys.argv)