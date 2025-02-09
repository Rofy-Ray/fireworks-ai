# 🔥 Fireworks AI KYC Identity Verification PoV

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Fireworks.ai](https://img.shields.io/badge/Fireworks.ai-FF6F00?style=for-the-badge&logo=firebase&logoColor=white)](https://fireworks.ai)

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
1. Select Document Type
Choose between passport or driver's license verification
2. Upload Document Image
Supported formats: JPG, JPEG, PNG (max 200MB)
3. View Results
- First-time upload: AI processing (10-15 sec)
- Repeat upload: Instant cached results
- Output includes key fields in formatted layout
4. Data Storage
Processed documents stored in:
- `data/passports/*.json` for passports
- `data/licenses/*.json` for driver's licenses

## 🛠️ Development
Prerequisites
- Python 3.8+
- Fireworks AI API key
- Basic Streamlit knowledge

Contribution Guidelines
1. Create feature branch from `main`
2. Add tests for new functionality
3. Update documentation accordingly
4. Submit PR with detailed description

## 🛡️ Security Note
This PoV implementation:
- Does NOT encrypt stored JSON data
- Uses ephemeral storage only
- Requires proper security implementation for production use
- Should not be used with real customer data

## 🚨 Disclaimer
This Proof-of-Value (PoV) implementation is for demonstration purposes only. It is not intended for production use and should not be used with real customer data. Always conduct thorough security reviews before deploying AI solutions in regulated environments.




