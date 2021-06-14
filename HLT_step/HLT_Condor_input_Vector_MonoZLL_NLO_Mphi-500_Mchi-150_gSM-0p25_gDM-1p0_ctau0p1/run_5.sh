#!/bin/bash

export RUN_DIR=/afs/cern.ch/work/t/tsarkar/private/LV/GenProduction_V1/CMSSW_9_4_14_UL_patch1/src/HLT_step/HLT_Condor_input_Vector_MonoZLL_NLO_Mphi-500_Mchi-150_gSM-0p25_gDM-1p0_ctau0p1

cd ${RUN_DIR}
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
export SCRAM_ARCH=slc7_amd64_gcc820
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
export LD_LIBRARY_PATH=$PWD:$LD_LIBRARY_PATH
cmsRun -p HLT_run_6.py 
