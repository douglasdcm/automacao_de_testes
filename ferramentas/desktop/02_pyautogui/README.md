# Instalação

```
python3 -m venv venv
pip install -r requirements.txt
python -m pytest -k test_pyauto_gui
```
Abra a calculadora do Linux e rode

```
python -m pytest -k test_pyauto_gui
```

Bugs comuns

- Ao rodar os testes aparece `pyautogui.ImageNotFoundException`. Rode os comandos abaixo
```
pip uninstall pyscreeze
pip install pyscreeze==0.1.29
```
Fonte:
- https://github.com/asweigart/pyautogui/issues/864
- https://github.com/asweigart/pyscreeze/issues/110