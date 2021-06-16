#!/usr/bin/env python
import os


dirs = ['DMSimp_DM_MonoZLL_NLO_Mphi-500_Mchi2-150_Mchi1-1_gSM-0p25_gDM-1p0','DMSimp_DM_MonoZLL_NLO_Mphi-500_Mchi2-1_Mchi1-1_gSM-0p25_gDM-1p0'] #organizing directories.

Tarballs = ['/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.4.3/DMVector_ZLL_NLO/v1/Vector_MonoZLL_NLO_Mphi-500_Mchi-150_gSM-0p25_gDM-1p0_13TeV-madgraph_tarball.tar.xz','/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.4.3/DMVector_ZLL_NLO/v1/Vector_MonoZLL_NLO_Mphi-500_Mchi-1_gSM-0p25_gDM-1p0_13TeV-madgraph_tarball.tar.xz']

gDM_1p0=True
if(gDM_1p0):
	m5000522 = ['1','1','1','1','1','1'] #Mass of stable dark matter==1
else:
	m5000522 = ['0.1','0.1','0.1','0.1','0.1'] #Mass of stable dark matter==0.1

pre_ext=['Mphi-500_Mchi2-150_Mchi1-1_gSM-0p25','Mphi-500_Mchi2-1_Mchi1-1_gSM-0p25']
ctau = ['0.1', '1', '10', '100', '1000'] #decay lengths (cm)


filename1 = ['_gDM-1p0_ctau-0p1.py','_gDM-1p0_ctau-1p0.py','_gDM-1p0_ctau-10p0.py','_gDM-1p0_ctau-100p0.py','_gDM-1p0_ctau-1000p0.py']

filename2 = ['_gDM-0p1_ctau-0p1.py','_gDM-0p1_ctau-1p0.py','_gDM-0p1_ctau-10p0.py','_gDM-0p1_ctau-100p0.py', '_gDM-1p0_ctau-1000p0.py']

count1=0

for directory in dirs:
	print "creating directory:", directory
	os.makedirs(directory)
	count2=0
        for ctaus in ctau:
		FilePrep="""
import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('%s'),
    nEvents = cms.untracked.uint32(5000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

# Link to cards:
# https://github.com/AndreasAlbert/genproductions/tree/monoz_LO_forDMLL/bin/MadGraph5_aMCatNLO/cards/production/13TeV/MonoZ

import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.Pythia8aMCatNLOSettings_cfi import *


generator = cms.EDFilter("Pythia8HadronizerFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring(
            'ParticleDecays:tau0Max = 1000.1',
            'LesHouches:setLifetime = 2',
            'SLHA:useDecayTable = off', # use pythia8 decay mode instead of decays defined in LH accord
            '5000522:new',
            '5000522:m0 = %s',
            '5000522:isResonance = false',
            '5000522:onMode = off',
            '5000522:mayDecay = off',
            '52:mayDecay = on',
            '52:mWidth = 0.01',  # needs to be non-zero for Pythia to decay it
            '52:onMode = off',
            '52:addChannel = 1 1 100 5000522 1 -1',
            '52:onIfAny = 5000522 1 -1',
            '52:tau0 = %s'
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'processParameters',
                                    )
        )
    )

"""%(Tarballs[count1],m5000522[count1],ctaus)
		print "creating Fragments for this directory"
                if(gDM_1p0):
			f=open(directory + '/' + pre_ext[count1] + filename1[count2],"w+")
                else:
			f=open(directory + '/' + pre_ext[count1] + filename2[count2],"w+")

		f.write(FilePrep)
		f.close()
		count2=count2+1
	count1=count1+1
	
