# @Time    : 2/24/22 3:08 PM
# @Author  : Ruizhi Cheng
# @FileName: wireshark_plot.py
# @Email   : rcheng4@gmu.edu

#This function is used to plot the wireshark I/O graphs.
#Sometimes you may feel that Wireshark's drawing lines are too thin and the labels are not clear.
#You can click "Save As" when draw the figure on Wireshark, then save it as a csv file.
# Then use this program to draw the data in the csv file

from plot_paper import plot_trace
import numpy as np
import pandas as pd
import os

#file path, change it based on your file path
PLATFORM = '../../worlds'
TYPE='dis'
DATE='0406_dis'
#CONDITION = 'B_U_6'
FILENAME = 'dis/dis_uplink_tcp_process.csv'
#FILENAME2 = 'udp_process.csv'
file = os.path.join(PLATFORM,FILENAME)
#file2 = os.path.join(PLATFORM,TYPE,DATE,FILENAME2)
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
uplink_1 =  get_col(file,1)/1000000
#uplink_server_2= get_col(file,2)/1000000
downlink_1 = get_col(file,2)/1000000
TCP_uplink =  get_col(file,3)/1000000

#normal_UDP_downlink =get_col(file2,2)/1000000
#downlink_server_2 = get_col(file,4)/1000000

# uplink_2 =  get_col(file2,1)/1000000
# downlink_2 =  get_col(file2,2)/1000000
# downlink_udp_bitrate[270:720] = downlink_udp_bitrate[270:720]/1.1
# downlink_tcp_bitrate[270:720] = downlink_tcp_bitrate[270:720]/1.1
# uplink = uplink_server_1+uplink_server_2
# downlink =downlink_server_1+downlink_server_2
#trace = [[uplink_1,'U1 Uplink'],[downlink_1,'U2 Downlink']]
trace = [[uplink_1,'UDP Uplink'],[downlink_1,' UDP Downlink'],[TCP_uplink,'TCP Uplink']]
#plot_trace(trace,'Time (s)','Throughput (Kbps)')
plot_trace(trace,'Time (s)','Throughput (Mbps)')