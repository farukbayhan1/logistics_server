from .base_validator import BaseValidator
import re
from datetime import datetime

class CreateVehicleTypeValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data

    def validate(self):
        return self.type_name_validator(self.data)

class CreateVehicleActivityTypeValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data

    def validate(self):
        return self.type_name_validator(self.data)

class CreateVehicleValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data

    def validate(self):
        type_id = self.single_id_validate('type_id',self.data.get("type_id"))
        plate = self.plate_validate('plate',self.data.get("plate"))
        brand = self.text_validate('brand',self.data.get("brand"))
        model = self.text_validate('model',self.data.get("model"))
        model_year = self.model_year_validate('model_year',self.data.get("model_year"))
        capacity = ""
        description = self.description_validate('description',self.data.get("description"))
    

    def plate_validate(self,field_name:str,plate):
        pattern = r""
        
        if not re.match(pattern,plate):
            raise ValueError(f"{field_name}: incorrect plate format")

    def model_year_validate(self,field_name:str,model_year):
        pass

class UpdateVehicleTypeValidator(BaseValidator):
    pass

class UpdateVehicleValidator(BaseValidator):
    pass