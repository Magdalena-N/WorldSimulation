class Tile:

    def __init__(self, pozycja, org):
        self._organizm = org
        self._pozycja = pozycja

    def empty(self):
        return self._organizm is None

    # getters and setters
    def set_organizm(self, organizm):
        self._organizm = organizm

    def get_organizm(self):
        return self._organizm

    def set_pozycja(self, pozycja):
        self._pozycja = pozycja

    def get_pozycja(self):
        return self._pozycja

