from CRABClient.UserUtilities import config, getUsernameFromCRIC

config = config()

config.General.requestName = "wgen_Vector_MonoZLL_NLO_Mphi-500_Mchi-1_gSM-0p25_gDM-1p0_ctau1p0"
config.General.workArea = "crab_projects"
config.General.transferLogs = True
config.General.transferOutputs = True

config.JobType.pluginName = "PrivateMC"
config.JobType.psetName = "run_wgen_Vector_MonoZLL_NLO_Mphi-500_Mchi-1_gSM-0p25_gDM-1p0_ctau1p0.py"
#config.JobType.maxMemoryMB = 4000
#config.JobType.numCores = 8

config.Data.outputPrimaryDataset = "wgen_Vector_MonoZLL_NLO_Mphi-500_Mchi-1_gSM-0p25_gDM-1p0_ctau1p0"
config.Data.outLFNDirBase = "/store/user/%s/" % (getUsernameFromCRIC())#FIXME
config.Data.outputDatasetTag = "RunIISummer20UL17_wmLHEGEN"
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 50
NJOBS = 20
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True

config.Site.storageSite = "T2_CH_CERN"
