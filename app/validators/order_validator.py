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

        # Required Fields
        self.returning_data["order_document_id"] = self.single_id_validate('order_document_id',self.data.get("order_document_id"))
        self.returning_data["in_warehouse"] = self.is_active_validate('in_warehouse',self.data.get("in_warehouse"))
        self.returning_data["in_position"] = self.is_active_validate('in_position',self.data.get("in_position"))
        self.returning_data["is_active"] = self.is_active_validate('is_active',self.data.get("is_active"))
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
            "delivered_at",
            "description"
        ]

        for k, v in self.data.items():
            if k not in required_keys and k in allowed_keys:
                if "id" in k or k == "box_count":
                    self.single_id_validate(k,v)
                    self.returning_data[k] = v
                if "date" in k:
                    self.date_validate(k,v)
                    self.returning_data[k] = v
               
class UpdateOrderStatusValidator(BaseValidator):
    pass

class UpdateOrderActivityTypeValidator(BaseValidator):
    pass

class UpdateOrderValidator(BaseValidator):
    pass