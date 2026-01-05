from .base_validator import BaseValidator
import re

class CreateEmailTypeValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data

    def validate(self):
        return self.type_name_validator(self.data)

class CreateEmailActivityTypeValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data

    def validate(self):
        return self.type_name_validator(self.data)

class CreateEmailValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data

    def validate(self):
        self.type_id = self.single_id_validate('type_id',self.data.get("type_id"))
        self.email = self.email_validate(self.data.get("email"))
        self.description = self.description_validate('description',self.data.get("description"))

        return {
            "type_id":self.type_id,
            "email":self.email,
            "description":self.description
        }
    
    def email_validate(self,email):
        pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        if not re.match(pattern,email):
            raise ValueError("incorrect email address")
        
        return email

class UpdateEmailValidator(CreateEmailValidator):
    def __init__(self,email_id,**kwargs):
        self.email_id = email_id
        self.type_id = kwargs.get("type_id")
        self.email = kwargs.get("email")
        self.description = kwargs.get("description")
        self.is_active = kwargs.get("is_active")

    def validate(self):
        self.single_id_validate('email_id',self.email_id)
        self._check_updatable_fields()

        data = {}

        if self.type_id is not None:
            self.single_id_validate('type_id',self.type_id)
            data["type_id"] = self.type_id
        if self.email is not None:
            self.email_validate(self.email)
            data["email"] = self.email
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
            self.email,
            self.description,
            self.is_active
        ]

        if not any(v is not None for v in updatable_fields):
            raise ValueError("at leats one field provided for update")

class UpdateEmailActivityTypeValidator(BaseValidator):
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



