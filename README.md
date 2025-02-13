# 🔥 Fireworks AI KYC Identity Verification PoV

An end-to-end Proof-of-Value solution for identity document verification using Fireworks AI's multimodal LLMs. Automates KYC processes for Financial Services Institutions (FSI) by extracting structured data from passports and driver's licenses.

**Live Demo**: [https://fireworks-ai.onrender.com/](https://fireworks-ai.onrender.com/)  
*(Note: May take 30-60 seconds to wake up if inactive)*

## 🚀 Features

- **Document Type Support**
  - Passports (JPEG/PNG)
  - Driver's Licenses (JPEG/PNG)
  
- **Core Capabilities**
  - Auto-caching of processed documents
  - JSON schema validation with Pydantic
  - Dark mode UI with Streamlit
  - Local JSON storage for PoV testing

- **AI Integration**
  - Fireworks AI's Llama 3.2 11B Vision model
  - Structured JSON output mode
  - Serverless inference endpoints

## ⚙️ Installation

### Prerequisites
- Python 3.8+
- Fireworks AI API key ([Get here](https://fireworks.ai/account/api-keys))

### Quick Start
```bash
# Clone repository
git clone https://github.com/Rofy-Ray/fireworks-ai.git
cd fireworks-ai

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment
echo "FIREWORKS_API_KEY=your-api-key-here" > .env

# Launch application
streamlit run app.py
```

## 📂 Project Structure
```
fireworks-ai/
├── app.py                 # Main Streamlit application
├── utils/                 # Utility functions
│   ├── fireworks_client.py # Fireworks API integration
│   └── layout.py          # Response formatting utilities
├── data/                  # Processed document storage
│   ├── passports/         # JSON outputs for passport scans
│   └── licenses/          # JSON outputs for driver's licenses
├── .env                   # API key configuration
├── requirements.txt       # Python dependencies
└── README.md              # This document
```

## 🔍 Usage Guide
- Select Document Type
    - Choose between passport or driver's license verification
- Upload Document Image
    - Supported formats: JPG, JPEG, PNG (max 200MB)
- View Results
    - First-time upload: AI processing (3-5 sec)
    - Repeat upload: Instant cached results
    - Output includes key fields in formatted layout
- Data Storage
    - Processed documents stored in:
        - `data/passports/*.json` for passports
        - `data/licenses/*.json` for driver's licenses

## 🛡️ Security Note
This PoV implementation:
- Does NOT encrypt stored JSON data
- Uses ephemeral storage only
- Requires proper security implementation for production use
- Should not be used with real customer data

## 🚨 Disclaimer
This Proof-of-Value (PoV) implementation is for demonstration purposes only. It is not intended for production use and should not be used with real customer data. Always conduct thorough security reviews before deploying AI solutions in regulated environments.
