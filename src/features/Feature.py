import abc

class Feature:

    @abc.abstractmethod
    def syntax(self): pass

    @abc.abstractmethod
    def translation(self): pass
        
