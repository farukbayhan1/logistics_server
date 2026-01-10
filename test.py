from app.validators.order_validator import CreateOrderValidator


data = {
    "order_document_id":1,
    "in_warehouse":True,
    "in_position":False,
    "is_active":True,
    "warehouse_id":1
}

print(CreateOrderValidator(data).validate())
