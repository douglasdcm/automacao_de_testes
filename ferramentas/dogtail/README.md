# Configuração

Verifique as dependências em https://github.com/vhumpa/dogtail?tab=readme-ov-file#dependencies.

# Execução no Linux
```
virtualenv --system-site-packages env
source env/bin/activate
pip install -r ferramentas/dogtail/requirements.txt
python ferramentas/dogtail/examples/test-test-utf8-procedural-api.py
```
O Gedit é aberto e um texto é copiado para dentro dele.<br>
Outro exemplo agora usando um framework de testes:
```
python -m pytest ferramentas/dogtail/examples/test-demo.py
```
Procure o log e screeshots na pasta `/tmp/dogtail-*`