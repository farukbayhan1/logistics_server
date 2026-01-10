from .base_validator import BaseValidator

class CreateContactTypeValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data

    def validate(self):
        return self.type_name_validator(self.data)

class CreateContactActivityTypeValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data

    def validate(self):
        return self.type_name_validator(self.data)

class CreateContactValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data

    def validate(self):
        type_id = self.single_id_validate('type_id',self.data.get("type_id"))
        contact_name = self.text_validate('contact_name',self.data.get("contact_name"))
        description = self.description_validate('description',self.data.get("description"))

        return {
            "type_id":type_id,
            "contact_name":contact_name,
            "description":description
        }
    
class UpdateContactTypeValidator(BaseValidator):
    def __init__(self,type_id,**kwargs):
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

class UpdateContactActivityTypeValidator(BaseValidator):
    def __init__(self,type_id:int,**kwargs):
        self.type_id = type_id
        self.type_name = kwargs.get("type_name")
        self.description = kwarg.get("description")

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

class UpdateContactValidator(BaseValidator):
    def __init__(self,contact_id,**kwargs):
        self.contact_id = contact_id
        self.type_id = kwargs.get("type_id")
        self.contact_name = kwargs.get("contact_name")
        self.description = kwargs.get("description")
        self.is_active = kwargs.get("is_active")

    def validate(self):
        self.single_id_validate('contact_id',self.contact_id)
        self._check_updatable_fields()

        data = {}

        if self.type_id is not None:
            data["type_id"] = self.single_id_validate('type_id',self.type_id)
        if self.contact_name is not None:
            data["contact_name"] = self.text_validate('contact_name',self.contact_name)
        if self.description is not None:
            data["description"] = self.description_validate('description',self.description)
        if self.is_active is not None:
            data["is_active"] = self.is_active_validate('is_active',self.is_active)

        return data
        
    def _check_updatable_fields(self):
        updatable_fields = [
            self.type_id,
            self.contact_id,
            self.contact_name,
            self.description,
            self.is_active
        ]

        if not any(v is not None for v in updatable_fields):
            raise ValueError("at least one field provided for update")