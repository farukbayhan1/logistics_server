from .base_validator import BaseValidator

class CreateOrderDocumentStatusValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data
    
    def validate(self):
        status_name = self.text_validate_lower('status_name',self.data.get("status_name"))
        description = self.description_validate('description',self.data.get("description"))

        return {
            "status_name":status_name,
            "description":description
        }

class CreateOrderDocumentActivityTypeValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data

    def validate(self):
        return self.type_name_validator(self.data)
    
class CreateOrderDocumentValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data

    def validate(self):
        status_id = self.single_id_validate('status_id',self.data.get("status_id"))
        document_number = self.text_validate('document_number',self.data.get("document_number"))

        return {
            "status_id":status_id,
            "document_number":document_number
        }
    
class UpdateOrderDocumentValidator(BaseValidator):
    def __init__(self,document_id:int,**kwargs):
        self.document_id = document_id
        self.status_id = kwargs.get("status_id")
        self.document_number = kwargs.get("document_number")
        self.description = kwargs.get("description")
        self.is_active = kwargs.get("is_active")

    def validate(self):
        self.single_id_validate('document_id',self.document_id)
        self._check_updatable_fields()

        data = {}

        if self.status_id is not None:
            self.single_id_validate('status_id',self.status_id)
            data["status_id"] = self.status_id
        if self.document_number is not None:
            self.text_validate('document_number',self.document_number)
            data["document_number"] = self.document_number
        if self.description is not None:
            self.description_validate('description',self.description)
            data["description"] = self.description
        if self.is_active is not None:
            self.is_active_validate('is_active',self.is_active)
            data["is_active"] = self.is_active

        return data

    def _check_updatable_fields(self):
        updatable_fields = [
            self.status_id,
            self.document_number,
            self.description,
            self.is_active
        ]

        if not any(v is not None for v in updatable_fields):
            raise ValueError("at least one field provided for update")
        
class UpdateOrderDocumentStatusValidator(BaseValidator):
    def __init__(self,status_id:int,**kwargs):
        self.status_id = status_id
        self.status_name = kwargs.get("status_name")
        self.description = kwargs.get("description")

    def validate(self):
        self.single_id_validate('status_id',self.status_id)
        self._check_updatable_fields()

        data = {}

        if self.status_name is not None:
            self.text_validate_lower('status_name',self.status_name)
            data["status_name"] = self.status_name
        if self.description is not None:
            self.description_validate('description',self.description)   
            data["description"] = self.description
        
        return data

    def _check_updatable_fields(self):
        updatable_fields = [
            self.status_name,
            self.description
        ]

        if not any(v is not None for v in updatable_fields):
            raise ValueError("at leats one field provided for update")



