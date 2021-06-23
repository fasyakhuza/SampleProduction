#!/bin/bash

python sim_submit_condor.py -f infile_Vector_MonoZLL_NLO_Mphi-500_Mchi2-150_Mchi1-1_gSM-0p25_gDM-1p0_ctau0p1.txt -p x509up_u47865
python sim_submit_condor.py -f infile_Vector_MonoZLL_NLO_Mphi-500_Mchi2-150_Mchi1-1_gSM-0p25_gDM-1p0_ctau1p0.txt -p x509up_u47865
python sim_submit_condor.py -f infile_Vector_MonoZLL_NLO_Mphi-500_Mchi2-150_Mchi1-1_gSM-0p25_gDM-1p0_ctau10p0.txt -p x509up_u47865
python sim_submit_condor.py -f infile_Vector_MonoZLL_NLO_Mphi-500_Mchi2-150_Mchi1-1_gSM-0p25_gDM-1p0_ctau100p0.txt -p x509up_u47865
python sim_submit_condor.py -f infile_Vector_MonoZLL_NLO_Mphi-500_Mchi2-150_Mchi1-1_gSM-0p25_gDM-1p0_ctau1000p0.txt -p x509up_u47865
