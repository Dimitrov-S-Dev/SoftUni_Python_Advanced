class Person:
    def __init__(self, name, age):
        # self.__name = name
        # self.__age = age
        self.__set_name(name)
        self.__set_age(age)

    def __set_name(self, new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name

    def __set_age(self, new_age):
        self.__age = new_age

    def get_age(self):
        return self.__age
