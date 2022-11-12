# ACM IMC '22: Are We Ready for Metaverse? A Measurement Study of Social Virtual Reality Platforms
This repository contains scripts used in our ACM IMC'22 paper "Are We Ready for Metaverse? A Measurement Study of Social Virtual Reality Platforms".
https://dl.acm.org/doi/abs/10.1145/3517745.3561417

## Repo Structure
```
Repo Root
+-- disruption.py           # Sec. 8: Network Disruptions
+-- plot_paper.py           # Backbond of plotting results
+-- ovr_plot.py             # Get data from OVR Metrics Tool and plot the results
+-- wireshark_plot.py       # Plot network trace from Wireshark
+-- E2Elatency              # Sec. 7: End-to-end Latency
    +-- crop_video.py       # Crop video
    +-- video2frame.py      # Extract the video frame from the video
    +-- quest2_AP_sync.py   # Sync time between Quest2s
    +-- E2Elatency.py       # Calculate the E2E latency
```

## Personal Homepage
[Homepage](https://felixshing.github.io/)

## Notes
Please consider citing our paper if you think the source code is useful in your research project.
```
@inproceedings{cheng2022are,
    author = {Ruizhi Cheng, Nan Wu, Matteo Varvello, Songqing Chen, and Bo Han},
    title = {{Are We Ready for Metaverse? A Measurement Study of Social Virtual Reality Platforms}},
    year = {2022},
    booktitle={Proceedings of ACM SIGCOMM Conference on Internet Measurement (IMC)}
}
```
You may also feel interested in our measurement study on Horizon Workrooms: https://ieeexplore.ieee.org/document/9757549
and
our visionary paper about Metaverse from the network perspective: https://ieeexplore.ieee.org/document/9877927.

## Contact
Ruizhi Cheng by rcheng4@gmu.edu
