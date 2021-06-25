import os
import sys
import random
import argparse
import json
import shutil
import subprocess

def create_jobs(input_jsonfile):
	cmsdriver_sh = open("submit_crab_job_step_MiniAOD.sh","w")
	cmsdriver_sh.write("#!/bin/bash\n")
	crab_file_list=[]
	with open(input_jsonfile) as data_file:    
		data = json.load(data_file)
		for sample, sample_cfg in data.items():		
			cfg_file="run_MiniAOD.py"
			shutil.copyfile("../skeleton/MiniAOD_basefile_crab_run.py",cfg_file)
		
			crab_file="submit_crab_"+sample_cfg["RequestName"]+".py"
			print(crab_file)
			#os.system('cp skeleton/crab_basefile.py '+crab_file)
			shutil.copyfile("../skeleton/digi_to_miniaod_crab_templete.py",crab_file)
			subprocess.call(["sed -i 's|###REQUESTNAME###|" + sample_cfg["RequestName"] + "|g' " + crab_file], shell=True)
			subprocess.call(["sed -i 's|###RUNCFGFILE###|" + cfg_file + "|g' " + crab_file], shell=True)
			subprocess.call(["sed -i 's|###INPUTDATASETTAG###|" + sample_cfg["InputDatasetTag"] + "|g' " + crab_file], shell=True)
			subprocess.call(["sed -i 's|###OUTPUTPRIMARYDATASET###|" + sample_cfg["OutputDatasetTag"] + "|g' " + crab_file], shell=True)
			crab_file_list.append(crab_file)
	  	

	print(len(crab_file_list))
	for i in range(len(crab_file_list)):
		print crab_file_list[i]
		cmsdriver_sh.write("crab submit "+crab_file_list[i]+"\n")	
	cmsdriver_sh.close()


def main():
        from argparse import ArgumentParser
        import argparse
        parser = ArgumentParser(description="Do -h to see usage")

        #parser.add_argument('-i', '--txt', action='store_true', help='input txt file name')
        #parser.add_argument('-f', '--txt',help='txt file input',type=argparse.FileType('r'),)
        #parser.add_argument('--f', type=open)

        parser.add_argument('-i', '--json', type=str)

        args = parser.parse_args()

        print(args)

        create_jobs(args.json)


if __name__ == "__main__":
        main()
