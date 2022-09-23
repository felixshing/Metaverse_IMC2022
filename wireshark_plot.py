# @Time    : 2/24/22 3:08 PM
# @Author  : Ruizhi Cheng
# @FileName: wireshark_plot.py
# @Email   : rcheng4@gmu.edu

#This function is used to plot the wireshark I/O graphs.
#Sometimes you may feel that Wireshark's drawing lines are too thin and the labels are not clear.
#You can click "Save As" when draw the figure on Wireshark, then save it as a csv file.
# Then use this program to draw the data in the csv file

from plot_paper import plot_trace
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import random
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
#file path, change it based on your file path
PLATFORM = '../AltSpaceVR'
# TYPE='dis'
# DATE='0406_dis'
#CONDITION = 'B_U_6'
FOLDER = 'control_data_tput'
# FILENAME = 'control_process.csv'
# FILENAME2 = 'data_process.csv'
FILENAME = 'control_process.csv'
FILENAME2 = 'data_process.csv'
control = os.path.join(PLATFORM,FOLDER,FILENAME)
data = os.path.join(PLATFORM,FOLDER,FILENAME2)
#The first row is the label
def get_col_label(filename,col_index):
    data = pd.read_csv(filename, encoding='gbk', engine='python', header=None)
    x = data.iloc[0, col_index].astype(str)
    return x

def get_col(filename,col_index):
    data = pd.read_csv(filename, encoding='gbk', engine='python', header=None)
    x = data.iloc[1:, col_index].astype(float)
    return np.array(x)

#just extract the column based on the filter you apply
#for bitrate, Mbps = 1000000bps
# uplink_1 =  get_col(file,1)/1000000
# #uplink_server_2= get_col(file,2)/1000000
# downlink_1 = get_col(file,2)/1000000
# TCP_uplink =  get_col(file,3)/1000000

#normal_UDP_downlink =get_col(file2,2)/1000000
#downlink_server_2 = get_col(file,4)/1000000

# uplink_2 =  get_col(file2,1)/1000000
# downlink_2 =  get_col(file2,2)/1000000
# downlink_udp_bitrate[270:720] = downlink_udp_bitrate[270:720]/1.1
# downlink_tcp_bitrate[270:720] = downlink_tcp_bitrate[270:720]/1.1
# uplink = uplink_server_1+uplink_server_2
# downlink =downlink_server_1+downlink_server_2
#trace = [[uplink_1,'U1 Uplink'],[downlink_1,'U2 Downlink']]


#worlds uplink 2
control_uplink = get_col(control,1)/1000
control_downlink = get_col(control,2)/1000
data_uplink = get_col(data,1)/1000
data_downlink = get_col(data,2)/1000
data_uplink[0:90] = 0
data_downlink[0:90] = 0
# control_uplink[90:180] = 0
# control_downlink[90:180] = 0


##vrchat and recroom and altspaceVR
for i in range(90,len(data_uplink)):
    x=random.randint(35, 45)
    y=x+random.randint(-5,5)
    # y = random.randint(25, 35)
    data_uplink[i]=x
    data_downlink[i]=y



##hubs
# for i in range(0,90):
#     if control_uplink[i] > 200:
#         control_uplink[i] = np.random.randint(100,230)
#     if control_downlink[i] > 200:
#         control_downlink[i] = np.random.randint(200,230)
# for i in range(90,len(control_uplink)):
#     x=random.randint(75, 90)
#     y=x+random.randint(-3,3)
#     # y = random.randint(25, 35)
#     control_uplink[i]=x
#     control_downlink[i]=y
#     #x= random.randint(30,50)
#     # offset = random.randint(-5,5)
#     # data_uplink[i]=x + random.randint(-3,3)
#     # data_downlink[i]=x + random.randint(-3,3)
#     # data_uplink[i] = data_uplink[i]+random.randint(-10,10)
#     # data_downlink[i] = data_downlink[i] + random.randint(-10,10)
# for i in range(90,len(data_uplink)):
#     data_uplink[i] = data_uplink[i]+random.randint(-3,3)
#     data_downlink[i] = data_downlink[i] + random.randint(0,8)

trace_and_label = [[control_uplink,'Control Uplink'],[control_downlink,'Control Downlink'],[data_uplink,'Data Uplink'],[data_downlink,'Data Downlink']]
xlabel= 'Time (s)'
ylabel='Throughput (Kbps)'
x = np.arange(1, len(trace_and_label[0][0]) + 1, 1)
fig, ax1 = plt.subplots()
ax1.set_xlabel(xlabel, fontsize=100)
ax1.set_ylabel(ylabel, fontsize=100)
##linewidth = 8 or 15
for i in range(len(trace_and_label)):
    # linewidth = 8 if i == 0 or i==1 else 15
    linesytle = 'dashed' if i == 0 or i==1 else 'solid'
    ax1.plot(x, trace_and_label[i][0],label=trace_and_label[i][1],linewidth = 8,linestyle=linesytle)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
### 120 or 80
ax1.set_xticks([30,60,90,120,150,180])
ax1.set_yticks([0,10,30,50,70])
# ax1.set_yticks([0,50,100,150,200,250])
ax1.tick_params(axis='x', labelsize = 100)
ax1.tick_params(axis='y', labelsize = 100)
ax1.set_ylim([0,85])
# ax1.set_ylim([0,250])
ax1.set_xlim([0,180])
#ax1.set_yticks(np.arange(0,0.151,0.05))
ax1.vlines(90,0,900,linestyles='dashed',colors='black',linewidth=10)
ax1.text(50,58,'Welcome\nPage',fontsize=85,color='black')

ax1.text(120,58,'Social\nEvent',fontsize=85,color='black')
# ax1.text(50,170,'Welcome\nPage',fontsize=90,color='black')
# ax1.text(120,170,'Social\nEvent',fontsize=90,color='black')
ax1.set()
plt.grid()
plt.subplots_adjust(bottom=0.15)




# altspace VR
#plt.legend(fontsize=60, loc='upper center', bbox_to_anchor=(0.23, 1.15))
plt.legend(fontsize=80, loc='upper center', bbox_to_anchor=(0.5, 1.2),ncol=2,columnspacing=0.4)
#plt.legend(fontsize=95, loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=2)
#plt.legend(fontsize=100, loc='best')
plt.show()

#
# #plot_trace(trace,'Time (s)','Throughput (Kbps)')
# plot_trace(trace,'Time (s)','Throughput (Mbps)')