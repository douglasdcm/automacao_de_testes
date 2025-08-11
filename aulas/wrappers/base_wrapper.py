class BaseWrapper:
    def wait_for_text(self, locator, text):
        raise NotImplementedError("This method should be implemented by subclasses")

    def click(self, locator):
        raise NotImplementedError("This method should be implemented by subclasses")

    def hover_over_by_class_name(self, locator):
        raise NotImplementedError("This method should be implemented by subclasses")

    def get_number_of_rows(self, locator):
        raise NotImplementedError("This method should be implemented by subclasses")

    def switch_to_frame(self, locator):
        raise NotImplementedError("This method should be implemented by subclasses")

    def switch_to_default_content(self):
        raise NotImplementedError("This method should be implemented by subclasses")

    def send_text(self, locator, text, clear):
        raise NotImplementedError("This method should be implemented by subclasses")

    def select(self, locator, value):
        raise NotImplementedError("This method should be implemented by subclasses")

    def goto(self, url):
        raise NotImplementedError("This method should be implemented by subclasses")

    def get_text(self, locator):
        raise NotImplementedError("This method should be implemented by subclasses")

    def get_text_by_css(self, locator):
        raise NotImplementedError("This method should be implemented by subclasses")

    def get_text_by_class_name(self, locator):
        raise NotImplementedError("This method should be implemented by subclasses")

    def get_dialog_text(self):
        raise NotImplementedError("This method should be implemented by subclasses")

    def send_text_to_alert(self, text):
        raise NotImplementedError("This method should be implemented by subclasses")

    def store_original_tab(self):
        raise NotImplementedError("This method should be implemented by subclasses")

    def restore_original_tab(self):
        raise NotImplementedError("This method should be implemented by subclasses")

    def dismiss_alert(self):
        raise NotImplementedError("This method should be implemented by subclasses")

    def accept_alert(self):
        raise NotImplementedError("This method should be implemented by subclasses")

    def close_current_tab(self):
        raise NotImplementedError("This method should be implemented by subclasses")

    def quit(self):
        raise NotImplementedError("This method should be implemented by subclasses")
