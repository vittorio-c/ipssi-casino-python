from inputimeout import inputimeout, TimeoutOccurred

class Service :
    """ Répertorie les fonctions utilitaires """

    @staticmethod
    def delayInput(content, timer = 10):
        try:
            response = inputimeout(prompt = content, timeout = timer)
            return response
        except TimeoutOccurred:
            return ''