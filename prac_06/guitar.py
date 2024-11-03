class Guitar:
    def __init__(self, name: str, year: int, cost: float):

        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self) -> str:
        return f"{self.name} ({self.year}), Cost: ${self.cost:.2f}"

    def get_age(self) -> int:
        current_year = 2024
        return current_year - self.year

    def is_vintage(self) -> bool:
        return self.get_age() >= 50