class Database :
    """ Permet de créer la connexion et les interractions avec la base de données """

    # Voir comment créer une connexion tout en s'assurant de la fermer
    # https://stackoverflow.com/questions/38076220/python-mysqldb-connection-in-a-class

    host = '' # Lien de connexion avec la BDD,
    identifiant = ''
    password = ''
    database = ''
    #...
    
    def __init__(self) :
        connection_string = ''
        identifiant = ''
        password = ''
    
    def query(self, query_string) :
        """ Permet de faire une requête à partir du paramètre """
        #return le resultat de la requête
    
