#!/usr/bin/env python

import os, sys, re
import shutil
import subprocess
sys.path.append("skeleton/")
from sim_condor_templete import *

def create_jobs(input_rootfiles):
	step ="digiPrimix"
	run_dir = os.path.join(os.getcwd(), step+'_Condor_input_'+str(input_rootfiles).replace('.txt',''))
	os.mkdir(run_dir)
	store_path="/eos/cms/store/user/tsarkar/"
	dir_name=store_path+step+"_Condor_output_"+str(input_rootfiles).replace('.txt','')
	os.mkdir(dir_name)
	#os.mkdir(os.path.join(run_dir, 'input'))
	filename = list()
	with open (input_rootfiles, "r") as myfile:
		for line in myfile:
			filename.append(line.strip())

	for i in range(len(filename)):
		print(filename[i])
		sim_cfg_file=step+"_run_"+str(i+1)+".py"
		infile= filename[i]
		outfile="step_"+step+"_2017UL_"+str(i+1)+".root"
		shutil.copyfile("skeleton/digiPrimix_basefile_run.py",os.path.join(run_dir,sim_cfg_file))
		subprocess.call(["sed -i 's|###INFILE###|" + infile + "|g' " + os.path.join(run_dir,sim_cfg_file)], shell=True)
		subprocess.call(["sed -i 's|###OUTFILE###|" + dir_name+"/"+outfile + "|g' " + os.path.join(run_dir,sim_cfg_file)], shell=True)
		run_script = run_script_template.replace('CFGFILE', sim_cfg_file)	
		run_script = run_script.replace('RUNDIR', run_dir)
		open(os.path.join(run_dir, 'run_{}.sh'.format(i)), 'w').write(run_script)
		
		condor_script = re.sub('EXEC', os.path.join(run_dir, 'run_{}.sh'.format(i)), condor_template)
          	#condor_script = re.sub('QUEUE', queue, condor_script)
          	condor_script = re.sub('JOB_NUMBER', str(i), condor_script)
          	condor_script = re.sub('OUTPUT', os.path.join(run_dir), condor_script)

          	open(os.path.join(run_dir, 'condor_{}.condor.jdl'.format(i)), 'w').write(condor_script)
		subprocess.call(["condor_submit",  "{0}".format(os.path.join(run_dir, 'condor_{}.condor.jdl'.format(i)))])

def main():
	from argparse import ArgumentParser
	import argparse
	parser = ArgumentParser(description="Do -h to see usage")

	#parser.add_argument('-i', '--txt', action='store_true', help='input txt file name')
	#parser.add_argument('-f', '--txt',help='txt file input',type=argparse.FileType('r'),)
	#parser.add_argument('--f', type=open)
	parser.add_argument('-f', '--txt', type=str)


  	args = parser.parse_args()

  	print(args)
	
	create_jobs(args.txt)



if __name__ == "__main__":
	main()
