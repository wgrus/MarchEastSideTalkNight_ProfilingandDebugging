from scipy import sparse as sp
import numpy as np
from pandas import DataFrame

import pdb

r = np.random.random_sample(size=(500,15))

#pdb.set_trace()

r = r * (r < 0.2).astype(int)
r = sp.csr_matrix(r)

df = DataFrame(np.random.random_sample(size=(500,2)),
               columns=['A','B'])
#df['C'] = r
df['C'] = [r[i] for i in range(r.shape[0])]
thing1 = sp.csr_matrix(df.A.values)
thing2 = sp.vstack(df.C.values)

output = sp.hstack([thing1, thing2])
