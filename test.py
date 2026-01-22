from app.validators.order_validator import CreateOrderValidator


data = {
    "order_document_id":1,
    "in_warehouse":True,
    "in_position":False,
    "is_active":True,
    "warehouse_id":1,
    "order_plan_confirmation_date":"2025-01-01",
    "box_count":2
}

print(CreateOrderValidator(data).validate())
