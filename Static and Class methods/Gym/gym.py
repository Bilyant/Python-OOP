from customer import Customer
from trainer import Trainer
from equipment import Equipment
from exercise_plan import ExercisePlan
from subscription import Subscription


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_item_to_obj(self, item_to_add, obj):
        if item_to_add not in obj:
            obj.append(item_to_add)

    def add_customer(self, customer: Customer):
        self.add_item_to_obj(customer, self.customers)

    def add_trainer(self, trainer: Trainer):
        self.add_item_to_obj(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment):
        self.add_item_to_obj(equipment, self.equipment)

    def add_plan(self, plan: ExercisePlan):
        self.add_item_to_obj(plan, self.plans)

    def add_subscription(self, subscription: Subscription):
        self.add_item_to_obj(subscription, self.subscriptions)

    def get_item_by_id(self, item_id, obj):
        for item in obj:
            if item.id == item_id:
                return item

    def subscription_info(self, subscription_id: int):
        subscription = self.get_item_by_id(subscription_id, self.subscriptions)
        customer = self.get_item_by_id(subscription.customer_id, self.customers)
        trainer = self.get_item_by_id(subscription.trainer_id, self.trainers)
        exercise_plan = self.get_item_by_id(subscription.exercise_id, self.plans)
        equipment = self.get_item_by_id(exercise_plan.equipment_id, self.equipment)

        output = [str(subscription), str(customer), str(trainer),
                  str(equipment), str(exercise_plan)]
        return '\n'.join(output)


customer = Customer("John", "Maple Street", "john.smith@gmail.com")
equipment = Equipment("Treadmill")
trainer = Trainer("Peter")
subscription = Subscription("14.05.2020", 1, 1, 1)
plan = ExercisePlan(1, 1, 20)

gym = Gym()

gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)

print(Customer.get_next_id())

print(gym.subscription_info(1))
