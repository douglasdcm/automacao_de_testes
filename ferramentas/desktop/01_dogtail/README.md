# Configuração

Verifique as dependências em https://github.com/vhumpa/dogtail?tab=readme-ov-file#dependencies.

# Execução no Linux
```
virtualenv --system-site-packages env
source env/bin/activate
pip install -r ./dogtail/requirements.txt
python ./examples/gedit-test-utf8-procedural-api.py
```
O Gedit é aberto e um texto é copiado para dentro dele.<br>
Outro exemplo agora usando um framework de testes:
```
python -m pytest ./examples/test_demo.py
```
Procure o log e screeshots na pasta `/tmp/dogtail-*`

Mais informações em https://wiki.ubuntu.com/Testing/Automation/DogtailTutorial
