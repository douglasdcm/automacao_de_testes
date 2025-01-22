# Instalação

Mais detalhes em
- [Getting Started](https://robotframework.org/?tab=1#getting-started)
- [Quick Start](https://github.com/robotframework/QuickStartGuide/blob/master/QuickStart.rst)
- Available settings
    - [Settings](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#toc-entry-694)
    - [Test Case](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#toc-entry-695)
    - [Keyword](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#keyword-section-1)
- [Complete User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html)
- [SeleniumLibrary](https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html)
- [Libraries](http://robotframework.org/robotframework/#user-guide)
- [Data Driven](https://docs.robotframework.org/docs/testcase_styles/datadriven)

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# verificar a versão o robot framework
robot --version

# Instalação da biblioteca Selenium
webdrivermanager --downloadpath . chrome

# execute o teste pelo nome da pasta
robot google_tests
```

