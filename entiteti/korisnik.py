class Korisnik():

    def __init__(self, id, ime, email, password):
        self._id_korisnik = id
        self._ime = ime
        self._email = email
        self._password = password

    @property
    def id(self):
        return self._id_korisnik

    @property
    def ime(self):
        return self._ime

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password

    def __str__(self):
        return """
        id: {0}
        ime: {1}
        email: {2}
        password: {3}
        ----------------
        """.format(self._id_korisnik, self._ime, self._email, self._password)

    
