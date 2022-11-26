
#Implementación del patron Singleton
class SingleConversion:
	__instance=None
	def __init__(self):
		if SingleConversion.__instance!=None:
			raise Exception("Esta clase solo permite una instancia")
		else:
			SingleConversion.__instance=self
	@staticmethod
	def getInstance():
		if SingleConversion.__instance==None:
			SingleConversion()
		return SingleConversion.__instance


