from fantasy_pet import FantasyPet

class PetShop:
    def __init__(self):
        # Constructor initializes an empty list to hold FantasyPet objects.
        self.pets = []  # List to store FantasyPet objects

    # Method to add a new pet to the shop
    def addPet(self, pet):
        if isinstance(pet, FantasyPet):  # Ensure the pet is a FantasyPet object
            self.pets.append(pet)
            print(f"Pet {pet.name} added to the shop!")
        else:
            print("The pet must be an instance of FantasyPet.")

    # Method to list all pets in the shop with descriptions
    def listPets(self):
        if self.pets:
            print("Pets available in the shop:")
            for pet in self.pets:
                pet.describePet()  # Use describePet to list the pet details
        else:
            print("No pets available in the shop.")