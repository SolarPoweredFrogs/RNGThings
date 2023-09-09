from RNGFunctions import RNG

def MakeDewfordPhrase(S):
	CONDITIONS=['HOT', 'EXISTS', 'EXCESS', 'APPROVED', 'HAS', 'GOOD', 'LESS', 'MOMENTUM', 'GOING', 'WEIRD', 'BUSY', 'TOGETHER', 'FULL', 'ABSENT', 'BEING', 'NEED', 'TASTY', 'SKILLED', 'NOISY', 'BIG', 'LATE', 'CLOSE', 'DOCILE', 'AMUSING', 'ENTERTAINING', 'PERFECTION', 'PRETTY', 'HEALTHY', 'EXCELLENT', 'UPSIDEDOWN', 'COLD', 'REFRESHING', 'UNAVOIDABLE', 'MUCH', 'OVERWHELMING', 'FABULOUS', 'ELSE', 'EXPENSIVE', 'CORRECT', 'IMPOSSIBLE', 'SMALL', 'DIFFERENT', 'TIRED', 'SKILL', 'TOP', 'NONSTOP', 'PREPOSTEROUS', 'NONE', 'NOTHING', 'NATURAL', 'BECOMES', 'LUKEWARM', 'FAST', 'LOW', 'AWFUL', 'ALONE', 'BORED', 'SECRET', 'MYSTERY', 'LACKS', 'BEST', 'LOUSY', 'MISTAKE', 'KIND', 'WELL', 'WEAKENED', 'SIMPLE', 'SEEMS', 'BADLY']
	LIFESTYLE=['CHORES', 'HOME', 'MONEY', 'ALLOWANCE', 'BATH', 'CONVERSATION', 'SCHOOL', 'COMMEMORATE', 'HABIT', 'GROUP', 'WORD', 'STORE', 'SERVICE', 'WORK', 'SYSTEM', 'TRAIN', 'CLASS', 'LESSONS', 'INFORMATION', 'LIVING', 'TEACHER', 'TOURNAMENT', 'LETTER', 'EVENT', 'DIGITAL', 'TEST', 'DEPTSTORE', 'TELEVISION', 'PHONE', 'ITEM', 'NAME', 'NEWS', 'POPULAR', 'PARTY', 'STUDY', 'MACHINE', 'MAIL', 'MESSAGE', 'PROMISE', 'DREAM', 'KINDERGARTEN', 'LIFE', 'RADIO', 'RENTAL', 'WORLD']
	HOBBIES=['IDOL', 'ANIME', 'SONG', 'MOVIE', 'SWEETS', 'CHAT', 'CHILDSPLAY', 'TOYS', 'MUSIC', 'CARDS', 'SHOPPING', 'CAMERA', 'VIEWING', 'SPECTATOR', 'GOURMET', 'GAME', 'RPG', 'COLLECTION', 'COMPLETE', 'MAGAZINE', 'WALK', 'BIKE', 'HOBBY', 'SPORTS', 'SOFTWARE', 'SONGS', 'DIET', 'TREASURE', 'TRAVEL', 'DANCE', 'CHANNEL', 'MAKING', 'FISHING', 'DATE', 'DESIGN', 'LOCOMOTIVE', 'PLUSHDOLL', 'PC', 'FLOWERS', 'HERO', 'NAP', 'HEROINE', 'FASHION', 'ADVENTURE', 'BOARD', 'BALL', 'BOOK', 'FESTIVAL', 'COMICS', 'HOLIDAY', 'PLANS', 'TRENDY', 'VACATION', 'LOOK']
	
	x = RNG(S.Seed)
	
	High16 = '%04x' % x.H16()    #state at start of first word
	w1 = CONDITIONS[x.H16() % 69]  #first word
	x.Advance()
	CAT = x.H16() & 1  #category of second word: 0 for hobbies, 1 for lifestyle
	x.Advance()
	if CAT == 1:
	  w2 = LIFESTYLE[x.H16() % 45]
	else:
	  w2 = HOBBIES[x.H16() % 54]
	#x.Advance()    #used to set whether trendiness is increasing or decreasing, don't really care about
	x.Advance(2)
	z = x.H16() % 98
	if z > 50:
	  x.Advance()
	  z = x.H16() % 98
	  if z > 80:
	    x.Advance()
	    z = x.H16() % 98
	z += 30
	#x.Advance()    #used to set current trendiness, don't really care about
	x.Advance(2)    #feebas seed
	FSeed = '%04x' % x.H16()
	Phrase = ' '.join([str(S.Frame),':',High16,w1,w2,FSeed,str(S.Frame+x.Frame+2)])
	return Phrase