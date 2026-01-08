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
        pattern = ""

        if not re.match(pattern,phone_number):
            raise ValueError("incorrect phone number format")


class UpdatePhoneNumberTypeValidator(BaseValidator):
    pass

class UpdatePhoneNumberValidator(BaseValidator):
    pass

