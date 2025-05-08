import unittest
from src.fiesta.fuerza_bruta.fuerza_bruta import planificar_fiesta_fuerza_bruta

class TestFiestaFuerzaBruta(unittest.TestCase):
    def test_caso_simple(self):
        adj_matrix = [
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0]
        ]
        conviviality = [10, 30, 15, 5, 8]
        expected_invitation = [0, 1, 0, 0, 1]
        expected_sum = 38
        
        invitation, total = planificar_fiesta_fuerza_bruta(adj_matrix, conviviality)
        self.assertEqual(invitation, expected_invitation)
        self.assertEqual(total, expected_sum)
    
    def test_caso_complejo(self):
        adj_matrix = [
            [0, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        conviviality = [12, 18, 5, 10, 8, 7]
        expected_invitation = [1, 0, 0, 1, 0, 1]
        expected_sum = 29
        
        invitation, total = planificar_fiesta_fuerza_bruta(adj_matrix, conviviality)
        self.assertEqual(invitation, expected_invitation)
        self.assertEqual(total, expected_sum)
    
    def test_caso_un_empleado(self):
        adj_matrix = [[0]]
        conviviality = [5]
        expected_invitation = [1]
        expected_sum = 5
        
        invitation, total = planificar_fiesta_fuerza_bruta(adj_matrix, conviviality)
        self.assertEqual(invitation, expected_invitation)
        self.assertEqual(total, expected_sum)

if __name__ == '__main__':
    unittest.main()