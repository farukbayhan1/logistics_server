import re
from .base_validator import BaseValidator

class CreatePhoneNumberTypeValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data
    
    def validate(self):
        return self.type_name_validator(self.data)

class CreatePhoneNumberActivityTypeValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data
    
    def validate(self):
        return self.type_name_validator(self.data)

class CreatePhoneNumberValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data

    def validate(self):
        type_id = self.single_id_validate('type_id',self.data.get("type_id"))
        phone_number = self.phone_number_validate('phone_number',self.data.get("phone_number"))
        description = self.description_validate('description',self.data.get("description"))

        return {
            "type_id":type_id,
            "phone_number":phone_number,
            "description":description
        }
    
    def phone_number_validate(self,field_name:str,phone_number):
        pattern = r"^\+?[1-9]\d{1,14}$"

        if not re.match(pattern,phone_number):
            raise ValueError(f"{field_name}: incorrect phone number format")
        
        return phone_number
        
        

class UpdatePhoneNumberTypeValidator(BaseValidator):
    def __init__(self,type_id:int,**kwargs):
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

class UpdatePhoneNumberValidator(CreatePhoneNumberValidator):
    def __init__(self,phone_number_id:int,**kwargs):
        self.phone_number_id = phone_number_id
        self.type_id = kwargs.get("type_id")
        self.phone_number = kwargs.get("phone_number")
        self.description = kwargs.get("description")
        self.is_active = kwargs.get("is_active")

    def validate(self):
        self.single_id_validate('phone_number_id',self.phone_number_id)
        self._check_updatable_fields()

        data = {}

        if self.type_id is not None:
            data["type_id"] = self.single_id_validate('type_id',self.type_id)
        if self.phone_number is not None:
            data["phone_number"] = self.phone_number_validate('phone_number',self.phone_number)
        if self.description is not None:
            data["description"] = self.description_validate('description',self.description)
        if self.is_active is not None:
            data["is_active"] = self.is_active
        
        return data

    def _check_updatable_fields(self):
        updatable_fields = [
            self.type_id,
            self.phone_number,
            self.description,
            self.is_active
        ]

        if not any(v is not None for v in updatable_fields):
            raise ValueError("at least one field provided for update")

