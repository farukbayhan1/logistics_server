from .base_validator import BaseValidator

class CreateOrderStatusValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data

    def validate(self):
        status_name = self.text_validate_lower('status_name',self.data.get("status_name"))
        description = self.description_validate('description',self.data.get("description"))

        return {
            "status_name":status_name,
            "description":description
        }

class CreateOrderActivityTypeValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data

    def validate(self):
        return self.type_name_validator(self.data)

class CreateOrderValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data

    def validate(self):
        self.returning_data = {}
        self._check_fields()
        return self.returning_data

    def _check_fields(self):
        required_keys = [
            "order_document_id",
            "in_warehouse",
            "in_position",
            "is_active"
        ]

        allowed_keys = [
            "warehouse_id",
            "client_id",
            "status_id",
            "trip_id",
            "order_no",
            "box_count",
            "order_driver",
            "order_plate",
            "trip_number",
            "delivery_address",
            "order_confirmation_date",
            "order_plan_confirmation_date",
            "description"
        ]

        for k, v in self.data.items():
            if k in required_keys:
                if k == "order_document_id":
                    self.single_id_validate(k,v)
                    self.returning_data[k] = v
                else:
                    self.is_active_validate(k,v)
                    self.returning_data[k] = v
            elif k in allowed_keys:
                if k in ["warehouse_id","client_id","status_id","trip_id","box_count"]:
                    self.single_id_validate(k,v)
                    self.returning_data[k] = v
                elif k in ["order_confirmation_date","order_plan_confirmation_date"]:
                    self.time_stamp_validator(k,v)
                    self.returning_data[k] = v
                else:
                    self.text_validate(k,v)
                    self.returning_data[k] = v
            else:
                raise ValueError(f"{k} incorrect field")
            
               
class UpdateOrderStatusValidator(BaseValidator):
    def __init__(self,status_id,**kwargs):
        self._status_id = status_id
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

        if not any(v is None for v in updatable_fields):
            raise ValueError("at least one field provided for update")

class UpdateOrderActivityTypeValidator(BaseValidator):
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
            data['type_name'] = self.type_name
        if self.description is not None:
            self.description('description',self.description)
            data["description"] = self.description
        
        return data
    
    def _check_updatable_fields(self):
        updatable_fields = [
            self.type_name,
            self.description
        ]

        if not any(v is not None for v in updatable_fields):
            raise ValueError("at least one field provided for update")

class UpdateOrderValidator(BaseValidator):
    pass