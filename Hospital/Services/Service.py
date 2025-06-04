from abc import ABC, abstractmethod

# patient.registering_status: "discharged" (False) / "admitted" (True)
# patient.billing_status: "unpaid" (False) / "paid" (True)

# Service class - abstract class

class Service(ABC):
    @abstractmethod
    def status(self, patient):
        pass