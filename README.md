# 🧠 RetailGen Studio  
**AI-Powered Retail Media Creative Builder with Compliance Enforcement**

RetailGen Studio is an AI-driven retail media creative tool that allows advertisers to design, validate, and export professional, multi-format ad creatives while automatically enforcing retailer and brand compliance rules.

The platform combines a browser-based visual editor with AI-powered image generation, background removal, and an OCR-based compliance engine that prevents illegal or rejected creatives from being exported.

---

## 🚀 What This Solves

Retail media advertising platforms enforce strict rules such as:
- No prices, discounts, claims, or sustainability messaging  
- Mandatory safe-zones for social ads  
- Specific branding and tag requirements  
- Accessibility and layout constraints  

These rules are difficult and expensive to enforce manually.  
RetailGen Studio converts these guidelines into executable AI rules so users can design freely while staying compliant.

---

## ✨ Core Features

- Drag-and-drop creative editor (Fabric.js)
- AI background generation (Flux via Pollinations)
- Background removal (rembg)
- Multi-format canvas (9:16, 1:1, 16:9, 1.9:1, custom)
- OCR-based compliance checking
- Safe-zone enforcement for Instagram & Facebook Stories
- Automatic layout fixing
- Compliance-locked export system (SD / HD / 4K)

---

## 🧩 System Architecture

### Frontend
- Next.js (App Router)
- Fabric.js canvas editor
- Tailwind / CSS for UI
- Runs in `retail-gen-frontend/`

### Backend
- FastAPI (`main.py`)
- EasyOCR for text detection
- OpenCV for image analysis
- Regex-based compliance engine
- rembg for background removal
- Flux AI for background generation

---

## 📁 Project Structure

```
Retail-Hackathon/
├── main.py                  # FastAPI backend
├── requirements.txt         # Python dependencies
├── .env                     # API keys / environment variables
├── venv/                    # Python virtual environment
├── retail-gen-frontend/     # Next.js frontend
│   ├── app/
│   ├── public/
│   ├── package.json
│   ├── next.config.ts
│   └── ...
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/blackcat21-sys/tesco-retail
cd retailgen-studio
```

---

### 2️⃣ Backend Setup (FastAPI)

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend will run at:
```
http://127.0.0.1:8000
```

---

### 3️⃣ Frontend Setup (Next.js)

```bash
cd retail-gen-frontend
npm install
npm run dev
```

Frontend will run at:
```
http://localhost:3000
```

---

## 🧪 How to Use

1. Open `http://localhost:3000`
2. Choose a creative format (Story, Square, etc.)
3. Upload a product image
4. Remove its background if needed
5. Generate an AI background
6. Add text and adjust layout
7. Click **Check Compliance**
8. If violations appear, use **Auto-Fix**
9. When compliant, download the final creative

---

## 🔐 Compliance Rules Enforced

The system detects and blocks:

- Prices, discounts, and offers  
- Sustainability and green claims  
- Charity references  
- Competitions and giveaways  
- Money-back or guarantee claims  
- Invalid retailer tags  
- Text inside social safe-zones  

Rules are enforced using OCR, regex, and image layout analysis.

---

## 📤 Export System

- Export is locked until compliance passes  
- Files are auto-compressed under 500KB  
- Available in SD, HD, and 4K  
- Generated as JPG  

---

## 📈 Scalability

RetailGen Studio supports:
- Multiple retailers
- Different guideline sets
- High user volume
- Multi-brand creative generation

New retailers can be added by updating rule sets without changing the UI.

---

## 🧠 Future Enhancements

- Brand-aware AI layouts
- Auto-generated campaign sets
- Collaborative review workflows
- Performance-optimized creatives
- Retailer API integration

---

## 🏁 Conclusion

RetailGen Studio transforms retail advertising from a manual, error-prone process into an AI-powered, compliance-safe creative pipeline — enabling advertisers to launch campaign-ready creatives in minutes with zero rejection risk.
