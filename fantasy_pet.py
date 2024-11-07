class FantasyPet:
    def __init__(self, name, species, age, price, magic_power):
        # Set attributes directly but with validation
        self.name = name
        self.species = species
        self.age = age
        self.price = price
        self.magic_power = magic_power

    # Setter and Getter for name
    def getName(self):
        return self._name

    def setName(self, value):
        self._name = value

    # Setter and Getter for species
    def getSpecies(self):
        return self._species

    def setSpecies(self, value):
        self._species = value

    # Setter and Getter for age (with validation in the setter)
    def getAge(self):
        return self._age

    def setAge(self, value):
        if value >= 0:
            self._age = value
        else:
            print("Age cannot be negative.")

    # Setter and Getter for price (with validation in the setter)
    def getPrice(self):
        return self._price

    def setPrice(self, value):
        if value >= 0:
            self._price = value
        else:
            print("Price cannot be negative.")

    # Setter and Getter for magic_power
    def getMagicPower(self):
        return self._magic_power

    def setMagicPower(self, value):
        self._magic_power = value

    # Method to describe the pet (name, species, age, and magic power)
    def describePet(self):
        print(f"{self.name} is a {self.age}-year-old {self.species}.")
        print(f"It has the magical power of {self.magic_power}.")
        print("-" * 30)

    # Method to calculate and return the discounted price based on a percentage
    def discountPrice(self, percent):
        if percent < 0 or percent > 100:
            print("Discount percentage must be between 0 and 100.")
            return None
        else:
            discount_amount = (percent / 100) * self.price
            discounted_price = self.price - discount_amount
            return discounted_price

    # Method to display the pet's magic power in action
    def performMagic(self):
        print(f"{self.name} performs a magical move: {self.magic_power}!")
        print("-" * 30)