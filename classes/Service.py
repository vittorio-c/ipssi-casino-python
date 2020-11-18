import msvcrt
import time
import sys
import subprocess

class Service :
    """ Répertorie les fonctions utilitaires """

    @staticmethod
    def delay10SecondesInput(prompt, timer=time.monotonic):
        sys.stdout.write(prompt)
        sys.stdout.flush()
        endtime = timer() + 10
        result = []
        while timer() < endtime:
            if msvcrt.kbhit():
                result.append(msvcrt.getwche())
                if result[-1] == '\r':
                    return ''.join(result[:-1])
            time.sleep(0.04)
        return ''
        