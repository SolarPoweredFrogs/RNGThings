from DewfordCommon import MakeDewfordPhrase
from RNGFunctions import RNG

Seedstr = input('Input Initial Seed (use 0x before hexadecimal seeds) (this will be your TID in Emerald): ')
if 'x' in Seedstr:
	Seed = int(Seedstr,16)
else:
	Seed = int(Seedstr)

Seed = RNG(Seed)

MIN = int(input('Min Advance: '))    #Min advancement to Search
MAX = int(input('Max Number of Advances: '))    #Max advancement to Search

#Advance RNG to min frame
Seed.Advance(MIN)

#Print values in range
for y in range(0,MAX):
	Seed.Advance()
	print(MakeDewfordPhrase(Seed))
