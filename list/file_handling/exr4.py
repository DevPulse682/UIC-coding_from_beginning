def describe_pet(animal, name="unknown"):
    pet_name = f"animal: {animal}, Name: {name}"
    
    return pet_name

print(describe_pet("Dog", "Buddy"))