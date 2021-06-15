#!/bin/bash

python hlt_submit_condor.py -f infile_Vector_MonoZLL_NLO_Mphi-500_Mchi-150_gSM-0p25_gDM-1p0_ctau0p1.txt
python hlt_submit_condor.py -f infile_Vector_MonoZLL_NLO_Mphi-500_Mchi-150_gSM-0p25_gDM-1p0_ctau1p0.txt
python hlt_submit_condor.py -f infile_Vector_MonoZLL_NLO_Mphi-500_Mchi-150_gSM-0p25_gDM-1p0_ctau10p0.txt
python hlt_submit_condor.py -f infile_Vector_MonoZLL_NLO_Mphi-500_Mchi-150_gSM-0p25_gDM-1p0_ctau100p0.txt
