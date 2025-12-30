from .base_validator import BaseValidator

class CreateAddressTypeValidator(BaseValidator):
    def validate(self,data:dict):
        return self.type_name_validator(data)

class CreateAdressActivityTypeValidator(BaseValidator):
    def validate(self,data:dict):
        return self.type_name_validator(data)

class CreateAddressValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data
    
    def validate(self):
        self.type_id = self.single_id_validate('type_id',self.data.get("type_id"))
        self.province_id = self.single_id_validate('province_id',self.data.get("province_id"))
        self.district_id = self.single_id_validate('district_id',self.data.get("district_id"))
        self.address_text = self.text_validate('address_text',self.data.get("address_text"))
        self.description = self.description_validate('description',self.data.get("description"))

        return {
            "type_id":self.type_id,
            "province_id":self.province_id,
            "district_id":self.district_id,
            "address_text":self.address_text,
            "description":self.description
        }
        
class UpdateAddressValidator(BaseValidator):
    def __init__(self,address_id:int,**kwargs):
        self.address_id = address_id
        self.type_id = kwargs.get("type_id")
        self.province_id = kwargs.get("province_id")
        self.district_id = kwargs.get("district_id")
        self.address_text = kwargs.get("address_text")
        self.location = kwargs.get("location")
        self.description = kwargs.get("description")
        self.is_active = kwargs.get("is_active")

    def validate(self):
        self.single_id_validate('address_id',self.address_id)
        self._check_updatable_fields()

        data = {}

        if self.type_id is not None:
            self.single_id_validate('type_id',self.type_id)
            data['type_id'] = self.type_id
        if self.province_id is not None:
            self.single_id_validate('province_id',self.province_id)
            data['province_id'] = self.province_id
        if self.district_id is not None:
            self.single_id_validate('district_id',self.district_id)
            data['district_id'] = self.district_id
        if self.address_text is not None:
            self.text_validate('address_text',self.address_text)
            data['address_text'] = self.address_text
        if self.location is not None:
            self.text_validate('location',self.location)
            data['location'] = self.location
        if self.description is not None:
            self.description_validate('description',self.description)
            data['description'] = self.description
        if self.is_active is not None:
            self.is_active_validate('is_active',self.is_active)
            data['is_active'] = self.is_active
        
        return data

    def _check_updatable_fields(self):
        updatable_fields = [
            self.type_id,
            self.province_id,
            self.district_id,
            self.address_text,
            self.location,
            self.description,
            self.is_active
        ]
        
        if not any(v is not None for v in updatable_fields):
            raise ValueError("at least one field must be provided for update")
    