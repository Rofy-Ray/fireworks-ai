import streamlit as st
import json
import os
import base64
from datetime import date
from pathlib import Path
from utils.fireworks_client import extract_kyc_data
from utils.layout import format_kyc_data

st.set_page_config(
    page_title="Fireworks AI KYC Demo",
    page_icon="🔒",
    layout="centered"
)

st.markdown("""
<style>
    .stApp { background-color: #1a1a1a; color: #ffffff; }
    .stFileUploader section { background-color: #2d2d2d; }
</style>
""", unsafe_allow_html=True)

def save_output(document_type: str, filename: str, data: dict):
    output_dir = Path("data") / ("passports" if document_type == "passport" else "licenses")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_path = output_dir / f"{Path(filename).stem}.json"
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
        
def load_existing_data(document_type: str, filename: str):
    output_dir = Path("data") / ("passports" if document_type == "passport" else "licenses")
    output_path = output_dir / f"{Path(filename).stem}.json"
    
    if output_path.exists():
        with open(output_path) as f:
            return json.load(f)
    return None

def encode_image(uploaded_file):
    return base64.b64encode(uploaded_file.getvalue()).decode("utf-8")

def main():
    st.title("Fireworks AI KYC Verification")
    
    doc_type = st.radio("Select Document Type:", 
                    ["passport", "license"], 
                    format_func=lambda x: "Passport" if x == "passport" else "Driver's License",
                    horizontal=True)
    
    uploaded_file = st.file_uploader(
        "Upload Document Image",
        type=["jpg", "jpeg", "png"],
        disabled=(doc_type is None)
    )
    
    if uploaded_file:
        existing_data = load_existing_data(doc_type.lower(), uploaded_file.name)
        
        if existing_data:
            st.success("✅ Previously processed document - loaded cached results")
            st.markdown("### Document Details")
            formatted_text = format_kyc_data(existing_data, doc_type)
            st.markdown(formatted_text)
            return
            
        with st.spinner("🔍 Analyzing document..."):
            try:
                image_b64 = encode_image(uploaded_file)
                raw_response = extract_kyc_data(doc_type.lower(), image_b64)
                raw_data = json.loads(raw_response)
                
                save_output(doc_type.lower(), uploaded_file.name, raw_data)
                
                st.success("✅ Document verified successfully")
                st.markdown("### Document Details")
                formatted_text = format_kyc_data(raw_data, doc_type)
                st.markdown(formatted_text)
                
            except Exception as e:
                st.error(f"❌ Validation error: {str(e)}")
                st.stop()

if __name__ == "__main__":
    main()