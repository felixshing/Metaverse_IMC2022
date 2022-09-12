# @Time    : 5/1/22 11:17 PM
# @Author  : Ruizhi Cheng
# @FileName: resource_plot.py
# @Email   : rcheng4@gmu.edu

import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# import os

# ylabel = 'CPU Utilization (%)'
# #ylabel = 'GPU Utilization (%)'
# #ylabel = 'Average FPS'
import numpy as np

xlabel = 'Number of Users'
fig, ax1 = plt.subplots()
#ax1.set_xlabel(xlabel, fontsize=90)
#ax1.set_ylabel(ylabel, fontsize=90)
# ax1.spines['top'].set_visible(False)
# ax1.spines['right'].set_visible(False)
# ax1.tick_params(axis='x', labelsize=80)
# ax1.tick_params(axis='y', labelsize=80)
x_ticks = [1,2,3,4,5,7,10,12,15]
# #y_ticks = [40,60,80,100]

#ax1.set_yticks(y_ticks)



####### CPU Utilization
# ylabel = 'CPU Utilization (%)'
# ax1.set_yticks([40,50,60,70,80,90,100])
# ax1.set_ylim([40,120])
# Worlds_CPU = [68,71,72,73,74,78,82,84,87]
# Worlds_low = [66,70,71,72,72,77,81,82,85]
# Worlds_high = [69,72,73,74,75,79,84,86,90]
#
# VRChat_CPU = [64,65,66,68,71,75,78,82,84]
# VRChat_low= [62,64,65,66,70,73,77,81,82]
# VRChat_high = [65,66,67,70,72,77,79,83,86]
#
# AltspaceVR_CPU = [47,47,48,49,50,54,59,62,63]
# AltspaceVR_low = [45,46,47,48,49,52,58,61,61]
# AltspaceVR_high = [48,49,49,51,51,55,60,64,65]
#
#
# RecRoom_CPU = [66,67,68,69,71,74,77,81,83]
# RecRoom_low = [65,65,67,68,70,72,76,80,81]
# RecRoom_high = [67,69,69,70,72,77,78,83,84]
#
# Hubs_CPU = [74,75,76,78,80,85,91,93,96]
# Hubs_low = [74,74,75,76,77,82,89,90,93]
# Hubs_high = [74,76,77,80,83,87,93,97,100]
#
# ax1.plot(x_ticks, Hubs_CPU, label='Hubs',marker='D',markersize=25, linewidth=8,color='red')
# ax1.plot(x_ticks, VRChat_CPU, label='VRChat', marker="o",markersize=25,linewidth=8,color='orange')
# ax1.plot(x_ticks, Worlds_CPU,label='Worlds',marker='^',markersize=25,linewidth = 8,color='blue')
# ax1.plot(x_ticks, AltspaceVR_CPU, label='AltsVR', marker="s",markersize=25,linewidth=8,color='green')
# ax1.plot(x_ticks, RecRoom_CPU, label='Rec Room', marker='X',markersize=25,linewidth=8,color='purple')



####### GPU Utilization
# ylabel = 'GPU Utilization (%)'
# ax1.set_yticks([40,50,60,70,80,90,100])
# ax1.set_ylim([40,120])
# Worlds_GPU = [65,66,67,68,68,72,75,77,80]
# Worlds_low = [63,65,65,66,67,71,73,75,76]
# Worlds_high = [66,67,69,70,70,74,76,79,83]
#
# VRChat_GPU = [57,57,58,58,60,63,64,66,70]
# VRChat_low = [57,57,57,57,58,62,62,63,68]
# VRChat_high = [57,57,59,59,61,65,67,68,73]
#
# AltspaceVR_GPU = [56,59,64,66,67,72,74,77,82]
# AltspaceVR_low = [53,55,63,65,64,68,70,73,77]
# AltspaceVR_high = [60,63,66,67,70,74,78,80,86]
#
# RecRoom_GPU = [58,58,58,59,59,61,63,65,68]
# RecRoom_low= [58,58,58,58,58,60,62,63,66]
# RecRoom_high = [58,58,58,60,60,62,64,67,70]
#
# Hubs_GPU = [53,54,55,56,56,60,64,65,69]
# Hubs_low = [53,54,53,53,55,59,62,63,67]
# Hubs_high = [53,54,56,56,58,62,67,67,71]
#
# ax1.plot(x_ticks, Worlds_GPU,label='Worlds',marker='^',markersize=25,linewidth = 8,color='blue')
# ax1.plot(x_ticks, Hubs_GPU, label='Hubs',marker='D',markersize=25, linewidth=8,color='red')
# ax1.plot(x_ticks, AltspaceVR_GPU, label='AltsVR', marker="s",markersize=25,linewidth=8,color='green')
# ax1.plot(x_ticks, RecRoom_GPU, label='Rec Room', marker='X',markersize=25,linewidth=8,color='purple')
# ax1.plot(x_ticks, VRChat_GPU, label='VRChat', marker="o",markersize=25,linewidth=8,color='orange')




###### Bitrate
# ylabel = 'Throughput (Mbps)'
# ax1.set_yticks([0,0.5,1,2,3,4])
# ax1.set_ylim([0,5.7])
# Worlds_bitrate = [0.12,0.43,0.74,1.01,1.34,2.01,3.14,3.83,4.58]
# Worlds_low = [0.1,0.33,0.64,0.94,1.14,1.81,3.04,3.68,4.38]
# Worlds_high = [0.14,0.53,0.84,1.11,1.54,2.25,3.25,3.99,4.78]
#
# VRChat_bitrate = [0.004,0.031,0.052,0.078,0.103,0.167,0.231,0.283,0.367]
# VRChat_low = [0.004,0.028,0.045,0.065,0.093,0.157,0.211,0.263,0.347]
# VRChat_high = [0.004,0.034,0.057,0.084,0.123,0.177,0.241,0.293,0.397]
#
# AltspaceVR_bitrate = [0.013,0.022,0.034,0.046,0.058,0.069,0.089,0.116,0.148]
# AltspaceVR_low = [0.011,0.02,0.031,0.042,0.053,0.051,0.078,0.105,0.131]
# AltspaceVR_high = [0.014,0.025,0.038,0.048,0.059,0.083,0.108,0.138,0.16]
#
# RecRoom_bitrate = [0.004,0.041,0.072,0.103,0.1452,0.232,0.356,0.431,0.535]
# RecRoom_low = [0.004,0.038,0.068,0.093,0.1352,0.202,0.326,0.401,0.505]
# RecRoom_high = [0.004,0.044,0.074,0.123,0.1552,0.262,0.376,0.451,0.575]
#
# Hubs_bitrate = [0,0.081,0.163,0.245,0.324,0.491,0.821,0.971,1.321]
# Hubs_low = [0,0.076,0.143,0.225,0.304,0.411,0.771,0.871,1.221]
# Hubs_high = [0,0.091,0.173,0.265,0.344,0.551,0.881,1.071,1.421]
# ax1.plot(x_ticks, Worlds_bitrate,label='Worlds',marker='^',markersize=25,linewidth = 8,color = 'blue')
# ax1.plot(x_ticks, VRChat_bitrate, label='VRChat', marker="o",markersize=25,linewidth=8,color = 'orange')
# ax1.plot(x_ticks, Hubs_bitrate, label='Hubs',marker='D',markersize=25, linewidth=8,color='red')
# ax1.plot(x_ticks, AltspaceVR_bitrate, label='AltsVR', marker="s",markersize=25,linewidth=8,color='green')
# ax1.plot(x_ticks, RecRoom_bitrate, label='Rec Room', marker='X',markersize=25,linewidth=8,color='purple')

# ylabel = 'FPS'
# ax1.set_yticks([30,40,50,60,72])
# ax1.set_ylim([30,85])
# Worlds_FPS = [72,72,72,71,71,68,64,62,54]
# Worlds_low = [72,72,72,70,69,64,61,57,52]
# Worlds_high = [72,72,72,72,72,72,68,65,55]
#
#
# VRChat_FPS = [72,71,70,68,66,60,50,46,41]
# VRChat_low = [72,70,69,67,63,58,48,43,38]
# VRChat_high = [72,72,72,72,70,64,54,49,43]
#
#
# AltspaceVR_FPS = [72,72,71,71,71,65,63,58,53]
# AltspaceVR_low = [72,72,70,69,69,62,60,56,50]
# AltspaceVR_high = [72,72,72,72,72,67,65,59,55]
#
# RecRoom_FPS = [72,70,68,68,65,58,53,47,43]
# RecRoom_low = [72,69,67,66,63,55,50,44,40]
# RecRoom_high = [72,72,71,70,67,60,55,49,45]
#
# Hubs_FPS = [72,68,65,62,60,53,46,40,33]
# Hubs_low = [72,66,63,60,57,50,44,38,31]
# Hubs_high = [72,71,67,65,60,55,48,42,36]
# ax1.plot(x_ticks, Worlds_FPS,label='Worlds',marker='^',markersize=25,linewidth = 8,color = 'blue')
# ax1.plot(x_ticks, VRChat_FPS, label='VRChat', marker="o",markersize=25,linewidth=8,color = 'orange')
# ax1.plot(x_ticks, AltspaceVR_FPS, label='AltsVR', marker="s",markersize=25,linewidth=8,color='green')
# ax1.plot(x_ticks, Hubs_FPS, label='Hubs',marker='D',markersize=25, linewidth=8,color='red')
# ax1.plot(x_ticks, RecRoom_FPS, label='Rec Room', marker='X',markersize=25,linewidth=8,color='purple')


ylabel = 'Used Memory (GB)'
ax1.set_yticks([1.0,1.3,1.5,1.7,2.0])
#ax1.set_xlim([0,15])
ax1.set_ylim([1,2.3])
Worlds_Memory = [1807,1825,1849,1857,1879,1893,1911,1933,1956]
Worlds_low=[1793,1805,1823,1839,1853,1863,1888,1903,1936]
Worlds_high=[1835,1854,1864,1878,1899,1923,1946,1965,1978]

Worlds_Memory=np.divide(Worlds_Memory,1000)
Worlds_low=np.divide(Worlds_low,1000)
Worlds_high=np.divide(Worlds_high,1000)


VRChat_Memory = [1713,1733,1742,1752,1769,1787,1803,1824,1841]
VRChat_low = [1700,1713,1722,1731,1759,1767,1777,1800,1811]
VRChat_high = [1732,1744,1755,1764,1787,1799,1833,1844,1871]
VRChat_Memory=np.divide(VRChat_Memory,1000)
VRChat_low=np.divide(VRChat_low,1000)
VRChat_high=np.divide(VRChat_high,1000)


AltspaceVR_Memory = [1603,1624,1633,1647,1654,1677,1703,1737,1751]
AltspaceVR_low = [1589,1604,1623,1637,1644,1657,1680,1707,1741]
AltspaceVR_high = [1633,1644,1653,1667,1684,1697,1723,1757,1781]
AltspaceVR_Memory=np.divide(AltspaceVR_Memory,1000)
AltspaceVR_low=np.divide(AltspaceVR_low,1000)
AltspaceVR_high=np.divide(AltspaceVR_high,1000)


RecRoom_Memory= [1514,1530,1544,1552,1561,1588,1621,1642,1674]
RecRoom_low= [1500,1510,1524,1532,1541,1558,1600,1622,1644]
RecRoom_high= [1534,1560,1564,1572,1591,1618,1631,1652,1694]
RecRoom_Memory=np.divide(RecRoom_Memory,1000)
RecRoom_low=np.divide(RecRoom_low,1000)
RecRoom_high=np.divide(RecRoom_high,1000)



Hubs_Memory = [1402,1415,1425,1435,1445,1467,1477,1497,1521]
Hubs_low = [1388,1397,1405,1415,1425,1447,1451,1467,1502]
Hubs_high = [1414,1431,1445,1455,1475,1487,1497,1533,1541]
Hubs_Memory=np.divide(Hubs_Memory,1000)
Hubs_low=np.divide(Hubs_low,1000)
Hubs_high=np.divide(Hubs_high,1000)


ax1.plot(x_ticks, Worlds_Memory,label='Worlds',marker='^',markersize=25,linewidth = 8,color = 'blue')
ax1.plot(x_ticks, RecRoom_Memory, label='Rec Room', marker='X',markersize=25,linewidth=8,color='purple')
ax1.plot(x_ticks, VRChat_Memory, label='VRChat', marker="o",markersize=25,linewidth=8,color = 'orange')
ax1.plot(x_ticks, Hubs_Memory, label='Hubs',marker='D',markersize=25, linewidth=8,color='red')
ax1.plot(x_ticks, AltspaceVR_Memory, label='AltsVR', marker="s",markersize=25,linewidth=8,color='green')

# ylabel = 'Latency (ms)'
# x_ticks = [2,3,4,5,6,7]
# ax1.set_yticks([100,150,200,250,300])
# ax1.set_ylim([80,360])
# Worlds_L = [128,137,147,158,170,183]
# Worlds_low = [116,130,140,152,163,177]
# Worlds_high = [139,144,154,164,177,189]
#
# VRChat_L = [104,110,117,127,138,149]
# VRChat_low = [98,100,112,119,133,145]
# VRChat_high = [112,120,122,134,143,153]
# #
# #
# AltspaceVR_L = [209,218,226,234,245,256]
# AltspaceVR_low = [198,208,218,227,240,249]
# AltspaceVR_high = [220,230,234,242,249,263]
#
# RecRoom_L = [101,107,114,122,130,140]
# RecRoom_low = [94,102,110,117,124,136]
# RecRoom_high = [105,113,118,127,136,144]
#
#
# Hubs_L = [239,246,255,266,279,295]
# Hubs_low = [232,240,250,261,272,291]
# Hubs_high = [246,251,260,271,286,299]
# ax1.plot(x_ticks, Hubs_L, label='Hubs',marker='D',markersize=25, linewidth=8,color='red')
# ax1.plot(x_ticks, VRChat_L, label='VRChat', marker="o",markersize=25,linewidth=8,color = 'orange')
# ax1.plot(x_ticks, AltspaceVR_L, label='AltsVR', marker="s",markersize=25,linewidth=8,color='green')
# ax1.plot(x_ticks, RecRoom_L, label='Rec Room', marker='X',markersize=25,linewidth=8,color='purple')
# ax1.plot(x_ticks, Worlds_L,label='Worlds',marker='^',markersize=25,linewidth = 8,color = 'blue')
####### battery
# ax1.set_yticks([0,20,40,60,80,100])
# ax1.set_ylim([0,110])
# Worlds_battery = [12,34,60,70,80,90,91]
# VRChat_battery = [34,45,6,7,92,91]
# AltspaceVR_battery = [98,98,97,96,94,91,90]
# RecRoom_battery = [54,35,60,71,80,90,100]
# Hubs_battery = [64,74,60,75,84,91,100]
# ax1.plot(x_ticks, Worlds_battery,label='Worlds',linewidth = 8)
# ax1.plot(x_ticks, VRChat_battery, label='VRChat', linewidth=8)
# ax1.plot(x_ticks, AltspaceVR_battery, label='AltspaceVR', linewidth=8)
# ax1.plot(x_ticks, RecRoom_battery, label='Rec Room', linewidth=8)
# ax1.plot(x_ticks, Hubs_battery, label='Hubs', linewidth=8)
# plt.grid()
# plt.legend(fontsize=75, loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=2)
# plt.show()

#ylabel = 'CPU Utilization (%)'
# ylabel = 'GPU Utilization (%)'
#ylabel = 'Average FPS'
#xlabel = 'Number of Users'
# fig, ax1 = plt.subplots()

ax1.set_xticks(x_ticks)
ax1.fill_between(x_ticks,Worlds_low,Worlds_high,facecolor='blue',alpha=0.2)
ax1.fill_between(x_ticks,VRChat_low,VRChat_high,facecolor='orange',alpha=0.2)
ax1.fill_between(x_ticks,AltspaceVR_low,AltspaceVR_high,facecolor='green',alpha=0.2)
ax1.fill_between(x_ticks,RecRoom_low,RecRoom_high,facecolor='purple',alpha=0.2)
ax1.fill_between(x_ticks,Hubs_low,Hubs_high,facecolor='red',alpha=0.2)
ax1.set_xlabel(xlabel, fontsize=90)
ax1.set_ylabel(ylabel, fontsize=90)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.tick_params(axis='x', labelsize=80)
ax1.tick_params(axis='y', labelsize=80)
plt.legend(fontsize=70, loc='upper center', bbox_to_anchor=(0.51, 1.2), ncol=3,columnspacing=0.4 )



#x_ticks = [1,2,3,4,5,10,15]
#y_ticks = [40,60,80,100]
#ax1.set_xticks(x_ticks)
#ax1.set_yticks(y_ticks)
plt.grid()
plt.show()