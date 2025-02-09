import os
from openai import OpenAI
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("FIREWORKS_API_KEY"), base_url="https://api.fireworks.ai/inference/v1")

class PassportData(BaseModel):
    full_name: str
    date_of_birth: date
    sex: str = Field(pattern="^(Male|Female|Other)$")
    nationality: str
    passport_number: str = Field(min_length=6)
    issuing_date: date
    expiration_date: date
    place_of_birth: str
    issuing_country: str

class LicenseData(BaseModel):
    full_name: str
    date_of_birth: date
    sex: str = Field(pattern="^(Male|Female|Other)$")
    height: str 
    hair_color: str
    eyes_color: str
    address: str
    license_number: str = Field(min_length=6)
    issuing_date: date
    expiration_date: date
    issuing_state: Optional[str] = None
    issuing_country: str

def extract_kyc_data(document_type: str, image_b64: str):
    schema = PassportData.model_json_schema() if document_type == "passport" else LicenseData.model_json_schema()
    prompt = f"""
    You are an AI-powered Identity Verification Specialist. 
    Extract all relevant fields from this {document_type} document, simulating human-level accuracy in Optical Character Recognition (OCR). 
    Focus on capturing data essential for Know Your Customer (KYC) processes, including identification numbers, names, addresses, dates, and other critical information. 
    Return the extracted data in JSON format using this schema: {schema}.
    """
    
    response = client.chat.completions.create(
        model="accounts/fireworks/models/llama-v3p2-11b-vision-instruct",
        response_format={"type": "json_object", "schema": schema},
        messages=[{
            "role": "user",
            "content": [{
                "type": "text",
                "text": prompt
            }, {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{image_b64}"
                }
            }]
        }]
    )
    
    return response.choices[0].message.content