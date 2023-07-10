from project.cat import Cat


class Tomcat(Cat):
    gender = "Male"

    def __init__(self, name, age):
        super().__init__(name, age, self.gender)

    def make_sound(self):
        return "Hiss"
