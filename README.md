# automacao_de_testes
Este projeto tem alguns exemplos de scripts de testes automatizados. Todo o material foi desenvolvido em Linux. Caso esteja usando Windows será necessaŕio adaptações. Uma outra alternativa é a utilização do [Cygwin](https://cygwin.com/) para execução de comandos Linux, ou utilizar o [WSL](https://www.treinaweb.com.br/blog/o-que-e-windows-subsystem-for-linux-wsl).

# Run linter
```
rm linter.txt; flake8 --exclude venv,venv*,env*,sikuli* --ignore=E501 --output-file linter.txt; clear; cat linter.txt
```