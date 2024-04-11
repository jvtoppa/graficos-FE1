import matplotlib.pyplot as plt
import numpy as np

massa1 = [7562.874,7138.422,6581.94,6306.144,5826.924,5554.062,5280.222,4774.596,4389.264,3880.704,3383.88,3096.348,2600.502,2305.146,2018.592,1474.824,1204.896,784.356,299.268]

deltax1 = [5.6,5.3,5.1,5.0,4.5,4.1,3.6,3.3,3.1,2.6,2.2,1.9,1.5,1.4,1.1,0.9,0.7,0.4,0.2] 

incerteza = 0.02886751346
plt.figure(figsize=(8,6))
plt.errorbar(deltax1, massa1, xerr=incerteza, ecolor='red', elinewidth=1, capsize=5, capthick=1,
             color='k', linestyle="none",)
plt.scatter(deltax1, massa1)
plt.grid()
plt.show()

