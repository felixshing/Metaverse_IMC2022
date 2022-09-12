# @Time    : 3/15/22 10:31 PM
# @Author  : Ruizhi Cheng
# @FileName: MTP_latency.py
# @Email   : rcheng4@gmu.edu

import numpy as np
from datetime import datetime, timedelta
hs_time_offset1 = 0.094
hs_time_offset2 = 0.094
PC_time_offset1 = 0.21507644653320312
PC_time_offset2 = 0.21584749221801758
AP_time_offset1 = -0.011548995971679688
AP_time_offset2 = -0.01565265655517578
PING = np.mean([83.638,77.374,77.478])
FPS = 71.431
each_frame = 1000/FPS #millsecond
PC_time_offset = np.mean([PC_time_offset1,PC_time_offset2])

AP_time_offset = np.mean([AP_time_offset1,AP_time_offset2])
hs_time_offset = np.mean([hs_time_offset1, hs_time_offset2])
PC_sys_start_time = datetime.strptime('2022-03-16 00:06:42.332349',"%Y-%m-%d %H:%M:%S.%f")
PC_start_time=PC_sys_start_time-timedelta(seconds=PC_time_offset)
print(PC_start_time.time())
#the first frame which seconds change, and its frame index
hs_sys_start_time=datetime(2022,3,16,0,5,27,0)
hs_change_time_index=161
hs_sys_start_time = hs_sys_start_time-timedelta(milliseconds=hs_change_time_index*each_frame)
hs_start_time = hs_sys_start_time -timedelta(seconds= hs_time_offset)
print(hs_start_time.time())

#first action happens after 6s, second happens after 4 s ...
Sender_timestamp = [5,7,9]
cut_video = 130
Receiver_video_frame_index= [5976,6288,653]


Sender_action_time = PC_start_time+timedelta(seconds=Sender_timestamp[0])
Receiver_action_time = hs_start_time+timedelta(milliseconds=Receiver_video_frame_index[0]*each_frame)
print(Receiver_video_frame_index[0]*each_frame)
print(Sender_action_time)
print(Receiver_action_time)
print(Receiver_action_time.timestamp()-Sender_action_time.timestamp())