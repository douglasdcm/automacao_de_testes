# automacao_de_testes
Este projeto tem alguns exemplos de scripts de testes automatizados. Todo o material foi desenvolvido em Linux Ubuntu e Python 3.11. Caso esteja usando Windows será necessaŕio adaptações. Uma outra alternativa é a utilização do [Cygwin](https://cygwin.com/) para execução de comandos Linux, ou utilizar o [WSL](https://www.treinaweb.com.br/blog/o-que-e-windows-subsystem-for-linux-wsl).

# Executar linter
```
flake8 --exclude venv,venv*,env*,sikuli* --ignore=E501
```
# Ferramentas abordadas
## [mabl](https://www.mabl.com/)
mabl harnesses multiple AI technologies including generative AI to extend test coverage, improve reliability, and reduce maintenance. 
## [Selenium IDE](https://www.selenium.dev/selenium-ide/)
Open source record and playback test automation for the web.
## No framework
Execução de testes sem ferramenta de mercado para mostrar que é possível automatizar mesmo com poucos recursos.
## [Selenium WebDriver](https://www.selenium.dev/documentation/webdriver/)
WebDriver drives a browser natively, as a user would, either locally or on a remote machine using the Selenium server. It marks a leap forward in terms of browser automation.
## [Pytest](https://docs.pytest.org/en/stable/)
The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.
## [SikuliX](https://sikulix-2014.readthedocs.io/en/latest/)
SikuliX allows one to automate visual workflows
## [Dogtail](https://gitlab.com/dogtail/dogtail)
dogtail is a GUI test tool and UI automation framework written in Python. It uses Accessibility (a11y) technologies to communicate with desktop applications. dogtail scripts are written in Python and executed like any other Python program.
## [Behave](https://behave.readthedocs.io/en/latest/)
Behavior-driven development (or BDD) is an agile software development technique that encourages collaboration between developers, QA and non-technical or business participants in a software project.
## [Jmeter](https://jmeter.apache.org/)
The Apache JMeter™ application is open source software, a 100% pure Java application designed to load test functional behavior and measure performance. It was originally designed for testing Web Applications but has since expanded to other test functions.
## [Caqui](https://github.com/douglasdcm/caqui)
Caqui is intended to command executions against Drivers synchronously and asynchronously.
## [Postman](https://www.postman.com/)
Postman is your single platform for collaborative API development.
## [Robot Framework](https://robotframework.org/)
Robot Framework is an open source automation framework for test automation and robotic process automation (RPA).
## [Playwright](https://playwright.dev/python/docs/intro)
Playwright was created specifically to accommodate the needs of end-to-end testing. Playwright supports all modern rendering engines including Chromium, WebKit, and Firefox.

# Padrões de projeto
## [Page Objects Model](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)
Within your web app’s UI, there are areas where your tests interact with. A Page Object only models these as objects within the test code. This reduces the amount of duplicated code and means that if the UI changes, the fix needs only to be applied in one place.
## [Arrange, Act, Assert (AAA)](https://docs.pytest.org/en/stable/explanation/anatomy.html)
Arrange is where we prepare everything for our test. Act is the singular, state-changing action that kicks off the behavior we want to test. Assert is where we look at that resulting state and check if it looks how we’d expect after the dust has settled.
## [Gherkin](https://cucumber.io/docs/gherkin/)
Gherkin uses a set of special keywords to give structure and meaning to executable specifications. Each keyword is translated to many spoken languages.
## Object Repository
Este padrão não tem intenção de ser usado no mercado, mas mostra que novos padrões podem ser explorados além dos mais conhecidos da literatura.
## [Page Transactions](https://guara.readthedocs.io/en/latest/index.html)
The intent of this pattern is to simplify UI test automation. It was inspired by Page Objects, App Actions, and Screenplay. Page Transactions focus on the operations (transactions) a user can perform on a web page, such as Login, Logout, or Submit Forms.
## [Screenplay](https://serenity-js.org/handbook/design/screenplay-pattern/)
The Screenplay Pattern is an innovative, user-centred approach to writing high-quality automated acceptance tests. It steers your team towards effectively using layers of abstraction, helps your test scenarios capture the business vocabulary of your domain, and encourages good testing and software engineering habits.
##
