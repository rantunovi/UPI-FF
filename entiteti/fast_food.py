class Fast_food():

    def __init__(self, id, naziv, adresa, telefon):
        self._id_fast_food = id
        self._naziv = naziv
        self._adresa = adresa
        self._telefon = telefon

    @property
    def id(self):
        return self._id_fast_food

    @property
    def naziv(self):
        return self._naziv

    @property
    def adresa(self):
        return self._adresa

    @property
    def telefon(self):
        return self._telefon

    def __str__(self):
        return """
        id: {0}
        naziv: {1}
        adresa: {2}
        telefon: {3}
        ----------------
        """.format(self._id_fast_food, self._naziv, self._adresa, self._telefon)

    
