from main import calculate_pi_parallel

def test_parallel():
    result = calculate_pi_parallel(10000, 4)
    assert 3.1 < result < 3.2, "Resultado fora do esperado para cálculo paralelo"
