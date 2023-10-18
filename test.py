class Human:
    name = ''
    def voice(self):
        print(f"Hello! My name is {self.name}")


class Developer(Human):
    field_description = "My Programming language"
    language = ""
    def make_some_code(self):
        return f"{self.field_description} is {self.value}"


class PythonDeveloper(Developer):
    value = "Python"


class JSDeveloper(Developer):
    value = "JavaScript"


p_dev = PythonDeveloper()
p_dev.name = 'Bob'
p_dev.voice()   # Hello! My name is Bob
p_dev.make_some_code()  # My Programming language is Python


js_dev = JSDeveloper()
js_dev.make_some_code()  # My Programming language is JavaScript

dev = Developer()
dev.name = 'as'
print(dev.make_some_code)
