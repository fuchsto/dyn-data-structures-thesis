import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10,4))
plt.subplot(121)
plt.plot([1, 2, 4, 8, 16], 
         [0.03, 0.01, 0.01, 0.01, 0.01], 'k-', label='1M Vertices')
		 
plt.plot([1, 2, 4, 8, 16], 
         [0.28, 0.15, 0.08, 0.05, 0.04], 'k--', label='10M Vertices')
		 
plt.legend(loc='upper right')
plt.axis([1, 16, 0, 0.32])
plt.xticks( 2**np.arange(5) )
plt.grid(True)
plt.xlabel('number of nodes')
plt.ylabel('time (s)')

plt.subplot(122)
plt.plot([1, 2, 4, 8, 16], 
         [0.05, 0.04, 0.02, 0.01, 0.01], 'k-', label='1M Edges')
		 
plt.plot([1, 2, 4, 8, 16], 
         [0.52, 0.26, 0.13, 0.08, 0.04], 'k--', label='10M Edges')
		 
plt.legend(loc='upper right')
plt.axis([1, 16, 0, 0.56])
plt.xticks( 2**np.arange(5) )
plt.grid(True)
plt.xlabel('number of nodes')
plt.tight_layout()

plt.show()