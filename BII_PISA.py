# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 20:25:24 2018

@author: Hal14
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sp

plt.Figure(figsize=(11,8.5))

BII_PISA_df = pd.read_csv('BII_PISA.csv')
print(BII_PISA_df)

plt.scatter(x=BII_PISA_df['Rank BII'], y=BII_PISA_df['Rank PISA'])

fit=np.polyfit(x=BII_PISA_df['Rank BII'], y=BII_PISA_df['Rank PISA'], deg=1)
print(fit)
p=np.poly1d(fit)
xp=np.linspace(1, BII_PISA_df['Rank BII'].max(), BII_PISA_df['Rank BII'].max())
print(xp)
plt.plot(xp, p(xp))

print(sp.linregress(BII_PISA_df['Rank BII'], BII_PISA_df['Rank PISA'])) 

plt.title('Bloomberg Innovation Index Rank vs PISA Rank')
plt.savefig('BII_PISA_Plot.png')







