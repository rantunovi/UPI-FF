class Stavka():

    def __init__(self, id, id_narudzba, id_proizvod_fast_food):
        self._id_stavka = id
        self._id_narudzba = id_narudzba
        self._id_proizvod_fast_food = id_proizvod_fast_food

    @property
    def id(self):
        return self._id_stavka

    @property
    def id_narudzba(self):
        return self._id_narudzba

    @property
    def id_proizvod_fast_food(self):
        return self._id_proizvod_fast_food

    def __str__(self):
        return """
        id: {0}
        id_narudzba: {1}
        id_proizvod_fast_food: {2}
        ----------------
        """.format(self._id_stavka, self._id_narudzba, self._id_proizvod_fast_food)

    
