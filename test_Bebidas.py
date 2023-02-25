import unittest
import Bebidas

class test_Bebidas(unittest.TestCase):
    def test_add(self):
        #1 Ejemplo exitoso
        self.assertTrue(Bebidas.agregar_nueva_bebida("Coca Cola, 1, 5, 8, 10, 12")) 

        #2 Error por desorden
        with self.assertRaises(Exception) as context:
            Bebidas.agregar_nueva_bebida("Coca Cola, 5, 10, 6, 5, 12")
        self.assertEqual(str(context.exception), "Rango de tamanos incorrecto por estar en desorden")

        #3 Error por longitud del nombre (demasiado largo)
        with self.assertRaises(Exception) as context:
            Bebidas.agregar_nueva_bebida("Turbo Mega Ultra Big Cola, 1, 5, 8, 10, 12")
        self.assertEqual(str(context.exception), "Nombre de bebida demasiado largo (mas de 15)")

        #4 Error por longitud del nombre (demasiado corto)
        with self.assertRaises(Exception) as context:
            Bebidas.agregar_nueva_bebida("T, 1, 5, 8, 10, 12")
        self.assertEqual(str(context.exception), "Nombre de bebida demasiado corto (menos de 1)")

        #5 Nombre de bebida justo en el limite de longitud (15) pero con espacios
        self.assertTrue(Bebidas.agregar_nueva_bebida("Turbo Ultra Chola, 1, 5, 8, 10, 12"))

        #6 Error por tamano fuera del rango (arriba)
        with self.assertRaises(Exception) as context:
            Bebidas.agregar_nueva_bebida("Fanta, 1, 5, 8, 10, 49")
        self.assertEqual(str(context.exception), "Tamano de bebida fuera del rango (demasiado grande)")

        #7 Error por tamano fuera del rango (abajo)
        with self.assertRaises(Exception) as context:
            Bebidas.agregar_nueva_bebida("Fanta, 0, 5, 8, 10, 12")
        self.assertEqual(str(context.exception), "Tamano de bebida fuera del rango (demasiado pequeno)")

        #8 Error por nombre con caracteres invalidos
        with self.assertRaises(Exception) as context:
            Bebidas.agregar_nueva_bebida("Fant@, 1, 5, 8, 10, 12")
        self.assertEqual(str(context.exception), "El nombre de la bebida contiene caracteres invalidos")

        #9 Error por formato invalido (separador)
        with self.assertRaises(Exception) as context:
            Bebidas.agregar_nueva_bebida("Fanta 1 5 8 10 12")
        self.assertEqual(str(context.exception), "Los elementos de la bebida no estan formateados correctamente")

        #9 Error por formato invalido (inconsistente)
        with self.assertRaises(Exception) as context:
            Bebidas.agregar_nueva_bebida("Fanta, 1, 5, 8 10 12")
        self.assertEqual(str(context.exception), "Los elementos de la bebida no estan formateados correctamente")

        #10 Error por formato invalido (desorden de los elementos)
        with self.assertRaises(Exception) as context:
            Bebidas.agregar_nueva_bebida("1, 5, 8, 10, 12, Fanta")
        self.assertEqual(str(context.exception), "Los elementos de la bebida no estan formateados correctamente")

        #11 Error por falta de tamanos
        with self.assertRaises(Exception) as context:
            Bebidas.agregar_nueva_bebida("Fanta")
        self.assertEqual(str(context.exception), "No hay tamanos de bebidas")

        #12 Error por exceso de tamanos
        with self.assertRaises(Exception) as context:
            Bebidas.agregar_nueva_bebida("Fanta, 1, 2, 3, 4, 5, 6")
        self.assertEqual(str(context.exception), "Hay demasiados tamanos de bebidas ingresados")

        #13 Error por entrada vacia
        with self.assertRaises(Exception) as context:
            Bebidas.agregar_nueva_bebida()
        self.assertEqual(str(context.exception), "No hay informacion sobre la bebida (nombre, tamanos)")

        #14 Error por tamano invalido
        with self.assertRaises(Exception) as context:
            Bebidas.agregar_nueva_bebida("Fanta, 1, @, 3, 4, 5")
        self.assertEqual(str(context.exception), "Tamano invalido de bebida")

        #15 Tamano decimal
        with self.assertRaises(Exception) as context:
            Bebidas.agregar_nueva_bebida("Fanta, 1, 2.5, 3.5, 4.8, 5")
        self.assertEqual(str(context.exception), "Tamano invalido de bebida")

        #16 Entrada sin espacios
        self.assertTrue(Bebidas.agregar_nueva_bebida("Fanta,1,2,3,4,5")) 

        #17 Comas innecesarias en la entrada
        with self.assertRaises(Exception) as context:
            Bebidas.agregar_nueva_bebida("Fanta, 1, 5, , 10, 12")
        self.assertEqual(str(context.exception), "Los elementos de la bebida no estan formateados correctamente")


if __name__=='__main__':
    unittest.main()