class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        # Check if the sequence is null right at the beginning
        if strbases == "":
            print("NULL sequence created")
            self.strbases = "NULL"
            return

        if not all(base in "ACGT" for base in strbases):
            print("Invalid sequence created!")
            self.strbases = "ERROR"
            return

        # If the sequence is not null, assign the value to self.strbases
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""
        # We return the string with the sequence
        return f"(Length: {self.len()}) {self.strbases}" if self.strbases else "NULL"

    # Esto no tiene que hacer print, aquí se crean las clases y se importan haciendo un sources root a los sucesivos ejercicios.

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

# self es una forma de acceder a las variables y métodos de la instancia de la clase desde dentro de la propia clase.
