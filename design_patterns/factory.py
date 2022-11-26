from abc import ABC, abstractmethod
from math import pi

#Abstract class
class Figura(ABC):

	@abstractmethod
	def draw(self):
		pass
	@abstractmethod
	def area(self):
		pass

#Clases concretas
class Circulo(Figura):
	def __init__(self, radio=1.0):
		self.radio=radio
	def area(self):
		return (pi*(self.radio*self.radio))
	def draw(self):
		print("Imagine un circulo muy bonito")

class Triangulo(Figura):
	def __init__(self, base=1.0, altura=1.0):
		self.base=base
		self.altura=altura
	def area(self):
		return ((self.base*self.altura)/2.0)
	def draw(self):
		print("Imagine un triangulo muy bonito")

class FiguraFactory:
	def __init__(self):
		pass
	def getFigura(self, type, parameters:dict):
		if type=="Triangulo":
			return Triangulo(parameters['base'], parameters['altura'])
		else:
			if type=="Circulo":
				return Circulo(parameters['radio'])