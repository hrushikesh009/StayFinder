import abc


class AbstractCriteriaDirector(abc.ABC):
    @abc.abstractmethod
    def build_criteria(self):
        pass

    @abc.abstractmethod
    def get_criteria(self):
        pass
