from .base_validator import BaseValidator

class CreateWarehouseTypeValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data
    
    def validate(self):
        return self.type_name_validator(self.data)

class CreateWarehouseValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data
    
    def validate(self):
        type_id = self.single_id_validate('type_id',self.data.get("type_id"))
        warehouse_name = self.text_validate('warehouse_name',self.data.get("warehouse_name"))
        description = self.description_validate('descripton',self.data.get("description"))

        return {
            "type_id":type_id,
            "warehouse_name":warehouse_name,
            "description":description
        }

class UpdateWarehouseTypeValidator(BaseValidator):
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

        return data
    
    def _check_updatable_fields(self):
        updatable_fields = [
            self.type_name,
            self.description
        ]

        if not any(v is not None for v in updatable_fields):
            raise ValueError("at least one field provided for update")

class UpdateWarehouseValidator(BaseValidator):
    def __init__(self,warehouse_id,**kwargs):
        self.warehouse_id = warehouse_id
        self.type_id = kwargs.get("type_id")
        self.warehouse_name = kwargs.get("warehouse_name")
        self.description = kwargs.get("description")
        self.is_active = kwargs.get("is_active")

    def validate(self):
        self.single_id_validate('warehouse_id',self.warehouse_id)
        self._check_updatable_fields()

        data = {}

        if self.type_id is not None:
            self.single_id_validate('type_id',self.type_id)
            data["type_id"] = self.type_id
        if self.warehouse_name is not None:
            self.text_validate('warehouse_name',self.warehouse_name)
            data["warehouse_name"] = self.warehouse_name
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
            self.warehouse_name,
            self.description,
            self.is_active
        ]

        if not any(v is not None for v in updatable_fields):
            raise ValueError("at least one field provided for update")
