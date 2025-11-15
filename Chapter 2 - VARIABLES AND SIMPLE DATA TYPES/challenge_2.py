# 2-3. Personal Message
name = "eric"
print(f"“Hello {name.title()}, would you like to learn some Python today?")

# 2-4. Name Cases
name = "peter"
print(name.lower())
print(name.upper())
print(name.title())

# 2-5. Famous Quote
name = "Albert Einstein"
print(f'{name} once said, "A person who never made a mistake never tried anything new."')

# 2-6. Famous Quote 2
famous_person = "Albert Einstein"
message = f'{name} once said, "A person who never made a mistake never tried anything new."'
print(message)

# 2-7. Stripping Names
my_famous_person = " Hannah Njuguna "
print(f"\t\n {my_famous_person}")
print(f"\t\n {my_famous_person.lstrip()}")
print(f"\t\n {my_famous_person.rstrip()}")
print(f"\t\n {my_famous_person.strip()}")

# 2-8. File Extensions
file_name = "python_notes.txt"
print(f"\n {file_name.removesuffix(".txt")}")
