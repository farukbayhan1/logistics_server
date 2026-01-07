from .base_validator import BaseValidator

class CreateTripStatusValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data

    def validate(self):
        status_name = self.text_validate_lower('status_name',self.data.get("status_name"))
        description = self.description_validate('description',self.data.get("description"))

        return {
            "status_name":status_name,
            "description":description
        }

class CreateTripActivityTypeValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data

    def validate(self):
        return self.type_name_validator(self.data)

class CreateTripValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data

    def validate(self):
        status_id = self.single_id_validate('status_id',self.data.get("status_id"))
        vehicle_id = self.single_id_validate('vehicle_id',self.data.get("vehicle_id"))
        driver_id = self.single_id_validate('driver_id',self.data.get("driver_id"))
        courier_id = self.single_id_validate('courier_id',self.data.get("courier_id"))
        loaded_province_id = self.single_id_validate('loaded_province_id',self.data.get("loaded_province_id"))
        loaded_district_id = self.single_id_validate('loaded_district_id',self.data.get("loaded_district_id"))
        destination_province_id = self.single_id_validate('destination_province_id',self.data.get("destination_province_id"))
        destination_district_id = self.single_id_validate('destination_district_id',self.data.get("destination_district_id"))
        description = self.description_validate('description',self.data.get("description"))

        return {
            "status_id":status_id,
            "vehicle_id":vehicle_id,
            "driver_id":driver_id,
            "courier_id":courier_id,
            "loaded_province_id":loaded_province_id,
            "loaded_district_id":loaded_district_id,
            "destination_province_id":destination_province_id,
            "destination_district_id":destination_district_id,
            "description":description
        }
    
class UpdateTripStatusValidator(BaseValidator):
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
            raise ValueError("at least one field provided for update")

class UpdateTripValidator(BaseValidator):
    def __init__(self,trip_id:int,**kwargs):
        self.trip_id = trip_id
        self.status_id = kwargs.get("status_id")
        self.vehicle_id = kwargs.get("vehicle_id")
        self.driver_id = kwargs.get("driver_id")
        self.courier_id = kwargs.get("courier_id")
        self.loaded_province_id = kwargs.get("loaded_province_id")
        self.loaded_district_id = kwargs.get("loaded_district_id")
        self.destination_province_id = kwargs.get("destination_province_id")
        self.destination_district_id = kwargs.get("destination_district_id")
        self.started_at = kwargs.get("started_at")
        self.ended_at = kwargs.get("ended_at")
        self.description = kwargs.get("description")
        self.is_active = kwargs.get("is_active")

    def validate(self):
        self.single_id_validate('trip_id',self.trip_id)
        self._check_updatable_fields()

        data = {}

        if self.status_id is not None:
            self.single_id_validate('status_id',self.status_id)
            data["status_id"] = self.status_id
        if self.vehicle_id is not None:
            self.single_id_validate('vehicle_id',self.vehicle_id)
            data["vehicle_id"] = self.vehicle_id
        if self.driver_id is not None:
            self.single_id_validate('driver_id',self.driver_id)
            data["driver_id"] = self.driver_id
        if self.courier_id is not None:
            self.single_id_validate('courier_id',self.courier_id)
            data["courier_id"] = self.courier_id
        if self.loaded_province_id is not None:
            self.single_id_validate('loaded_province_id',self.loaded_province_id)
            data["loaded_province_id"] = self.loaded_province_id
        if self.loaded_district_id is not None:
            self.single_id_validate('loaded_district_id',self.loaded_district_id)
            data["loaded_district_id"] = self.loaded_district_id
        if self.destination_province_id is not None:
            self.single_id_validate('destination_province_id',self.destination_province_id)
            data["destionation_province_id"] = self.destination_province_id
        if self.destination_district_id is not None:
            self.single_id_validate('destination_district_id',self.destination_district_id)
            data["destination_district_id"] = self.destination_district_id
        if self.started_at is not None:
            self.date_validate('started_at',self.started_at)
            data["started_at"] = self.started_at
        if self.ended_at is not None:
            self.date_validate('ended_at',self.ended_at)
            data["ended_at"] = self.ended_at
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
            self.vehicle_id,
            self.driver_id,
            self.courier_id,
            self.loaded_province_id,
            self.loaded_district_id,
            self.destination_province_id,
            self.destination_district_id,
            self.started_at,
            self.ended_at,
            self.description,
            self.is_active
        ]

        if not any(v is not None for v in updatable_fields):
            raise ValueError("at least one field provided for update")