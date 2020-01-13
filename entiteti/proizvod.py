class Proizvod():

    def __init__(self, id, naziv):
        self._id_proizvod = id
        self._naziv = naziv
        
    @property
    def id(self):
        return self._id_proizvod

    @property
    def naziv(self):
        return self._naziv


    def __str__(self):
        return """
        id: {0}
        naziv: {1}
        ----------------
        """.format(self._id_proizvod, self._naziv)

    
