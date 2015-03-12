# -*- coding: utf-8 -*-
'''
Created on 8 ���� 2015

@author: gilad
'''
import httplib
import ctypes 
conn = httplib.HTTPConnection("israel.usembassy.gov");
conn.request("GET", "/consular/niv/checkstatus.html");
r1 = conn.getresponse();
if "AA004RQITW" in r1.read():
	ctypes.windll.user32.MessageBoxA(0, "Visa found!", "US Visa", 1)