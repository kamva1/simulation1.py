import Pyxis
#from pyrap.tables import table
import mqt,lsm
import os
import sys
import scipy.special
import numpy as np

def sim():


  # defined your parameters here
   ms_set = "MeerKATnew.MS_p0"
   sr_pos = np.arange(10,180,10) # in arcmin
   options = {}

       #options['gridded_sky.source_flux'] = 1. # bringtness
       # options['gridded_sky.grid_m0'] = 0
      # options['gridded_sky.grid_l0'] = sr_pos
   options["tiggerlsm.filename"] = "phase-center-source.lsm.html"
   options['ms_sel.msname']=ms_set;
   options['ms_sel.output_column'] = 'DATA'
   mqt.run("turbo-sim.py",job="_tdl_job_1_simulate_MS",
          config="tdlconf.profiles",section="turbo-sim:from-skymodel",
                options=options);        
   
   os.system("wsclean -size 2048  2048  -scale 2.asec -weight natural -niter 1000 -name 0project_images -datacolumn DATA -make-psf %s"%ms_set)



if __name__ == '__main__':
    sim()
    
