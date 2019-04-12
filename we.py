#!/usr/bin/python3.6
import subprocess

subprocess.Popen("nohup websockify --web=/usr/share/novnc 40009 192.168.42.246:5990  &", stdout=None, shell=True)

