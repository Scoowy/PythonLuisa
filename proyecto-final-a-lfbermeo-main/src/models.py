from datetime import datetime


class Register:
    def __init__(self, fecha: datetime, infections: int, deaths: int):
        self._fecha = fecha
        self._infections = infections
        self._deaths = deaths

    def getFecha(self):
        return self._fecha

    def getinfections(self):
        return self._infections

    def getdeaths(self):
        return self._deaths

    def __str__(self):
        return f"{self._fecha.strftime('%m/%d/%Y')} - Contagios: {self._infections} | Muertes: {self._deaths}"

    def __repr__(self):
        return self.__str__()


class State:
    def __init__(self, name: str, registers=[]):
        self._name = name
        self._registers = registers

    def getName(self):
        return self._name

    def getRegisters(self):
        return self._registers

    def addRegister(self, register: Register):
        self._registers.append(register)

    def __str__(self):
        return f"{self._name} - Registros: {len(self._registers)}"

    def __repr__(self):
        return self.__str__()


class Country:
    def __init__(self, name: str, states={}):
        self._name = name
        self._states = states

    def getName(self):
        return self._name

    def getStates(self):
        return self._states

    def __str__(self):
        return f"{self._name} - Estados: {len(self._states)}"

    def __repr__(self):
        return self.__str__()
