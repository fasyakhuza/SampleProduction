
import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.4.3/DMVector_ZLL_NLO/v1/Vector_MonoZLL_NLO_Mphi-500_Mchi-150_gSM-0p25_gDM-1p0_13TeV-madgraph_tarball.tar.xz'),
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
            '5000522:m0 = 1',
            '5000522:isResonance = false',
            '5000522:onMode = off',
            '5000522:mayDecay = off',
            '52:mayDecay = on',
            '52:mWidth = 0.01',  # needs to be non-zero for Pythia to decay it
            '52:onMode = off',
            '52:addChannel = 1 1 100 5000522 1 -1',
            '52:onIfAny = 5000522 1 -1',
            '52:tau0 = 1'
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'processParameters',
                                    )
        )
    )

