#!/usr/bin/env python

import os, sys, re
import shutil
import subprocess

def create_inputfiles(path,input_dir):
        full_path=path+input_dir
        infile= str(input_dir).replace('DIGIPremix_Condor_output_','infile_')+'.txt'
        print os.getcwd(), infile
        out_txtfile= open(os.path.join(os.getcwd(),infile),'w')
        for root, subFolder, files in os.walk(full_path):
                for item in files:
                        if item.endswith(".root") :
                                fileNamePath = str(os.path.join(root,item))
                                print(fileNamePath)
                                out_txtfile.write(fileNamePath+'\n')



def main():
        from argparse import ArgumentParser
        import argparse
        parser = ArgumentParser(description="Do -h to see usage")

        #parser.add_argument('-i', '--txt', action='store_true', help='input txt file name')
        #parser.add_argument('-f', '--txt',help='txt file input',type=argparse.FileType('r'),)
        #parser.add_argument('--f', type=open)

        parser.add_argument('-p', '--path', type=str)
        parser.add_argument('-d', '--dire', type=str)

        args = parser.parse_args()

        print(args)

        create_inputfiles(args.path,args.dire)


if __name__ == "__main__":
        main()
