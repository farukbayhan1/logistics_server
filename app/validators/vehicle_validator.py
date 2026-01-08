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
        capacity = self.capacity_validate('capacity',self.data.get("capacity"))
        description = self.description_validate('description',self.data.get("description"))
    
        return {
            "type_id":type_id,
            "plate":plate,
            "brand":brand,
            "model":model,
            "model_year":model_year,
            "capacity":capacity,
            "description":description
        }

    def plate_validate(self,field_name:str,plate):
        pattern = r"^(0[1-9]|[1-7][0-9]|8[01])\s[A-Z]{1,3}\s\d{2,4}$"
        
        if not re.match(pattern,plate):
            raise ValueError(f"{field_name}: incorrect plate format")

        return plate
    
    def model_year_validate(self,field_name:str,model_year:int):
        if not isinstance(model_year,int):
            raise ValueError("model year must be an integer")
        
        max_year = datetime.now().year + 1
        if model_year >= max_year:
            raise ValueError(f"{field_name}: model year can not bigger than {accepted_year}")
        if model_year <= 1950:
            raise ValueError(f"{field_name}: incorrect model year format")

        return model_year
    
    def capacity_validate(self,field_name:str,capacity):
        max_digits = 5
        max_decimals = 2

        if abs(capacity) >= 10 ** max_digits:
            raise ValueError(f"{field_name}: too many digits")
        
        decimals = str(capacity).split(".")[1] if "." in str(capacity) else ""
        if len(decimals) > max_decimals:
            raise ValueError("too many decimals")
        
        return capacity

class UpdataVehicleValidator(CreateVehicleValidator):
    def __init__(self,vehicle_id,**kwargs):
        self.vehicle_id = vehicle_id
        self.type_id = kwargs.get("type_id")
        self.plate = kwargs.get("plate")
        self.brand = kwargs.get("brand")
        self.model = kwargs.get("model")
        self.model_year = kwargs.get("model_year")
        self.capacity = kwargs.get("capacity")
        self.description = kwargs.get("description")
        self.is_active = kwargs.get("description")

    def validate(self):
        self.single_id_validate('vehicle_id',self.vehicle_id)
        self._check_updatable_fields()

        data = {}

        if self.type_id is not None:
            self.single_id_validate('type_id',self.type_id)
            data["type_id"] = self.type_id
        if self.plate is not None:
            self.plate_validate('plate',self.plate)
            data["plate"] = self.plate
        if self.brand is not None:
            self.text_validate('brand',self.brand)
            data["brand"] = self.brand
        if self.model is not None:
            self.text_validate('model',self.model)
            data["model"] = self.model
        if self.model_year is not None:
            self.model_year_validate('model_year',self.model_year)
            data["model_year"] = self.model_year
        if self.capacity is not None:
            self.capacity_validate('capacity',self.capacity)
            data["capacity"] = self.capacity
        if self.description is not None:
            self.description_validate('description',self.description)
            data["description"] = self.description
        if self.is_active is not None:
            self.is_active_validate('is_active',self.is_active)
            data["is_active"] = self.is_active
        
        return data

    def _check_updatable_fields(self):
        updatable_fields = [
            self.type_id,
            self.plate,
            self.brand,
            self.model,
            self.model_year,
            self.capacity,
            self.description,
            self.is_active
        ]

        if not any(v is not None for v in updatable_fields):
            raise ValueError("at least one field provided for update")

class UpdataVehicleTypeValidator(BaseValidator):
    def __init__(self,type_id,**kwargs):
        self.type_id = type_id
        self.type_name = kwargs.get("type_name")
        self.description = kwargs.get("description")

    def validate(self):
        self.single_id_validate('type_id',self.type_id)
        self._check_updatable_fields()

        data = {}

        if self.type_name is not None:
            self.text_validate_lower('type_name',self.type_name)
            data["type_name"] = self.type_name
        if self.description is not None:
            self.description_validate('description',self.description)
            data["description"] = self.description

        return data

    def _check_updatable_fields(self):
        updatable_fields = [
            self.type_name,
            self.description
        ]

        if not any(v is not None for v in updatable_fields):
            raise ValueError("at least one field provided for update")