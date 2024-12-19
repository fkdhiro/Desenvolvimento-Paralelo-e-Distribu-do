
# Como Executar o Projeto

## Instalação
```bash
pip install pytest
```

## Passos para Execução
1. Execute o script principal:
   ```bash
   python main.py
   ```

2. Inicie o servidor distribuído:
   ```bash
   python distributed/server.py
   ```

3. Conecte os clientes ao servidor:
   ```bash
   python distributed/client.py
   ```

4. Execute os testes automatizados:
   ```bash
   pytest tests/
   ```
   ou
   ```bash
   python -m pytest tests/
   ```
