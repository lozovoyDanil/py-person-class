class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        current = Person.people[person["name"]]

        if "wife" in person and person["wife"] is not None:
            current.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"] is not None:
            current.husband = Person.people[person["husband"]]

    return [Person.people[name] for name in Person.people]
