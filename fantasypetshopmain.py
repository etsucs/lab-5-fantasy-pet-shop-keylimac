from fantasy_pet import FantasyPet
from pet_shop import PetShop

def main():
    # Create a PetShop instance
    shop = PetShop()

    # Create some FantasyPet instances
    pet1 = FantasyPet("Flare", "Fire Dragon", 5, 1500.00, "Fire Breath")
    pet2 = FantasyPet("Blaze", "Phoenix", 3, 1200.00, "Rebirth")
    pet3 = FantasyPet("Frost", "Ice Griffin", 4, 1300.00, "Ice Storm")
    pet4 = FantasyPet("Storm", "Thunder Beast", 2, 1000.00, "Thunderstrike")
    
    # Add pets to the shop
    shop.addPet(pet1)
    shop.addPet(pet2)
    shop.addPet(pet3)
    shop.addPet(pet4)

    # Describe each pet
    print("\nDescribing each pet:")
    pet1.describePet()
    pet2.describePet()
    pet3.describePet()
    pet4.describePet()

    # Show discounted price for pet1 (Flare) with a 20% discount
    print("\nApplying a 20% discount on Flare's price:")
    discounted_price = pet1.discountPrice(20)
    if discounted_price is not None:
        print(f"Flare's discounted price: ${discounted_price:.2f}")

    # Perform magic for Blaze (Phoenix)
    print("\nPerforming magic for Blaze (Phoenix):")
    pet2.performMagic()

    # Perform magic for Storm (Thunder Beast)
    print("\nPerforming magic for Storm (Thunder Beast):")
    pet4.performMagic()

    # List all pets in the shop and display their details
    print("\nListing all pets in the shop:")
    shop.listPets()

main()