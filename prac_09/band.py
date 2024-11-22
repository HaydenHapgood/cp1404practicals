class Band:

    def __init__(self, name=""):
        self.name = name
        self.musicians = []

    def __str__(self):
        musicians_info = ', '.join(f"{musician.name} ({musician.instruments})" for musician in self.musicians)
        return f"{self.name} ({musicians_info})"

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        play_info = []
        for musician in self.musicians:
            play_info.append(musician.play())
        return "\n".join(play_info)
