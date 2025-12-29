
class BaseValidator:

    def type_name_validator(self,data:dict):

        if "type_name" not in data:
            raise ValueError("type name required")
        
        raw_type_name = data.get("type_name")
        if not isinstance(raw_type_name,str):
            raise ValueError("type name must be a string")
        
        type_name = raw_type_name.strip().lower()
        if not type_name:
            raise ValueError("type name can not be empty")
        if len(type_name) < 2:
            raise ValueError("type name can not be smaller than 2 characters")
        if not type_name.replace(" ","").isalpha():
            raise ValueError("type name can not contain numeric characters")
        
        description = self.description_validate()

        return {
            "type_name":type_name,
            "description":description
        }
    
    def single_id_validate(self,field_name:str,value):
        
        if value is None:
            raise ValueError(f"{field_name}: can not be empty")
        if isinstance(value,bool) or not isinstance(value,int):
            raise ValueError(f"{field_name}: must be an integer")
        if value <= 0:
            raise ValueError(f"{field_name}: must be greater than zero")
        
        return value

    def description_validate(self,field_name:str,value):

        if value is None:
            return None
        
        if not isinstance(value,str):
            raise ValueError(f"{field_name}: must be a string")
        
        value = value.strip()
        if len(value) < 2:
            raise ValueError(f"{field_name}: can not be smaller than 2 characters")

        return value
    
    def text_validate(self,field_name,value):
        
        if value is None:
            raise ValueError(f"{field_name}: can not be empty")
        if not isinstance(value,str):
            raise ValueError(f"{field_name}: must be a string")
        
        value = value.strip()
        if len(value) < 2:
            raise ValueError(f"{field_name}: can not be smaller than 2 characters")
        
        return value