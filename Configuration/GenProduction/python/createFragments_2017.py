#!/usr/bin/env python
import os
import sys
import random
import argparse
import json
import shutil
import subprocess

def create_config(input_jsonfile):
	with open(input_jsonfile) as data_file:
		data = json.load(data_file)
		for sample, sample_cfg in data.items():
			directory = sample_cfg["dir"]
			print "creating directory:", directory
			os.makedirs(directory)
			count2=0
			tarball = sample_cfg["tarball"]
			m5000522 = sample_cfg["m5000522"]
			pre_ext = sample_cfg["pre_ext"]
			filename = sample_cfg["filename"]
			ctau = sample_cfg["ctau"]
			for i in range(len(ctau)):
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
            '18:mayDecay = on',
            '18:mWidth = 0.01',  # needs to be non-zero for Pythia to decay it
            '18:onMode = off',
            '18:addChannel = 1 1 100 5000522 1 -1',
            '18:onIfAny = 5000522 1 -1',
            '18:tau0 = %s'
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'processParameters',
                                    )
        )
    )

"""%(tarball,m5000522,ctau[i])
				print "creating Fragments for this directory"
				#f=open(directory + '/' + pre_ext[i] + filename[i],"w+")
				f=open(os.path.join(directory, pre_ext + filename[i]), 'w+')
				f.write(FilePrep)
				f.close()
	


def main():
        from argparse import ArgumentParser
        import argparse
        parser = ArgumentParser(description="Do -h to see usage")

        #parser.add_argument('-i', '--txt', action='store_true', help='input txt file name')
        #parser.add_argument('-f', '--txt',help='txt file input',type=argparse.FileType('r'),)
        #parser.add_argument('--f', type=open)

        parser.add_argument('-i', '--json', type=str)

        args = parser.parse_args()

        print(args)

        create_config(args.json)


if __name__ == "__main__":
        main()
