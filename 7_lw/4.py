class Name:
    def __init__(self, name) -> None:
        if name not in ["Богдан", "Анонім"]:
            raise ValueError("Дозволені імена: Богдан, Анонім")
        self.name = name

a = Name("Ладик")