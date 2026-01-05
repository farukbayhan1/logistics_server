from .base_validator import BaseValidator

class CreateTripStatusValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data

    def validate(self):
        status_name = self.text_validate_lower('status_name',self.data.get("status_name"))
        description = self.description_validate('description',self.data.get("description"))

        return {
            "status_name":status_name,
            "description":description
        }

class CreateTripActivityTypeValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data

    def validate(self):
        return self.type_name_validator(self.data)

class CreateTripValidator(BaseValidator):
    pass

class UpdateTripStatusValidator(BaseValidator):
    pass

class UpdateTripValidator(BaseValidator):
    pass