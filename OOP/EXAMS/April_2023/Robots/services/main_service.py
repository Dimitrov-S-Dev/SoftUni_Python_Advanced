from OOP.EXAMS.April_2023.Robots.services.base_service import BaseService


class MainService(BaseService):
    CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, self.CAPACITY)

    def details(self):
        output = f"{self.name} Main Service:\n"
        output += f"Robots: {' '.join(r.name for r in self.robots) if self.robots else 'none'}"
        return output
