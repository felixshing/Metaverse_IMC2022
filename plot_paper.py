#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time     :2022/1/6 7:14 PM
# @Author   :Ruizhi Cheng

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
ROOT = '../..'
U1_FILENAME = 'recroom_sca_U1_exp1_process.csv'
# U2_FILENAME = 'U2.csv'

dash_line = {0:'-',1:'--',2:'-.'}
####create a figure
#[[trace,label],[trace,label],[trace,label]]
def plot_trace(trace_and_label,xlabel,ylabel):
    x = np.arange(1, len(trace_and_label[0][0]) + 1, 1)
    fig, ax1 = plt.subplots()
    ax1.set_xlabel(xlabel, fontsize=85)
    ax1.set_ylabel(ylabel, fontsize=85)
    ##linewidth = 8 or 15
    for i in range(len(trace_and_label)):
        ax1.plot(x, trace_and_label[i][0],label=trace_and_label[i][1],linewidth = 8)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ### 120 or 80
    ax1.tick_params(axis='x', labelsize = 85)
    ax1.tick_params(axis='y', labelsize = 85)
    #ax1.set_yticks(np.arange(0,0.151,0.05))



    ####### Worlds Tput
    # ax1.set_ylim([0, 950])
    # ax1.set_xlim([0.1, 130])
    # ax1.set_yticks([0,300,500,700])
    # ax1.set_xticks([60,120,180])
    # ax1.text(63, 80, 'Worlds', fontsize=120, color='red')

    #####recroom tput
    # ax1.set_ylim([0, 75])
    # ax1.set_xlim([0.1, 130])
    # ax1.set_yticks([0, 20,40,60])
    # ax1.set_xticks([60, 120, 180])
    # ax1.text(60, 5, 'Rec Room', fontsize=120, color='red')

    ######worlds uplink disruption
    # ax1.set_yticks([0,300,500,700])
    # ax1.set_xticks([60,120,180])


    #######Worlds downlink disruption
    # ax1.set_xticks([40,80, 120, 160,200, 240, 300])
    # ax1.set_yticks([0,0.3,0.5,0.7,1.0,1.5])
    # ax1.set_xlim([0.1, 310])
    # ax1.set_ylim([0,2.1])
    # ax1.text(5, 1.6, '1.0', fontsize=80, color='red')
    # ax1.text(45, 1.6, '0.7', fontsize=80, color='red')
    # ax1.text(85, 1.6, '0.5', fontsize=80, color='red')
    # ax1.text(125, 1.6, '0.3', fontsize=80, color='red')
    # ax1.text(165, 1.6, '0.2', fontsize=80, color='red')
    # ax1.text(205, 1.6, '0.1', fontsize=80, color='red')
    # ax1.text(260, 1.6, 'N', fontsize=80, color='red')


    ###TCP uplink
    ax1.set_xlim([0.1, 310])
    ax1.set_ylim([0,2.1])
    ax1.set_yticks([0, 0.3, 0.5, 0.7, 1.0, 1.5])
    ax1.set_xticks([60, 120, 180, 240, 300])
    ax1.text(20, 1.35, '5s', fontsize=80, color='red')
    ax1.text(70, 1.35, '10s', fontsize=80, color='red')
    ax1.text(130, 1.35, '15s', fontsize=80, color='red')
    ax1.text(185, 1.35, '100%', fontsize=80, color='red')
    ax1.text(260, 1.35, 'N', fontsize=80, color='red')

    #
    ##tput

    # ax1.set_xlim([0.1, 310])
    # ax1.set_ylim([0,2.1])
    # ax1.set_yticks([0, 0.3, 0.5, 0.7, 1.0, 1.5])
    # ax1.set_xticks([40, 80, 120, 160, 200, 240, 300])
    # ax1.text(5, 1.35, '1.5', fontsize=80, color='red')
    # ax1.text(45, 1.35, '1.2', fontsize=80, color='red')
    # ax1.text(85, 1.35, '1.0', fontsize=80, color='red')
    # ax1.text(125, 1.35, '0.7', fontsize=80, color='red')
    # ax1.text(165, 1.35, '0.5', fontsize=80, color='red')
    # ax1.text(205, 1.35, '0.3', fontsize=80, color='red')
    # ax1.text(260, 1.35, 'N', fontsize=80, color='red')

    #Utilization
    # ax1.set_yticks([0,50,70,100])
    # ax1.set_ylim([0,100])
    # ax1.text(5, 20, '1.0', fontsize=80, color='red')
    # ax1.text(45, 20, '0.7', fontsize=80, color='red')
    # ax1.text(85, 20, '0.5', fontsize=80, color='red')
    # ax1.text(125, 20, '0.3', fontsize=80, color='red')
    # ax1.text(165, 20, '0.2', fontsize=80, color='red')
    # ax1.text(205, 20, '0.1', fontsize=80, color='red')
    # ax1.text(260, 20, 'N', fontsize=80, color='red')
    # ax1.set_ylim([0, 110])







    #this is for diruption
    # plt.fill_between([91,118], 0, 1.55,  # upperbound，downbound
    #                  facecolor='green',  # fill color
    #                  edgecolor='red',  # edge color
    #                  alpha=0.3)  # Transparency
    # plt.vlines(160,0,1.55,colors = "black",linestyle="--",linewidth = 10)

    # ax1.set_ylim([0, 550])
    #ax1.set_ylim([0, 3.1])

    plt.grid()





    # altspace VR
    #plt.legend(fontsize=60, loc='upper center', bbox_to_anchor=(0.23, 1.15))
    plt.legend(fontsize=80, loc='upper center', bbox_to_anchor=(0.5, 1.2),ncol=2,columnspacing=0.4)
    #plt.legend(fontsize=95, loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=2)
    #plt.legend(fontsize=100, loc='best')
    plt.show()

def get_col(filename,col_index):
    data = pd.read_csv(filename, encoding='gbk', engine='python', header=None)
    x = data.iloc[1:, col_index].astype(float)
    return np.array(x)


# u1_file = os.path.join(ROOT,FOLDER,U1_FILENAME)
# # u1_Downlink_Packet_Size = get_col(u1_file,3)
# # u1_Uplink_Packet_Size = get_col(u1_file,4)
# # u1_Downlink_Packet_Rate = get_col(u1_file,5)
# # u1_Uplink_Packet_Rate= get_col(u1_file,6)
# u1_Downlink_Bitrate= get_col(u1_file,1)/1000000
# u1_Uplink_Bitrate= get_col(u1_file,2)/1000000
#
# # u2_file = os.path.join(ROOT,FOLDER,U2_FILENAME)
# # u2_Downlink_Packet_Size = get_col(u2_file,1)
# # u2_Uplink_Packet_Size = get_col(u2_file,2)
# # u2_Downlink_Packet_Rate = get_col(u2_file,3)
# # u2_Uplink_Packet_Rate= get_col(u2_file,4)
# # u2_Downlink_Bitrate= get_col(u2_file,5)/1000000
# # u2_Uplink_Bitrate= get_col(u2_file,6)/1000000
#
# xlabel = 'Time (s)'
# #ylabel1 = 'Packet Size/s (Byte)'
# ylabel2 = 'Packets/s'
# ylabel2 = 'Packets/s'
# ylabel3 = 'Bitrate (Mbps)'
# ########u1#######
# #trace1=[[u1_Uplink_Packet_Size,'Uplink'],[u1_Downlink_Packet_Size,'Downlink']]
# #trace2=[[u1_Uplink_Packet_Rate,'Uplink'],[u1_Downlink_Packet_Rate,'Downlink']]
# trace3=[[u1_Uplink_Bitrate,'Session I'],[u1_Downlink_Bitrate,'Session II']]
# #plot_trace(trace1,xlabel,ylabel1)
# #plot_trace(trace2,xlabel,ylabel2)
# plot_trace(trace3,xlabel,ylabel3)
#
# ########u2#######
# # trace1=[[u2_Uplink_Packet_Size,'Uplink'],[u2_Downlink_Packet_Size,'Downlink']]
# # trace2=[[u1_Uplink_Packet_Rate,'Uplink'],[u1_Downlink_Packet_Rate,'Downlink']]
# # trace3=[[u2_Uplink_Bitrate,'Uplink'],[u2_Downlink_Bitrate,'Downlink']]
# #plot_trace(trace1,xlabel,ylabel1)
# #plot_trace(trace2,xlabel,ylabel2)
# # plot_trace(trace3,xlabel,ylabel3)
