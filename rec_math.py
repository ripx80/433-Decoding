#!/usr/bin/python 
#coding: utf-8

from datetime import datetime, timedelta, date
import json
from pprint import pprint
import matplotlib.pyplot as plt

max_dur = 5
def Decodetime(obj):
	if '__type__' not in obj:
		return obj
	t = obj.pop('__type__')
	if t == 'datetime':
		return datetime(**obj)
	elif t == 'timedelta':
		return timedelta(**obj)
	else:
		print('warning: not implemented')
		return obj

with open('./samples/sample-in.json') as fp:	
	samples = json.loads(json.load(fp))

# ~ for i,v in enumerate(samples[0]):
	# ~ pprint(i)
	# ~ exit(0)
	# ~ samples[0][i]=Decodetime(samples[0][i])

samples[0][:]=[Decodetime(i) for i in samples[0]]
strone=""
print('**Processing results**')
for i in range(len(samples[0])):		
	samples[0][i] = (samples[0][i].second + (samples[0][i].microsecond/1000000.0))/100
	#samples[0][i] = samples[0][i].microsecond/1000000.0
	strone+=str(samples[1][i])
	# ~ print(samples[0][i].microsecond/1000000.0)
	# ~ print(samples[0][i].second)
	# ~ exit(0)
print(strone)
print('**Plotting results**')
#print(samples[0])
#print(samples[1])
#plt.plot([1,2,3,4],[1,4,9,16],'ro')
#plt.axis([0,6,0,20])
plt.plot(samples[0], samples[1])
plt.axis([0.00, 5.00, 0, 2])
#plt.axis([0, max_dur, -1, 2])
plt.show()
