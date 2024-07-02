# Instalação
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

# Subindo o servidor de CPF fake
```
flask run --reload --port 5001
```
Teste a conexão
```
curl http://127.0.0.1:5001
{"status":"running"}
```

# Usando o servidor fake
- O servidor simula dois endpoints: `validate` e `generate`
- Em um novo terminal execute o teste
```
python -m pytest -k test_demo 
``` 
- Volte ao terminal on o servidor está rodando o verifique os logs
```
127.0.0.1 - - [01/Jul/2024 23:49:30] "POST /validate HTTP/1.1" 200 -
```