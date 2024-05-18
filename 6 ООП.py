
import random

class Flower:
    def __init__(self, name, color, price, freshness):
        self.name = name
        self.color = color
        self.price = price
        self.freshness = freshness

    def __str__(self):
        return f"{self.color} {self.name} ({self.freshness} свіжість), ${self.price}"

class Rose(Flower):
    def __init__(self, color, price, freshness):
        super().__init__("Роза", color, price, freshness)

class Tulip(Flower):
    def __init__(self, color, price, freshness):
        super().__init__("Тюльпан", color, price, freshness)

class Lily(Flower):
    def __init__(self, color, price, freshness):
        super().__init__("Лілія", color, price, freshness)

class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda x: x.freshness, reverse=True)

    def find_flower_by_length(self, min_length, max_length):
        return [flower for flower in self.flowers if min_length <= len(flower.name) <= max_length]

# Creating flower objects
flowers = [
    Rose("Червона", 10, random.randint(1, 10)),
    Tulip("Жовта", 8, random.randint(1, 10)),
    Lily("Біла", 15, random.randint(1, 10))
]

# Creating a bouquet and adding flowers to it
bouquet = Bouquet()
for flower in flowers:
    bouquet.add_flower(flower)

# Sorting flowers by freshness
bouquet.sort_by_freshness()
print("\nВідсортований букет за свіжістю:")
for flower in bouquet.flowers:
    print(flower)

