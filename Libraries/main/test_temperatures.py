import unittest
import statistics
from custom_functions import temperature_methods


class TestCollectionMethods(unittest.TestCase):

    def promedio(self):

        list_temp = [38,37,35,34,37,33,32,30,32,35,36,32]
        temp_p = temperature_methods.promedio(list_temp)

        self.assertEqual(temp_p, 29.08)

class TestCollectionMethods(unittest.TestCase):

    def componente_mayor(self):

        list_temp = [38,37,35,34,37,33,32,30,32,35,36,32]
        temp_p = temperature_methods.componente_mayor(list_temp)

        self.assertEqual(temp_p, 38)

class TestCollectionMethods(unittest.TestCase):

    def desviacion_estandar(self):

        list_temp = [38,37,35,34,37,33,32,30,32,35,36,32]
        temp_p = temperature_methods.desviacion_estandar(list_temp)

        self.assertEqual(temp_p, 2.49848438906955)