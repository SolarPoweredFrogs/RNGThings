TID = int(input('Enter your target ID: '))
MaxDay = int(input('Max number of days: '))
MinFrame = 100
MaxFrame = int(input('Max number of advancements: '))

Seed = 0

def RNGAdvance(S): 
	MULT = 0x41c64e6d
	ADD = 0x6073
	return (S * MULT + ADD) % 0x100000000

for i in range(0,MinFrame):
	Seed = RNGAdvance(Seed)

def LRNGAdvance(S): 
	MULT = 0x4e6d
	ADD = 12345
	return (S * MULT + ADD) % 0x10000


def H16(x): 
	return x >> 16

def LottoDayAdvance(frame,seed,MaxDay,target):
	LSeed = H16(seed)
	for i in range(1,MaxDay+1):
		LSeed = LRNGAdvance(LSeed)
		if LSeed == target:
			print(i, frame)

for i in range(MinFrame,MaxFrame):
	Seed = RNGAdvance(Seed)
	LottoDayAdvance(i,Seed,MaxDay,TID)