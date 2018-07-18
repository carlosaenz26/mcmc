import numpy as np 
import random 
import matplotlib.pylab as plt

t=np.genfromtxt('CircuitoRC.txt', usecols=0, delimiter='')
q = np.genfromtxt('CircuitoRC.txt', usecols=1 , delimiter='')





rin=30
cin=0.01




rguard=np.empty((0))
cguard= np.empty((0))
lguard= np.empty((0))

rguard = np.append(rguard, rin)
cguard = np.append(cguard, cin)




def modelo(t,r,c):
	v=10
	qmax=v*c
	qt=qmax*(1.0-np.exp(-t/(r*c)))
	return qt




def x2(di,d):
	
	x=np.sum((di-d)**2)
	return x

def L(c2):
	lk=np.exp(-1*c2/2)
	return lk




for i in range(10000):

	rgues=np.random.normal(rguard[i],0.3)
	cgues=np.random.normal(cguard[i],0.3)
	
	ying=modelo(t,rguard[i],cguard[i])
	chig=x2(ying,q)/10000
	likev=L(chig)

	yd=modelo(t,rgues,cgues)
	chid=x2(yd,q)/10000
	liken=L(chid)

	alpha=liken/likev

	if alpha> 1:
	
		print cgues
		rguard = np.append(rguard, rgues)
		cguard = np.append(cguard, cgues)
		lguard = np.append(lguard, liken)
		
		
	else:
		beta=random.random()
		if beta<= alpha:
			
			rguard = np.append(rguard, rgues)
			cguard = np.append(cguard, cgues)
			lguard = np.append(lguard, liken)
		else:
			
			rguard = np.append(rguard, rguard[i])
			cguard = np.append(cguard, cguard[i])
			lguard = np.append(lguard, liken)



mejorl= np.argmax(lguard)
mejorc = cguard[mejorl]
mejorr = rguard[mejorl]
mejormodelo=modelo(t,mejorr,mejorc)

plt.figure()
plt.plot(t,q)
plt.plot(t,mejormodelo)
plt.show()

#plt.figure(1)
#plt.plot(mejorl,modelo(t,rguard,cguard)) # esto es un ontento de lo ultimo 
#plt.show()
