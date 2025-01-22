# Configuração

Verifique as dependências em https://github.com/vhumpa/dogtail?tab=readme-ov-file#dependencies.

# Execução no Linux
```
python -m venv venv
sudo apt install libcairo2-dev libxt-dev libgirepository1.0-dev
source env/bin/activate
pip install -r ./dogtail/requirements.txt
python ./examples/gedit-test-utf8-procedural-api.py
```

Se rodando com Python 3.11+ pode ser que tenha que fazer [isso](https://gitlab.com/dogtail/dogtail/-/issues/37#note_2304763633)

O Gedit é aberto e um texto é copiado para dentro dele.<br>
Outro exemplo agora usando um framework de testes:
```
python -m pytest ./examples/test_pretty.py
```
Procure o log e screeshots na pasta `/tmp/dogtail-*`

Mais informações em
- https://wiki.ubuntu.com/Testing/Automation/DogtailTutorial
- https://fedoramagazine.org/automation-through-accessibility/
- https://fedorapeople.org/~vhumpa/dogtail/epydoc/