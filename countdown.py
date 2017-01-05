import time
import sys
import winsound
import os
from random import randint

#print ("Countdown let's Go..")
cwd = os.getcwd()
bip_count = cwd + '\sfx\Bip Count.wav'
bip_start = cwd + '\sfx\Bip Start.wav'

b = randint(4,7)
#print b
#print "+-----------------------------------+"
while b > 0:
	if b > 0:
		time.sleep(0.6)
		winsound.PlaySound(bip_count, winsound.SND_FILENAME)
		#print(b)
		b -= 1
		if b < 1:
			print "\t\t------> Let's Go!!! <------"
			winsound.PlaySound(bip_start, winsound.SND_FILENAME)
			sys.exit()
	else:
		#input("Error")
		sys.exit