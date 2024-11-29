O mesmo teste é executado múltiplas vezes com frameworks de teste diferentes: Selenium, Playwright e Caqui. Foi utilizado o padrão de projeto Template Mathod para deixar o método de teste genérico para todos os frameworks.

## Instalação

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install
```

# Execução

Nota: Para executar o Caqui inicialize o driver conforme [documentação](https://github.com/douglasdcm/caqui?tab=readme-ov-file#simple-start)

```
pytest
```