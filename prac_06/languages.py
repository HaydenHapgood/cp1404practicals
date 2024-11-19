
from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)


languages = [python, ruby, visual_basic]
print("Dynamically typed Languages are:")
for lang in languages:
    if lang.is_dynamic():  # Use the is_dynamic method
        print(lang.name)
