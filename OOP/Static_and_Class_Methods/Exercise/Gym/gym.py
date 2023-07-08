from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subs_id: int):
        subscription = [s for s in self.subscriptions if s.id == subs_id][0]

        cust_id = subscription.customer_id
        customer = [c for c in self.customers if c.id == cust_id][0]

        t_id = subscription.trainer_id
        trainer = [t for t in self.trainers if t.id == t_id][0]

        exr_id = subscription.exercise_id
        exercise = [e for e in self.plans if e.id == exr_id][0]

        eq_id = exercise.equipment_id
        equipment = [e for e in self.equipment if e.id == eq_id][0]

        output = f"{repr(subscription)}\n"
        output += f"{repr(customer)}\n"
        output += f"{repr(trainer)}\n"
        output += f"{repr(equipment)}\n"
        output += f"{repr(exercise)}"

        return output

