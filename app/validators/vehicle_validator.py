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
        pattern = r"^(0[1-9]|[1-7][0-9]|8[01])\s[A-Z]{1,3}\s\d{2,4}$"
        
        if not re.match(pattern,plate):
            raise ValueError(f"{field_name}: incorrect plate format")

    def model_year_validate(self,field_name:str,model_year:int):
        if not isinstance(model_year,int):
            raise ValueError("model year must be an integer")
        
        max_year = datetime.now().year + 1
        if model_year >= max_year:
            raise ValueError(f"{field_name}: model year can not bigger than {accepted_year}")
        if model_year <= 1950:
            raise ValueError(f"{field_name}: incorrect model year format")
    
    def capacity_validate(self):
        pass

class UpdateVehicleTypeValidator(BaseValidator):
    pass

class UpdateVehicleValidator(BaseValidator):
    pass