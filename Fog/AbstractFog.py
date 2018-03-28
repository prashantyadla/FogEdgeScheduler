from abc import ABC, abstractmethod


class AbstractFog(ABC):

    # custom data structures defined for sake of instantiation
    local_index = []
    delta_index = []
    CEP_query = "Stored Query"
    edge_registry = {}
    next_task_registry = {}


    def __init__(self):
        pass

    def recheck_and_register_cep(self, microbatch_list,task, filter, slack_time):
        # returns <true/false, true/false, next microbatch> and best lambda for each microbatch
        self.compute_stepA()
        self.compute_stepB()
        self.compute_stepC()
        pass


    def compute_stepA(self):

        pass

    def compute_stepB(self):
        pass

    def compute_stepC(self):
        pass

    def compute_stepD(self):
        pass

    def acknowledge_task(self, input_microbatch, task, slack_time):           # function called from Cloud
        self.store_in_next_task_registry(task,slack_time)
        self.compute_stepD()
        pass

    def store_in_next_task_registry(self,task,slack_time):
        pass

    def no_acknowledge_task(self,input_microbatch, task):
        pass

    def telemetry(self):
        pass

    def out_of_range__termication_notification(self,gamma,edge):
        pass

    def task_incomplete(self,A, omega):
        pass

    def task_complete(self,task):
        pass

    def cep_filter(self):
        pass

    def update_delta_index(self):
        pass









