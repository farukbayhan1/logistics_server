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
        started_at = self.date_validate('started_at',self.data.get("started_at"))
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
            "started_at":started_at,
            "description":description
        }
    
class UpdateTripStatusValidator(BaseValidator):
    def __init__(self,trip_id:int,**kwargs):
        self.trip_id = trip_id
        self.status_id = kwargs.get("status_id")
        self.vehicle_id = kwargs.get("vehicle_id")
        

class UpdateTripValidator(BaseValidator):
    pass