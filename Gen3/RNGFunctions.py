def RNGAdvance(S): 
	MULT = 0x41c64e6d
	ADD = 0x6073
	return (S * MULT + ADD) & 0xFFFFFFFF


def H16(x): 
	return x >> 16

class RNG:
	def __init__(self,Seed):
		self.InitSeed = Seed
		self.Seed = Seed
		self.Frame = -1
	def Advance(self, count=1):
		for i in range(0,count):
			self.Seed = (self.Seed * 0x41c64e6d + 0x6073) & 0xFFFFFFFF
			self.Frame += 1
	def Reverse(self, count=1): 
		for i in range(0,count):
			self.Seed = (self.Seed * 0xEEB9EB65 + 0x0A3561A1) & 0xFFFFFFFF
			self.Frame -= 1
	def FAdvance(self):
		self.Seed = (self.Seed * 0x41c64e6d + 0x3039) & 0xFFFFFFFF
		self.Frame += 1
	def H16(self):
		return self.Seed >> 16
	def L16(self):
		return self.Seed & 0xFFFF