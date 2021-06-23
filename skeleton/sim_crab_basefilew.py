from CRABClient.UserUtilities import config, getUsernameFromCRIC

config = config()

config.General.requestName = "sim_vector_monoZLL_NLO_Mphi-10000_Mchi-1000_gSM-0p25_gDM-1p0"
config.General.workArea = "crab_projects"
config.General.transferLogs = True
config.General.transferOutputs = True

config.JobType.pluginName = "Analysis"
config.JobType.psetName = "run_crab.py"
config.JobType.maxMemoryMB = 4000
config.JobType.numCores = 4

config.Data.inputDataset = "/wgen_Vector_MonoZLL_NLO_Mphi-10000_Mchi-1000_gSM-0p25_gDM-1p0/tsarkar-RunIISummer20UL17_wmLHEGEN_RAWSIMoutput-5e06348d3746297a6f3bfa82ab553caa/USER" 
config.Data.outLFNDirBase = "/store/user/%s/" % (getUsernameFromCRIC())
config.Data.outputDatasetTag = "RunIISummer20UL17_SIM"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.ignoreLocality = True

config.Site.storageSite = "T2_CH_CERN"
config.Site.whitelist = ["T2_*","T3_*"]
