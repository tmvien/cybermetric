#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 23:36:59 2019

@author: Mavis
"""

import pandas as pd

xls = pd.ExcelFile('STAT.xlsx')

novak = pd.read_excel(xls, 'DJOKOVIC')

def get_w_l(df):
    SINGLES_W = []
    SINGLES_L = []
    for i in df['SINGLES W-L']:
        SINGLES_W.append(int(i.split("-")[0]))
        SINGLES_L.append(int(i.split("-")[1]))
    return SINGLES_W, SINGLES_L

novak = novak.iloc[:-1,]
novak['SINGLES_W'], novak['SINGLES_L'] = get_w_l(novak)
novak.drop(['SINGLES W-L'], axis = 1, inplace=True)

novak.set_index('YEAR', inplace = True)
novak.index = pd.to_datetime(novak.index, format = "%Y")
novak.index = novak.index.year

#novak = pd.to_numeric(novak, errors = "coerce")
novak = novak.astype('int')

novak = novak[::-1]

import matplotlib.pyplot as plt
from matplotlib import style
#import seaborn as sns
#sns.set(style = 'darkgrid')
style.use('fivethirtyeight')

fig, ax1 = plt.subplots(figsize = (10, 8))
#y = [3, 6, 5.5, 9, 12, 12, 12, 14, 16.5, 14, 2, 16, 11]

color = 'tab:red'
ax1.set_xlabel('Year')
ax1.set_ylabel('PRIZE MONEY (in 10,000,000s)', color=color)
ax1.bar(novak.index, novak['PRIZE MONEY'], color=color)
ax1.set_yticks([3000000, 6000000, 9000000, 12000000, 15000000])

rects = ax1.patches

# Make some labels.
labels = ["~3M", "~6M", "~5.5M", "~4M", "~12M", "~12.1M", "~12M", "~14M", "~16.5M", "~14M",
          "~2M", "~16M", "~11M"]

for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
            ha='center', va='bottom')
    
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('SINGLES TITLES', color=color)  # we already handled the x-label with ax1
ax2.plot(novak.index, novak['SINGLES TITLES'], color=color)
#ax2.grid(False)

#ax2.tick_params(axis='y', labelcolor=color)
plt.title("Prize Money and Singles Titles of Novak Djokovic from 2007-2019", loc = "right")
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()