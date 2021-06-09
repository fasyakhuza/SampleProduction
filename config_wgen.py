import os
import sys
import random
import argparse
import json
import shutil
import subprocess


cmsdriver_sh = open("create_confg_run_crab.sh","w")
cmsdriver_sh.write("#!/bin/bash\n")
crab_file_list=[]
with open('input_mphi_500_mchi_150_and_1.json') as data_file:    
	data = json.load(data_file)
	for sample, sample_cfg in data.items():		
		print "fname = ", sample_cfg["fragmentname"], ' ',sample_cfg["Nevents"]
		cfg_file="run_"+sample_cfg["RequestName"]+".py"
		cmsdriver_p = "cmsDriver.py "+sample_cfg["fragmentname"]+".py --no_exec --mc --python_filename "+cfg_file+" --fileout step_wgen.root --eventcontent RAWSIM --datatier GEN --step LHE,GEN --geometry DB:Extended -n 6284 --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed="+str(random.randint(1, 100000))+" --conditions 106X_mc2017_realistic_v6 --beamspot Realistic25ns13TeVEarly2017Collision --era Run2_2017"
		
		cmsdriver_sh.write(cmsdriver_p+"\n\n")
		crab_file="submit_crab_"+sample_cfg["RequestName"]+".py"
		print(crab_file)
		#os.system('cp skeleton/crab_basefile.py '+crab_file)
		shutil.copyfile("skeleton/crab_basefile.py",crab_file)
		subprocess.call(["sed -i 's|###REQUESTNAME###|" + sample_cfg["RequestName"] + "|g' " + crab_file], shell=True)
		subprocess.call(["sed -i 's|###RUNCFGFILE###|" + cfg_file + "|g' " + crab_file], shell=True)
		subprocess.call(["sed -i 's|###OUTPUTPRIMARYDATASET###|" + sample_cfg["OutputPrimaryDataset"] + "|g' " + crab_file], shell=True)
		subprocess.call(["sed -i 's|###INPUTDATASETTAG###|" + sample_cfg["OutputDatasetTag"] + "|g' " + crab_file], shell=True)
		subprocess.call(["sed -i 's|###UNITSPERJOB###|" + str(int(sample_cfg["Nevents"])/int(sample_cfg["Njobs"])) + "|g' " + crab_file], shell=True)
		subprocess.call(["sed -i 's|###NJOBS###|" + sample_cfg["Njobs"] + "|g' " + crab_file], shell=True)
		crab_file_list.append(crab_file)
	  	

print(len(crab_file_list))
for i in range(len(crab_file_list)):
	print crab_file_list[i]
	cmsdriver_sh.write("crab submit "+crab_file_list[i]+"\n")	
cmsdriver_sh.close()



