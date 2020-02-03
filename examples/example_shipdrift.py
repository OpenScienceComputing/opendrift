#!/usr/bin/env python
"""
Ship drift
==================================
"""

from datetime import datetime
from opendrift.models.shipdrift import ShipDrift

o = ShipDrift(loglevel=20)

o.add_readers_from_list([
    'http://thredds.met.no/thredds/dodsC/sea/nordic4km/zdepths1h/aggregate_be',
    'http://thredds.met.no/thredds/dodsC/meps25files/meps_det_extracted_2_5km_latest.nc',
    'http://thredds.met.no/thredds/dodsC/sea/mywavewam4/mywavewam4_be'
    ])

#%%
# Seed ship elements at defined position and time
o.seed_elements(lon=5.0, lat=63.0, radius=1000, number=1000,
                time=datetime.now(),
                length=80.0, beam=10.0, height=9.0, draft=4.0)

print(o.elements_scheduled)

#%%
# Running model
o.run(steps=24, stop_on_error=True)

#%%
# Print and plot results
print(o)
o.plot(linecolor='orientation')
#o.animation()