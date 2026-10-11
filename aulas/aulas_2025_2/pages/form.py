class Form:
    def __init__(self, driver):
        self._driver = driver

    def fill_username(self, username):
        self._driver.send_text("username", username)

    def fill_password(self, password):
        self._driver.send_text("password", password)

    def fill_email(self, email):
        self._driver.send_text("email", email)

    def fill_bio(self, bio):
        self._driver.send_text("bio", bio)

    def select_country(self, country):
        self._driver.select("country", country)

    def fill_age(self, age):
        self._driver.send_text("age", age)

    def fill_birthdate(self, birthdate):
        self._driver.send_text("birthdate", birthdate)

    def submit(self):
        self._driver.click("submit-btn")
        return self._driver.get_dialog_text()
