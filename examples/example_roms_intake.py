#!/usr/bin/env python
"""
ROMS 
Intake reader
==================================
"""
import numpy as np
from opendrift.readers import reader_ROMS_intake
from opendrift.models.oceandrift import OceanDrift
import intake
import xarray as xr

intake_catalog = 'https://mghp.osn.xsede.org/rsignellbucket1/rsignell/testing/cnaps.yml'
dataset = 'CNAPS_opendrift' 

o = OceanDrift(loglevel=20)  # Set loglevel to 0 for debug information

cnaps = reader_ROMS_intake.Reader(intake_catalog=intake_catalog, dataset=dataset)
o.add_reader(cnaps)


# Seed elements at defined positions, depth and time
o.seed_elements(lon=-75.5, lat=34.77, radius=0, number=10,
                z=np.linspace(0, -150, 10), time=cnaps.start_time)


# Running model
o.run(time_step=3600)


# Print and plot results, with lines colored by particle depth
print(o)
o.plot(linecolor='z', fast=True)
o.animation()

