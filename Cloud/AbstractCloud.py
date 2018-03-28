from abc import ABC, abstractmethod

class AbstractCloud(ABC):

    # custom data structures defined for sake of instantiation
    globalIndex = []
    lineageChain = []
    kMaxHeaps = []

    def __init__(self):
        pass

    def userInput(self, DAG, deadLine, openFilter):
        # get approximate fogs from global index
        # compute induvidual slack times of each task

        # calls recheckMicrobatches in Fog
        pass

    def store_in_lineage_chain(self, microbatch_lambda_list):
        self.compute_min_Lambda(microbatch_lambda_list)
        pass

    def compute_min_lambda(self,microbatch_lamda_list):
        pass

    def task_done(self,task, next_task, edge_lambdas, derived_microbatch):
        pass

    def task_undone(self):
        # recompute slacks

        # if microbatch unavailable, call StepE
        self.compute_stepE()
        pass

    def compute_stepE(self):
        pass


    def update_global_index(self):
        pass

    def update_heap(self):
        pass
