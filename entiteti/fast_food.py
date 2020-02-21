class Fast_food():

    def __init__(self, id, naziv, adresa, ikona, lokacija, path):
        self._id_fast_food = id
        self._naziv = naziv
        self._adresa = adresa
        self._ikona = ikona
        self._lokacija = lokacija
        self._path = path
        

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
    def ikona(self):
        return self._ikona

    @property
    def lokacija(self):
        return self._lokacija

    @property
    def path(self):
        return self._path

    def __str__(self):
        return """
        id: {0}
        naziv: {1}
        adresa: {2}
        ikona: {3}
        lokacija: {4}
        path: {5}
        ----------------
        """.format(self._id_fast_food, self._naziv, self._adresa, self._ikona, self._lokacija, self._path)

    
