from RNGFunctions import RNGAdvance
from RNGFunctions import H16

TID = int(input('Enter your target ID: '))
MaxDay = int(input('Max number of days: '))
MaxFrame = int(input('Max number of advancements: '))

Seed = 0

def LRNGAdvance(S): 
	MULT = 0x4e6d
	ADD = 12345
	return (S * MULT + ADD) % 0x10000

def LottoDayAdvance(frame,seed,MaxDay,target):
	LSeed = H16(seed)
	for i in range(1,MaxDay+1):
		LSeed = LRNGAdvance(LSeed)
		if LSeed == target:
			print(i, frame)

for i in range(0,MaxFrame):
	Seed = RNGAdvance(Seed)
	LottoDayAdvance(i,Seed,MaxDay,TID)
