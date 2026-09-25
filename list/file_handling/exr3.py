def student_info(name, age, **details):
    info = f"Name: {name}, Age: {age}"
    
    if details:
        for key, value in details.items():
            info += f", {key}: {value}"

    return info


print(student_info("Alice", 20, major="Computer Science", year="Sophomore"))
print(student_info("Bob", 22))

