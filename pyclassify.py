#!/usr/bin/python3.3

import sys
import argparse
import rules_handler as rh
import mime_handler as mh
import os
import shutil


def print_file(rules):
    for l in rules:
        print("Type : ", l[0], "\tTo : ", l[1])
        
    
def add_file(option, rules):
    i = 0
    
    while i < len(option) :
        try:
            r = [option[i], option[i+1]]
            rules.append(r)
        except IndexError:
            print("arg : \""+ option[i] + "\" is not a couple !")
        i+=2

def move_file(rules, f):
    
    mime = mh.getMime(f)
    
    for r in rules:
        if mime == r[0]:
            print("Moving : " + f + " to : " + r[1])
            shutil.move(f, r[1])

def move_files(rules, path="."):
    listfiles = os.listdir(path)
    
    for f in listfiles:
        if os.path.isfile(f):
            move_file(rules, f)
    
    
def main():
    
    files = []    
    fn = "rules.csv"
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-p", action="store_true", dest="print", help="print the current organizing rules")
    parser.add_argument("-a", action="store", dest="add", nargs='*', help="add the tuple mimetype/path to the ruleset")
    parser.add_argument("-f", action="store", dest="filename", nargs=1, help="specify the ruleset file to use")
    parser.add_argument("-c", action="store", default=".", dest="clean", help="Classify the file following the rules")
   
    result = parser.parse_args()
    
    if result.filename:
        fn = result.filename[0]
    
    rh.load_rules(files, filename=fn)

    if result.add:
        add_file(result.add, files)

    if result.print:
        print_file(files)
        
    if result.clean:
        move_files(files, path=result.clean)
        
    
        
    rh.write_rules(files, filename=fn)
   
if __name__ == "__main__":
    main()
