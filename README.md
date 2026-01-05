# 🧠 RetailGen Studio  
**AI-Powered Retail Media Creative Builder with Compliance Enforcement**

RetailGen Studio is an AI-driven creative tool that enables advertisers to design, validate, and export professional retail media creatives that comply with strict retailer and brand guidelines. It combines a visual editor with AI-based image generation, background removal, and a compliance engine that automatically enforces rules such as safe-zones, banned copy, and layout constraints.

---

## 🚀 What This Solves

Retail media creatives must follow complex rules (no prices, no claims, safe-zones, branding rules, accessibility). Today this is done manually or via agencies.  
RetailGen Studio turns these guidelines into executable AI rules, allowing advertisers to create compliant creatives in minutes without rejections or rework.

---

## ✨ Core Features

- Visual creative builder (drag, resize, text, layers)
- AI background generation (Flux via Pollinations)
- Background removal (rembg)
- Multi-format canvas (9:16, 1:1, 16:9, 1.9:1, custom)
- Retailer compliance engine using OCR + rules
- Safe-zone enforcement for Instagram/Facebook Stories
- Auto-fix layout violations
- Compliance-locked exports (SD, HD, 4K)

---

## 🧩 System Architecture

**Frontend**
- Next.js  
- Fabric.js (canvas editor)

**Backend**
- FastAPI  
- EasyOCR (text detection)  
- OpenCV (image analysis)  
- Regex-based compliance engine  

**AI**
- Flux (AI backgrounds)  
- rembg (background removal)

---

## 📦 Repository Structure

```
/backend
  ├── main.py          # FastAPI server
  ├── requirements.txt
/frontend
  ├── app/page.tsx     # Main Fabric.js canvas UI
  ├── components/
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/retailgen-studio.git
cd retailgen-studio
```

---

### 2️⃣ Backend Setup (FastAPI)

```bash
cd backend
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
cd frontend
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
2. Select creative format (Story, Square, etc.)  
3. Upload a product image  
4. Remove background if needed  
5. Generate an AI background  
6. Add text and adjust layout  
7. Click **Check Compliance**  
8. If violations appear, use **Auto-Fix**  
9. When compliant, download the final creative  

---

## 🔐 Compliance Rules Enforced

The system enforces retailer rules such as:

- No prices, discounts, claims, sustainability, charity, competitions  
- Tesco-approved tag text only  
- Mandatory safe-zones for 9:16 stories  
- Text placement rules  
- OCR-based copy detection  
- Accessibility and contrast checks (extendable)  

All creatives are blocked from export unless compliant.

---

## 📤 Exporting

Exports are:
- Locked until compliance passes  
- Auto-compressed under 500KB  
- Available in SD, HD, and 4K  
- Generated as JPG  

---

## 📈 Scalability

The rule engine is modular and supports:
- Multiple retailers  
- Different guideline sets  
- High user volumes  
- Multi-brand deployments  

---

## 🧠 Future Improvements

- Brand-aware AI layouts  
- Campaign-level generation  
- Performance-optimized creatives  
- Multi-user review workflows  
- Retailer API integration  

---

## 🏁 Conclusion

RetailGen Studio transforms retail advertising from a manual, error-prone process into an AI-powered, compliance-safe creative pipeline — enabling any advertiser to launch professional, retailer-ready campaigns at scale.
