class Recenzija():

    def __init__(self, id, id_fast_food, id_korisnik, komentar, ocjena):
        self._id_recenzija = id
        self._id_fast_food = id_fast_food 
        self._id_korisnik = id_korisnik
        self._komentar = komentar
        self._ocjena = ocjena

    @property
    def id(self):
        return self._id_recenzija

    @property
    def id_fast_food(self):
        return self._id_fast_food

    @property
    def id_korisnik(self):
        return self._id_korisnik

    @property
    def komentar(self):
        return self._komentar
    
    @property
    def ocjena(self):
        return self._ocjena

    def __str__(self):
        return """
        id: {0}
        id_fast_food: {1}
        id_korisnik: {2}
        komentar: {3}
        ocjena: {4}
        ----------------
        """.format(self._recenzija, self._id_fast_food, self._id_korisnik, self._komentar, self._ocjena)

    
