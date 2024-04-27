import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import scipy.optimize as opt
from scipy.interpolate import interp1d
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import math
#get_ipython().run_line_magic('matplotlib', 'inline')


#GENERATE RANDOM TEST DATA
#TIME VALUES FROM 0 TO 5 WITH STEP SIZE 0.01
np.random.seed(73) #change or delete for true randomness, this keeps it at the same values

time = np.arange(0, 5, 0.01)
time = list(time)

frequency = 2
amplitude = 5
phi = np.pi/2
nselvl = 0.1


#acceleration data using shm eq a(t) -w^2 * cos(wt + phi)

w = 2*np.pi*frequency
displac = amplitude*np.pi*frequency

def accel (t) :
    return -amplitude * w**2 * math.cos(w * t)

accel_points = [accel(t) for t in time]


#accel = -w**2 *displac


#accel.extend(np.random.normal(size=len(time))) #adding noise for some randomness
noise_t = np.random.uniform(0,5,math.floor(nselvl*len(time)))
noise_a = np.random.uniform(-800,800,math.floor(nselvl*len(time)))

#add points togeather
total_times = time.copy()
total_times.extend(noise_t)
total_accel = accel_points.copy()
total_accel.extend(noise_a)

'''
plt.scatter(total_times,total_accel)
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (ms^-2)')
plt.title('Acceleration vs Time')
plt.savefig('bhoomiData.png')

plt.clf()
#'''

#fitting to simple harmonic model

# Simple harmonic motion using acceleration
def simple_a(t, a=amplitude, ang=w, b=displac, phase=phi):                  # inputs: t:time, A:amplitude, B:offset, w:angular frequency, phi:phase
    return b - a * (ang**2) * np.cos(ang*t + phase)   # output: acceleration

simp_a = [simple_a(t) for t in time]

sorted_times = time.copy()
sorted_simpa = simp_a.copy()
sorted_accel = accel_points.copy()
for i in range(len(noise_t)) :
    x = noise_t[i]
    y = noise_a[i]
    i2 = 0
    while i2<len(sorted_times) :
        if x < sorted_times[i2] :
            sorted_times.insert(i2, x)
            sorted_simpa.insert(i2, y)
            sorted_accel.insert(i2, y)
            break
        i2 += 1

# Graph
'''
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (ms^-2)')
plt.title('Acceleration vs Time')
plt.plot(sorted_times, sorted_simpa, color='orange')

plt.scatter(sorted_times, sorted_simpa)

plt.savefig('bhoomiGraph.png')

plt.clf()
#'''


#check for duplicate data 
assert len(sorted_times) == len(set(sorted_times)), "there were duplicates"

#Filtering is moot

#'''
#interpolation
yinterp = interp1d(sorted_times, sorted_accel, kind="linear")
yvals = yinterp(sorted_times)

s_start_pars=[amplitude, displac, w, phi]

#parameter values and covariance
s_pars, s_cov = opt.curve_fit(simple_a, sorted_times, sorted_accel, p0=s_start_pars)

[sA, sB, sw, sphi] = s_pars

#predicted values for simple_a model and vdamped_a model
s_ypred = [simple_a(t, sA, sB, sw, sphi) for t in sorted_times]

#calculating residuals
s_yresidual = yvals - s_ypred
#'''

#graphing
fig1=plt.figure(figsize=(10, 10), dpi= 80, facecolor='w', edgecolor='k')
plt.rcParams.update({'font.size': '16'})
plt.title("Simple Harmonic Oscillator Model \n Acceleration vs. Time")
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s$^2$)")
plt.plot(sorted_times, sorted_simpa, color='orange', label="Simple Harmonic Oscillator Model")
plt.scatter(sorted_times, sorted_simpa, label="Data")
handles, labels = plt.gca().get_legend_handles_labels()
order = [1,0]
plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order])
plt.legend(loc='upper right')
plt.savefig("sho_fit.png")