from RNGFunctions import RNGAdvance
from RNGFunctions import H16

Seedstr = input('Input Initial Seed (use 0x before hexadecimal seeds) (this will be your TID in Emerald): ')
if 'x' in Seedstr:
	Seed = int(Seedstr,16)
else:
	Seed = int(Seedstr)
	
MIN = int(input('Input Min Advance: '))    #Min advancement to Search
MAX = int(input('Input Max Advance: '))    #Max advancement to Search

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

def TrendyPhraseSeed(x,trend1,trend2,frame): 
	CONDITIONS=['HOT', 'EXISTS', 'EXCESS', 'APPROVED', 'HAS', 'GOOD', 'LESS', 'MOMENTUM', 'GOING', 'WEIRD', 'BUSY', 'TOGETHER', 'FULL', 'ABSENT', 'BEING', 'NEED', 'TASTY', 'SKILLED', 'NOISY', 'BIG', 'LATE', 'CLOSE', 'DOCILE', 'AMUSING', 'ENTERTAINING', 'PERFECTION', 'PRETTY', 'HEALTHY', 'EXCELLENT', 'UPSIDEDOWN', 'COLD', 'REFRESHING', 'UNAVOIDABLE', 'MUCH', 'OVERWHELMING', 'FABULOUS', 'ELSE', 'EXPENSIVE', 'CORRECT', 'IMPOSSIBLE', 'SMALL', 'DIFFERENT', 'TIRED', 'SKILL', 'TOP', 'NONSTOP', 'PREPOSTEROUS', 'NONE', 'NOTHING', 'NATURAL', 'BECOMES', 'LUKEWARM', 'FAST', 'LOW', 'AWFUL', 'ALONE', 'BORED', 'SECRET', 'MYSTERY', 'LACKS', 'BEST', 'LOUSY', 'MISTAKE', 'KIND', 'WELL', 'WEAKENED', 'SIMPLE', 'SEEMS', 'BADLY']
	LIFESTYLE=['CHORES', 'HOME', 'MONEY', 'ALLOWANCE', 'BATH', 'CONVERSATION', 'SCHOOL', 'COMMEMORATE', 'HABIT', 'GROUP', 'WORD', 'STORE', 'SERVICE', 'WORK', 'SYSTEM', 'TRAIN', 'CLASS', 'LESSONS', 'INFORMATION', 'LIVING', 'TEACHER', 'TOURNAMENT', 'LETTER', 'EVENT', 'DIGITAL', 'TEST', 'DEPTSTORE', 'TELEVISION', 'PHONE', 'ITEM', 'NAME', 'NEWS', 'POPULAR', 'PARTY', 'STUDY', 'MACHINE', 'MAIL', 'MESSAGE', 'PROMISE', 'DREAM', 'KINDERGARTEN', 'LIFE', 'RADIO', 'RENTAL', 'WORLD']
	HOBBIES=['IDOL', 'ANIME', 'SONG', 'MOVIE', 'SWEETS', 'CHAT', 'CHILDSPLAY', 'TOYS', 'MUSIC', 'CARDS', 'SHOPPING', 'CAMERA', 'VIEWING', 'SPECTATOR', 'GOURMET', 'GAME', 'RPG', 'COLLECTION', 'COMPLETE', 'MAGAZINE', 'WALK', 'BIKE', 'HOBBY', 'SPORTS', 'SOFTWARE', 'SONGS', 'DIET', 'TREASURE', 'TRAVEL', 'DANCE', 'CHANNEL', 'MAKING', 'FISHING', 'DATE', 'DESIGN', 'LOCOMOTIVE', 'PLUSHDOLL', 'PC', 'FLOWERS', 'HERO', 'NAP', 'HEROINE', 'FASHION', 'ADVENTURE', 'BOARD', 'BALL', 'BOOK', 'FESTIVAL', 'COMICS', 'HOLIDAY', 'PLANS', 'TRENDY', 'VACATION', 'LOOK']
	
	w1 = CONDITIONS[H16(x) % 69]
	x = RNGAdvance(x)
	CAT = H16(x) % 2
	x = RNGAdvance(x)
	if CAT == 1:
	  w2 = LIFESTYLE[H16(x) % 45]
	else:
	  w2 = HOBBIES[H16(x) % 54]
	x = RNGAdvance(x)    #used to set whether trendiness is increasing or decreasing, don't really care about
	x = RNGAdvance(x)
	occ = 5
	z = H16(x) % 98
	if z > 50:
	  x = RNGAdvance(x)
	  occ += 1
	  z = H16(x) % 98
	  if z > 80:
	    x = RNGAdvance(x)
	    z = H16(x) % 98
	    occ += 1
	z += 30
	x = RNGAdvance(x)    #used to set current trendiness, don't really care about
	x = RNGAdvance(x)
	occ += 2
	FSeed = H16(x)
	if (trend1 == w1) & (trend2 == w2):
	  print(str(frame), ':', w1, w2, str(hex(FSeed)),str(frame + occ))
	#return FSeed

#Advance RNG to min frame
for y in range(0, MIN):
  Seed = RNGAdvance(Seed)

#Print values in range that match given phrase
for y in range(MIN,MAX):
  TrendyPhraseSeed(Seed,T1,T2,y)
  Seed = RNGAdvance(Seed)