# SampleProduction UL 2017
## Setup framework

Setup a CMSSW release:
```
mkdir GenProduction
cd GenProduction
cmsrel CMSSW_10_6_18
cmsrel CMSSW_9_4_14_UL_patch1

cd CMSSW_10_6_18/src
cmsenv
```
Checkout this framework and switch to this branch:
```
git clone -b UL_2017 https://github.com/tanmayvb/SampleProduction.git
cd CMSSW_10_6_18/src
cmsenv
```
Then compile:
```
scram b -j4
```

## STEP1: Prepare Configuration file
```
cd Configuration/GenProduction/python
```
 Run: 
```
python createFragments_2017.py
```  
#### It will create cfg file from different gridpack and for different ctau values

```
cd ${CMSSW_BASE}/src
```
and then compile:
```scram b -j4```

Set proxy:
```
voms-proxy.int
```
## STEP2: wGen
```
cd wGen_step
```
```python config_wgen.py -i input_mphi_500_mchi_150_and_1.json```  with input of a json file

It will create a sh file create_confg_run_crab.sh which contain everyting and will submit crab jobs

To run and submit crab job: ```sh create_confg_run_crab.sh```

## STEP3: SIM
```
cd ../SIM_step
```
##Prepare file like ```create_infile.sh``` ##which contain output path and directory name of previous wGen step output

##run: ```sh create_infile.sh``` ##It will create some **.txt file, contains each root file path of wGen step

##Remember to change output path and directory name of wGen step

##The to submit condor jobs for SIM step just run: ```sh create_submit_condor_sim_Mphi-500_Mchi-150_jobs.sh```


## STEP4: DIGIPremix (Same as SIM step)
```
cd ../DigiPremix_step
```
Prepare file like ```create_infile.sh``` which contain output path and directory name of previous SIM step output

run: sh ```create_infile.sh``` It will create some **.txt file, contains each root file path of SIM step

#### Remember to change your output path and directory name of SIM step

The to submit condor jobs for DIGIPremix step just run: ```sh create_submit_condor_digiPremix_Mphi-500_Mchi-150_jobs.sh```

## STEP5: HLT (Same as previous step)
```
cd ../../../CMSSW_9_4_14_UL_patch1/src/HLT_step
```
```cmsenv``` **This is different CMSSW version specially for HLT step**

Prepare file like ```create_infile.sh``` which contain output path and directory name of previous DIGIPremix step output

run: ```sh create_infile.sh``` It will create some **.txt** file, contains each root file path of DIGIPremix step

#### Remember to change your output path and directory name of DIGIPremix step

To submit condor jobs for HLT step just run: ```sh create_submit_condor_hlt_Mphi-500_Mchi-150_jobs.sh```

## STEP6: RECO (Same as previous step)
```
cd ../../../CMSSW_10_6_18/src/RECO_step/
```
Prepare file like ```create_infile.sh``` which contain output path and directory name of previous HLT step output

run: ```sh create_infile.sh``` It will create some **.txt** file, contains each root file path of HLT step

#### Remember to change your output path and directory name of HLT step

To submit condor jobs for RECO step just do run: ```sh create_submit_condor_reco_Mphi-500_Mchi-150_jobs.sh```

## STEP7: MiniAOD (Same as previous step)
```
cd ../MiniAOD_step
```
Prepare ```file like create_infile.sh``` which contain output path and directory name of previous RECO step output

run: ```sh create_infile.sh``` It will create some **.txt** file, contains each root file path of RECO step

###### Remember to change output path and directory name of RECO step

To submit condor jobs for MiniAOD step just run: ```sh create_submit_condor_MiniAOD_Mphi-500_Mchi-150_jobs.sh```
