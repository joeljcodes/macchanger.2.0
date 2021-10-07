#!/usr/bin/env python
import subprocess
subprocess.call("ifconfig",shell=True)
subprocess.call("ifconfig eth0 down",shell=True)
subprocess.call("ifconfig eth0 hw ether 00:88:22:11:44:55",shell=True)
subprocess.call("ifconfig eth0 up",shell=True)
subprocess.call("ifconfig",shell=True)
