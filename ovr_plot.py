# @Time    : 2/24/22 3:00 PM
# @Author  : Ruizhi Cheng
# @FileName: ovr_plot.py
# @Email   : rcheng4@gmu.edu


#This program is used to plot the metrics collected by OVR metrics tool.
import matplotlib.pyplot as plt
from plot_paper import plot_trace
import numpy as np
import pandas as pd
import os

PLATFORM = '../../Worlds'
TYPE='dis'
DATE='0406_dis/downlink_shooting_1'

FILENAME = '20220406_155342_worlds_downlink_shooting_dis_process.csv'
file = os.path.join(PLATFORM,TYPE,DATE,FILENAME)


def get_time_stamp(filename):
    data = pd.read_csv(filename, encoding='gbk',engine='python',header= None)
    x = data.iloc[1:, 0].astype(int)
    return np.array(x)


def get_battery_level_percentage(filename):
    data = pd.read_csv(filename, encoding='gbk',engine='python',header= None)
    x = data.iloc[1:, 3].astype(int)
    return np.array(x)

def get_battery_temperature_celcius(filename):
    data = pd.read_csv(filename, encoding='gbk',engine='python',header= None)
    x = data.iloc[1:, 4].astype(int)
    return np.array(x)


def get_cpu_level(filename):
    data = pd.read_csv(filename, encoding='gbk',engine='python',header= None)
    x = data.iloc[1:, 10].astype(int)
    return np.array(x)

def get_gpu_level(filename):
    data = pd.read_csv(filename, encoding='gbk',engine='python',header= None)
    x = data.iloc[1:, 11].astype(int)
    return np.array(x)


def get_average_frame_rate(filename):
    data = pd.read_csv(filename, encoding='gbk',engine='python',header= None)
    x = data.iloc[1:, 17].astype(int)
    return np.array(x)

def get_avg_pred_ms(filename):
    data = pd.read_csv(filename, encoding='gbk', engine='python', header=None)
    x = data.iloc[1:, 19].astype(int)
    return np.array(x)

def get_screen_tear_count(filename):
    data = pd.read_csv(filename, encoding='gbk',engine='python',header= None)
    x = data.iloc[1:, 20].astype(int)
    return np.array(x)

def get_early_frame_count(filename):
    data = pd.read_csv(filename, encoding='gbk',engine='python',header= None)
    x = data.iloc[1:, 21].astype(int)
    return np.array(x)

def get_stale_frame_count(filename):
    data = pd.read_csv(filename, encoding='gbk',engine='python',header= None)
    x = data.iloc[1:, 22].astype(int)
    return np.array(x)

def get_foveation_level(filename):
    data = pd.read_csv(filename, encoding='gbk', engine='python', header=None)
    x = data.iloc[1:, 24].astype(int)
    return np.array(x)

def get_eye_buffer_width(filename):
    data = pd.read_csv(filename, encoding='gbk',engine='python',header= None)
    x = data.iloc[1:, 25].astype(int)
    return np.array(x)

def get_eye_buffer_height(filename):
    data = pd.read_csv(filename, encoding='gbk',engine='python',header= None)
    x = data.iloc[1:, 26].astype(int)
    return np.array(x)

def get_app_gpu_time(filename):
    data = pd.read_csv(filename, encoding='gbk', engine='python', header=None)
    x = data.iloc[1:, 27].astype(int)
    return np.array(x)

def get_time_wrap_gpu_time(filename):
    data = pd.read_csv(filename, encoding='gbk',engine='python',header= None)
    x = data.iloc[1:, 28].astype(int)
    return np.array(x)

def get_cpu_utilization_percentage(filename):
    data = pd.read_csv(filename, encoding='gbk',engine='python',header= None)
    x = data.iloc[1:, 30].astype(int)
    return np.array(x)

def get_gpu_utilization_percentage(filename):
    data = pd.read_csv(filename, encoding='gbk',engine='python',header= None)
    x = data.iloc[1:, 39].astype(int)
    return np.array(x)


average_frame_rate = get_average_frame_rate(file)
early_frame_rate = get_early_frame_count(file)
stale_frame_rate = get_stale_frame_count(file)
app_gpu_time=get_app_gpu_time(file)
time_wrap_gpu_time=get_time_wrap_gpu_time(file)
eye_buffer_width=get_eye_buffer_width(file)
eye_buffer_height=get_eye_buffer_height(file)
foveation_level = get_foveation_level(file)
screen_tear_count = get_screen_tear_count(file)
avg_pred_ms=get_avg_pred_ms(file)
time_stamp = get_time_stamp(file)
cpu_utilization_percentage=get_cpu_utilization_percentage(file)
gpu_utilization_percentage=get_gpu_utilization_percentage(file)


frame = [[average_frame_rate,'Average'],[stale_frame_rate,'Stale'],[early_frame_rate,'Early']]
resolution = [[eye_buffer_width,'Width'],[eye_buffer_height,'Height']]
#print(resolution)
twgt= [[time_wrap_gpu_time,'time_wrap_gpu_time']]
pred = [[avg_pred_ms,'avg_pred_ms']]
foveation=[[foveation_level,'foveation_level']]
tear = [[screen_tear_count,'screen_tear_count']]
app_gpu_time=[[app_gpu_time,'app_gpu_time']]
#print(tear)
#print(resolution)
utilization = [[cpu_utilization_percentage,'CPU'],[gpu_utilization_percentage,'GPU']]
#plot_trace(frame,'Time (s)','frame')
#plot_trace(resolution,'Time (s)','Resolution')
#print(height)
#plot_trace(height,'timestamp','value')
plot_trace(utilization,'Time (s)', 'Utilization (%)' )
#plot_trace(utilization,'Time (s)','value')