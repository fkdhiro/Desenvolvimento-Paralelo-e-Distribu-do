from main import calculate_pi_sequential

def test_sequential():
    result = calculate_pi_sequential(10000)
    assert 3.1 < result < 3.2, "Resultado fora do esperado para cálculo sequencial"
