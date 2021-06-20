run_script_template='''#!/bin/bash

export RUN_DIR=RUNDIR

cd ${RUN_DIR}
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
export SCRAM_ARCH=slc7_amd64_gcc820
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
export LD_LIBRARY_PATH=$PWD:$LD_LIBRARY_PATH
cmsRun -p CFGFILE 
'''

condor_template = """universe              = vanilla
Proxy_filename = x509up
Proxy_path = /proxypath/$(Proxy_filename)
executable            = EXEC
arguments             = $(ClusterID) $(ProcId) $(Proxy_path)
output                = OUTPUT/job_JOB_NUMBER.out
error                 = OUTPUT/job_JOB_NUMBER.err
log                   = OUTPUT/job_JOB_NUMBER.log
queue
"""
