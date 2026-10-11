Repositório base para curso de automação de testes

Estrutura de pastas:
- colab: arquivos do Google Colaboratory
- planos: arquvivos de plano de projeto
- prompts: arquivos contendo exemplos de prompts para engenharia de prompting
- scripts: exemplos de scritps de testes com Selenium Webdriver

Como usar:
- colab: importe os arquivos no Google Colaboratory e execute os comandos linha a linha para entender os exemplos
- planos: use para configurar agentes de IA
- prompts: use para requisitar serviços do agente de IA
- scritps: configure o setup conforme abaixo e execute os scripts para mais detalhes do funcionamento do Selenium Webdriver

```bash
# configure o ambiente virtual
python3.11 -m venv venv

# ative o ambiente virtual
source venv/bin/activate

# instale as dependências
pip install selenium pytest

# execute os testes
# todos
python -m pytest

# por nome
python -m pytest -k <nome do teste>
```