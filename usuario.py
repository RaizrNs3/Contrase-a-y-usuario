# _*_ coding: utf-8 _*_

"""
Crear un módulo para validación de nombres de usuarios. Dicho módulo, deberá
cumplir con los siguientes criterios de aceptación:
• El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12
• El nombre de usuario debe ser alfanumérico
• Nombre de usuario con menos de 6 caracteres, retorna el mensaje “El nombre de
usuario debe contener al menos 6 caracteres”
• Nombre de usuario con más de 12 caracteres, retorna el mensaje “El nombre de
usuario no puede contener más de 12 caracteres”
• Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el mensaje
“El nombre de usuario puede contener solo letras y números”
• Nombre de usuario válido, retorna True
"""
	
class Usuario:
	"""Usuario es una persona que busca registrarse en un sistema de logueo."""
	def __init__(self, nombre):
		self.nombre = nombre
		pass

	def longitud(self):
		"""El metodo longitud se encarga de determinar si un nombre de usuario tiene la lngitud correcta"""
		#print("Entramos en longitud")
		if len(self.nombre) < 6:
			print("El nombre de usuario debe contener al menos 6 caracteres")
			return False
		elif len(self.nombre) > 12:
			print("El nombre de usuario no puede contener más de 12 caracteres")
			return False
		else:
			return True
	
	def alfanumerico(self):
		"""El metodo alfanumerico determina si el nombre solo contiene letras o numeros."""
		#print("Entramos en alfanumerico")
		if self.nombre.isalnum() == False:
			print("El nombre de usuario puede contener solo letras y números")
			return False
		else:
			return True

	def usuario_valido(self):
		"""El metodo usuario_valido trabaja con los metodos pasados y determina si un nombre es valido
		segun los resultados de los otros dos metodos."""
		#print("Si entramos en Usuario valido")
		if self.longitud() == True and self.alfanumerico() == True:
			return True
		else:
			return False


		








