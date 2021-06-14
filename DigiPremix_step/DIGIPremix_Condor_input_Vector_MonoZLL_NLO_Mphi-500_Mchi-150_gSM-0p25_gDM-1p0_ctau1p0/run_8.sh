#!/bin/bash

export RUN_DIR=/afs/cern.ch/work/t/tsarkar/private/LV/GenProduction_V1/CMSSW_10_6_18/src/DigiPremix_step/DIGIPremix_Condor_input_Vector_MonoZLL_NLO_Mphi-500_Mchi-150_gSM-0p25_gDM-1p0_ctau1p0

cd ${RUN_DIR}
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
export SCRAM_ARCH=slc7_amd64_gcc820
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
export LD_LIBRARY_PATH=$PWD:$LD_LIBRARY_PATH
cmsRun -p DIGIPremix_run_9.py 
