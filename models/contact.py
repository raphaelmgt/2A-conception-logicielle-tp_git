class Contact:
    def __init__(self, name: str, phone: str, email: str) -> None:
        self.name: str = name
        self.phone: str = phone
        self.email: str = email

    def __str__(self) -> str:
        return f"Nom: {self.name}, Téléphone: {self.phone}, Email: {self.email}"
