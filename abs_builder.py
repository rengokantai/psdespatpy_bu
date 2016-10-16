import abc
from computer import Computer

class AbsBuilder(object):
    __metaclass__ = abc.ABCMeta

    def get_computer(self):
        return self._computer

    def new_computer(self):
        self._computer = Computer()

    @abc.abstractmethod
    def get_case(self):
        pass

