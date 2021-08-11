import pandas as pd
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import scipy.integrate as it
from statsmodels.nonparametric.smoothers_lowess import lowess

data = sys.argv[1]
df = pd.read_csv(data, sep=';', header=0)
df['velocity_x']=0
df['velocity_y']=0
df=df.shift(periods=1, axis=0, fill_value=0).reset_index()

'''
SOS Butterworth FIlter
sos_x = signal.butter(5, [0.1, 0.8], btype='band', output='sos')
df['filtered_x'] = signal.sosfilt(sos_x, df['x'])
smoothed= lowess(df['x'], df.index, frac=0.008) #smooth 0.008
df['filtered_x']=smoothed[:, 1]

sos_y = signal.butter(5, [0.05, 0.4], btype='band', output='sos')
df['filtered_y'] = signal.sosfilt(sos_y, df['y'])
smoothed_y= lowess(df['y'], df.index, frac=0.006) #smooth 0.008
df['filtered_y'] =smoothed_y[:, 1]
'''

#Butterworth Filer
b_x, a_x = signal.butter(3, 0.192, btype='lowpass', analog=False)  #0.2
low_passed_x = signal.filtfilt(b_x, a_x, df['x'])
df['filtered_x']=low_passed_x 

b_y, a_y = signal.butter(3, 0.192, btype='lowpass', analog=False)  #0.19
low_passed_y = signal.filtfilt(b_y, a_y, df['y'])
df['filtered_y']=low_passed_y 


'''
#LOWESS Filter
smoothed = lowess(df['x'], df.index, frac=0.008) #smooth 0.008
df['filtered_x']=smoothed[:, 1]

smoothed_y= lowess(df['y'], df.index, frac=0.006) #smooth 0.008
df['filtered_y'] =smoothed_y[:, 1]
'''


