# _*_ coding: utf-8 _*_

"""
Crear un módulo para validación de contraseñas. Dicho módulo, deberá cumplir con
los siguientes criterios de aceptación:
• La contraseña debe contener un mínimo de 8 caracteres
• Una contraseña debe contener letras minúsculas, mayúsculas, números y al menos
1 carácter no alfanumérico
• La contraseña no puede contener espacios en blanco
• Contraseña válida, retorna True
• Contraseña no válida, retorna el mensaje “La contraseña elegida no es segura”
"""


class Contrasena:
    longitud = 0

    def __init__(self, contrasena):
        self.contrasena = contrasena
        pass

    def longitud_contrasena(self):
        """Metodo que determina si una contraseña tiene el largo necesario"""
        if len(self.contrasena) < 8:
            print("La contraseña debe contener almenos 8 caracteres.")
            return False
        else:
            self.longitud = len(self.contrasena)
            # print("La longitud de tu contraseña es:",self.longitud)
            return True
        pass

    def no_tiene_espacio(self):
        """Metodo que determina si una contraseña contiene espacios"""
        bandera = 0
        for x in range(0, self.longitud):
            if self.contrasena[x] == " ":
                bandera = 1
                pass
            pass
        if bandera == 1:
            print("La contraseña no debe contener espacios.")
            return False
            pass
        else:
            return True
        pass

    def minusculas(self):
        """Metodo que determina si una contraseña contiene pueras letras minusculas."""
        if self.contrasena.islower() == True:
            print("La contraseña debe contener por lo menos una mayúscula.")
            return False
        else:
            return True
        pass

    def mayusculas(self):
        """Metodo que determina si una contraseña contiene pueras letras mayusculas."""
        if self.contrasena.isupper() == True:
            print("La contraseña debe contener por lo menos una minuscula.")
            return False
        else:
            return True
        pass

    def mayandmin(self):
        """Metodo que determina si la contraseña posee letras mayusculas y minusculas."""
        if self.minusculas() == True and self.mayusculas() == True:
            return True
            pass
        else:
            return False
        pass

    def caracter_no_alfanumerico(self):
        """Metodo que determina si una contraseña posee por lo menos un caracter alfanumerico."""
        if self.contrasena.isalnum() == True:
            print("La contraseña debe contener almenos un caracter no alfanumerico.")
            return False
            pass
        else:
            return True

    def contrasena_valida(self):
        """Metodo que valida la contraseña."""
        if self.longitud_contrasena() == True and self.no_tiene_espacio() == True and self.mayandmin() == True and self.caracter_no_alfanumerico() == True:
            return True
            pass
        else:
            return False
        pass
