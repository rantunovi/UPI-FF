class Korisnik():

    def __init__(self, id, ime, email, password, vlasnik):
        self._id_korisnik = id
        self._ime = ime
        self._email = email
        self._password = password
        self._vlasnik=vlasnik

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

    @property
    def vlasnik(self):
        return self._vlasnik

    def __str__(self):
        return """
        id: {0}
        ime: {1}
        email: {2}
        password: {3}
        vlasnik: {4}
        ----------------
        """.format(self._id_korisnik, self._ime, self._email, self._password, self._vlasnik)

    
