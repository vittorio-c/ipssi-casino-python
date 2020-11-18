class ConfigurationLevel :
    """ Contient les informations d'un niveau """

    number = None
    nb_try = None
    interval = None
    gain = []

    def __init__(self, number, nb_try, interval, gain = []) :
        self.number = number
        self.nb_try = nb_try
        self.interval = interval
        self.gain = gain