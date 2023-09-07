def RNGAdvance(S): 
	MULT = 0x41c64e6d
	ADD = 0x6073
	return (S * MULT + ADD) % 0x100000000


def H16(x): 
	return x >> 16