# Class method: bound to the class, not instance. Takes `cls` as first param. Can access/modify class state.

# Static method: not bound to class or instance. Takes no `self`/`cls`. Just a regular function inside a class (for organizational purposes).

class Employee:
    company = "TechCorp"

    @classmethod
    def change_company(cls, name):
        cls.company = name

    @staticmethod
    def is_valid_age(age):
        return age >= 18

Employee.change_company("NewCorp")
print(Employee.company)  # NewCorp

print(Employee.is_valid_age(20))  # True