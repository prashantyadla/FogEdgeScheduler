from abc import ABC, abstractmethod


class AbstractEdge(ABC):
    def __init__(self):
        pass

    def telemetry(self):
        pass

    def pullMicrobatch(self, microbatch):
        pass


    def executeTask(self,task, microbatch):
        pass




