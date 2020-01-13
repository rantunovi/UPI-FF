class Narudzba():



    def __init__(self, id, id_korisnik, id_fast_food):
        self._id_narudzba = id
        self._id_korisnik = id_korisnik
        self._id_fast_food = id_fast_food

    @property
    def id(self):
        return self._id_narudzba

    @property
    def id_korisnik(self):
        return self._id_korisnik

    @property
    def id_fast_food(self):
        return self._id_fast_food


    def __str__(self):
        return """
        id: {0}
        id_korisnik: {1}
        id_fast_food: {2}
        ----------------
        """.format(self._id_narudzba, self._id_korisnik, self._id_fast_food)

    
