import dpdata
import numpy as np

sys = dpdata.LabeledSystem('./OUTCAR.relax', fmt = 'vasp/outcar')

#sys.sub_system([0,1,2]).to_deepmd_npy('system',prec=np.float32)
sys.to_deepmd_npy('system',set_size=5,prec=np.float32)
