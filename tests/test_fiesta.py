import pytest
from src.fiesta.fuerza_bruta.fuerza_bruta import planificar_fiesta_fuerza_bruta

class TestFiestaFuerzaBruta:
    @pytest.fixture
    def caso_simple(self):
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
        return adj_matrix, conviviality, expected_invitation, expected_sum

    @pytest.fixture
    def caso_complejo(self):
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
        return adj_matrix, conviviality, expected_invitation, expected_sum

    @pytest.fixture
    def caso_un_empleado(self):
        adj_matrix = [[0]]
        conviviality = [5]
        expected_invitation = [1]
        expected_sum = 5
        return adj_matrix, conviviality, expected_invitation, expected_sum

    def test_caso_simple(self, caso_simple):
        adj_matrix, conviviality, expected_invitation, expected_sum = caso_simple
        invitation, total = planificar_fiesta_fuerza_bruta(adj_matrix, conviviality)
        assert invitation == expected_invitation
        assert total == expected_sum

    def test_caso_complejo(self, caso_complejo):
        adj_matrix, conviviality, expected_invitation, expected_sum = caso_complejo
        invitation, total = planificar_fiesta_fuerza_bruta(adj_matrix, conviviality)
        assert invitation == expected_invitation
        assert total == expected_sum

    def test_caso_un_empleado(self, caso_un_empleado):
        adj_matrix, conviviality, expected_invitation, expected_sum = caso_un_empleado
        invitation, total = planificar_fiesta_fuerza_bruta(adj_matrix, conviviality)
        assert invitation == expected_invitation
        assert total == expected_sum