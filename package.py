# Class to hold package information
class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        # Default status set
        self.status = "Not shipped yet: At hub"
        # Default Delivery time
        self.delivery_time = None
        # Default truck
        self.truck = None

    def __str__(self):
        # Formatting for all packages
        delivery_time = self.delivery_time if self.delivery_time else "N/A"
        return (f"Package ID : {self.package_id}\n"
                f"Delivery Address: {self.address}\n"
                f"Delivery City: {self.city}\n"
                f"Delivery State: {self.state}\n"
                f"Delivery Zip: {self.zip_code}\n"
                f"Delivery Deadline: {self.deadline}\n"
                f"Package Weight: {self.weight}\n"
                f"Status: {self.status}\n"
                f"Delivery Time: {delivery_time}\n"
                f"Truck: {self.truck}\n")

