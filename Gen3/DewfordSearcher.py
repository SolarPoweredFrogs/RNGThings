from RNGFunctions import RNG
from DewfordCommon import MakeDewfordPhrase

Seedstr = input('Input Initial Seed (use 0x before hexadecimal seeds) (this will be your TID in Emerald): ')
if 'x' in Seedstr:
	Seed = int(Seedstr,16)
else:
	Seed = int(Seedstr)

Seed = RNG(Seed)

MIN = int(input('Min Advance: '))    #Min advancement to Search
MAX = int(input('Max Number of Advances: '))    #Max advancement to Search

def FormatStringForTrendy(S):
	S = str.upper(S)
	S = str.replace(S,"'","")
	S = str.replace(S," ","")
	S = str.replace(S,"_","")
	S = str.replace(S,"-","")
	return S

T1 = input("Input first word of trendy phrase: ")
T1 = FormatStringForTrendy(T1)

T2 = input("Input second word of trendy phrase: ")
T2 = FormatStringForTrendy(T2)

#Advance RNG to min frame
Seed.Advance(MIN)

#Print values in range that match given phrase
for y in range(0,MAX):
	Seed.Advance()
	TestPhrase = MakeDewfordPhrase(Seed)
	if ' '.join([T1,T2]) in TestPhrase:
		print(TestPhrase)
