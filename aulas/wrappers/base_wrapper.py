class BaseWrapper:
    def click(self, locator):
        raise NotImplementedError("This method should be implemented by subclasses")

    def send_text(self, locator, text):
        raise NotImplementedError("This method should be implemented by subclasses")

    def select(self, locator, value):
        raise NotImplementedError("This method should be implemented by subclasses")

    def goto(self, url):
        raise NotImplementedError("This method should be implemented by subclasses")

    def get_text(self, locator):
        raise NotImplementedError("This method should be implemented by subclasses")

    def get_text_by_name(self, locator):
        raise NotImplementedError("This method should be implemented by subclasses")

    def get_dialog_text(self):
        raise NotImplementedError("This method should be implemented by subclasses")

    def quit(self):
        raise NotImplementedError("This method should be implemented by subclasses")
