from .base_validator import BaseValidator

class CreateClientTypeValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data

    def validate(self):
        return self.type_name_validator(self.data)

class CreateClientActivityTypeValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data

    def validate(self):
        return self.type_name_validator(self.data)

class CreateClientValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data

    def validate(self):
        self.type_id = self.single_id_validate('type_id',self.data.get("type_id"))
        self.tax_id = self.tax_id_validator(self.tax_id)
        self.client_name = self.single_id_validate('client_name',self.data.get("client_name"))
        self.description = self.single_id_validate('description',self.data.get("description"))

    def tax_id_validator(self,tax_id:str):
        if tax_id is None:
            raise ValueError("tax id required")

        if not isinstance(tax_id,str):
            raise ValueError("tax id must be a string")

        tax_id = tax_id.strip()

        if not tax_id.isdigit():
            raise ValueError("tax id must contain only digits")
        
        if len(tax_id) not in (10,11):
            raise ValueError("tax id must be 10 or 11 digits")
        
        return tax_id
    
class UpdateClientTypeValidator(BaseValidator):
    def __init__(self,type_id:int,**kwargs):
        self.type_id = type_id
        self.type_name = kwargs.get("type_name")
        self.description = kwargs.get("description")

    def validate(self):
        self.single_id_validate('type_id',self.type_id)
        self._check_updatable_fields()

        data = {}

        if self.type_name is not None:
            data["type_name"] = self.text_validate_lower('type_name',self.type_name)
        if self.description is not None:
            data["description"] = self.description_validate('description',self.description)

        return data

    def _check_updatable_fields(self):
        updatable_fields = [
            self.type_name,
            self.description
        ]

        if not any(v is not None for v in updatable_fields):
            raise ValueError("at least one field provided for update")

class UpdateClientActivityTypeValidator(BaseValidator):
    def __init__(self,type_id:int,**kwargs):
        self.type_id = type_id
        self.type_name = kwargs.get("type_name")
        self.description = kwargs.get("description")

    def validate(self):
        self.single_id_validate('type_id',self.type_id)
        self._check_updatable_fields()

        data = {}

        if self.type_name is not None:
            data["type_name"] = self.text_validate_lower('type_name',self.type_name)
        if self.description is not None:
            data["description"] = self.description_validate('description',self.description)

    def _check_updatable_fields(self):
        updatable_fields = [
            self.type_name,
            self.description
        ]

        if not any(v is not None for v in updatable_fields):
            raise ValueError("at least one field provided for update")
        
class UpdateClientValidator(CreateClientValidator):
    def __init__(self,client_id:int,**kwargs):
        self.client_id = client_id
        self.type_id = kwargs.get("type_id")
        self.tax_id = kwargs.get("tax_id")
        self.client_name = kwargs.get("client_name")
        self.description = kwargs.get("description")
        self.is_active = kwargs.get("is_active")
    
    def validate(self):
        self.single_id_validate('client_id',self.client_id)
        self._check_updatable_fields()

        data = {}

        if self.type_id is not None:
            data["type_id"] = self.single_id_validate('type_id',self.type_id)
        if self.tax_id is not None:
            data["tax_id"] = self.tax_id_validator('tax_id',self.tax_id)
        if self.client_name is not None:
            data["client_name"] = self.text_validate('client_name',self.client_name)
        if self.description is not None:
            data["description"] = self.description_validate('description',self.description)
        if self.is_active is not None:
            data["is_active"] = self.is_active_validate('is_active',self.is_active)
        
        return data

    def _check_updatable_fields(self):
        updatable_fields = [
            self.type_id,
            self.tax_id,
            self.client_name,
            self.description,
            self.is_active
        ]

        if not any(v is not None for v in updatable_fields):
            raise ValueError("at least one field must be provided for update")