class ProgrammingLanguage:

    def __init__(self, name: str, typing: str, reflection: str, year: int):

        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self) -> bool:

        return self.typing.lower() == "dynamic"

    def __str__(self) -> str:
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"