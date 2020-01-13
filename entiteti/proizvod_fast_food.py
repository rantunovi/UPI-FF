class Proizvod_fast_food():

    def __init__(self, id, id_proizvod, id_fast_food, cijena):
        self._id_proizvod_fast_food = id
        self._id_proizvod =id_proizvod 
        self._id_fast_food = id_fast_food
        self._cijena = cijena

    @property
    def id(self):
        return self._id_proizvod_fast_food

    @property
    def id_proizvod(self):
        return self._id_proizvod

    @property
    def id_fast_food(self):
        return self._id_fast_food

    @property
    def cijena(self):
        return self._cijena

    def __str__(self):
        return """
        id: {0}
        id_proizvod: {1}
        id_fast_food: {2}
        cijena: {3}
        ----------------
        """.format(self._id_proizvod_fast_food, self._id_proizvod, self._id_fast_food, self._cijena)

    
