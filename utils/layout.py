def format_kyc_data(data: dict, doc_type: str) -> str:
    common_fields = [
        (f"📝 Full Name", "full_name"),
        (f"📅 Date of Birth", "date_of_birth"),
        (f"⚧ Gender", "sex"),
    ]
    
    passport_fields = [
        ("🌍 Nationality", "nationality"),
        ("🔢 Passport Number", "passport_number"),
        ("📍 Place of Birth", "place_of_birth"),
        ("🏛️ Issuing Country", "issuing_country"),
        ("📅 Issue Date", "issuing_date"),
        ("📅 Expiration Date", "expiration_date"),
    ]
    
    license_fields = [
        ("📏 Height", "height"),
        ("👱 Hair Color", "hair_color"),
        ("👁️ Eye Color", "eyes_color"),
        ("🏠 Address", "address"),
        ("🔢 License Number", "license_number"),
        ("🏛️ Issuing State", "issuing_state"),
        ("🌍 Issuing Country", "issuing_country"),
        ("📅 Issue Date", "issuing_date"),
        ("📅 Expiration Date", "expiration_date"),
    ]
    
    fields = common_fields + (passport_fields if doc_type == "passport" else license_fields)
    
    formatted_data = []
    for field in fields:
        label, key = field[0], field[1]
        if key in data:
            value = data[key]
            if len(field) == 3: 
                value = field[2](value)
            formatted_data.append(f"{label}: {value}")
    
    return "\n\n\n".join(formatted_data)