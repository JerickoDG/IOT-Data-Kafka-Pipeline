from datetime import datetime as dt

# Mapping source fields to DB columns
FIELD_MAPPING = {
    "field1": "temperature",
    "field2": "humidity",
    "field3": "atmospheric_pressure",
    "field4": "gas",
    "field5": "wind_speed",
    "field6": "precipitation",
    "field7": "wind_direction",
    "field8": "uv"
}

def transform_iot_data(raw_data: dict) -> dict:
    transformed = {}

    created_at_str = raw_data.get("created_at")
    if created_at_str:
        transformed["created_at"] = dt.fromisoformat(created_at_str.replace("Z", "+00:00"))
    
    for src_field, db_field in FIELD_MAPPING.items():
        value = raw_data.get(src_field)
        if value is not None:
            try:
                transformed[db_field] = float(value)
            except ValueError:
                transformed[db_field] = None
        else:
            transformed[db_field] = None
    
    return transformed