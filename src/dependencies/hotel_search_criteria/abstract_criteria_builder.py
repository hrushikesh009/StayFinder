import abc


class AbstractCriteriaBuilder(abc.ABC):

    @abc.abstractmethod
    def get_criteria(self):
        pass

    @abc.abstractmethod
    def create_criteria(self):
        pass
