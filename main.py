import io
import os
import sys
import logging
import json
import base64
import random

# --- 1. SETUP LOGGING ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("RetailGen")

# --- 2. IMPORT LIBRARIES ---
try:
    import numpy as np
    import cv2
    import requests
    import google.generativeai as genai
    from fastapi import FastAPI, Form, UploadFile, File, Response
    from fastapi.middleware.cors import CORSMiddleware
    from PIL import Image
    from rembg import remove
    import easyocr
    logger.info("✅ All libraries imported successfully.")
except ImportError as e:
    logger.error(f"❌ CRITICAL ERROR: Missing library. {e}")
    sys.exit(1)

# --- 3. API KEY SETUP ---
GEMINI_API_KEY = "Pls enter your key here" 

try:
    genai.configure(api_key=GEMINI_API_KEY)
    # We use the library ONLY for text (Headlines)
    text_model = genai.GenerativeModel('gemini-1.5-flash')
    logger.info("✅ Google Text Model Configured")
except Exception as e:
    logger.error(f"⚠️ Gemini Config Error: {e}")

# --- 4. APP SETUP ---
app = FastAPI(title="RetailGen Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OCR
try:
    reader = easyocr.Reader(['en'], gpu=False) 
except:
    reader = None

# --- 5. ENDPOINTS ---

@app.get("/")
def home():
    return {"status": "Online", "message": "Backend is running"}

@app.post("/check-compliance")
async def check_compliance(file: UploadFile = File(...)):
    if not reader:
        return {"status": "FAIL", "violations": ["Server Error: OCR not loaded"]}
    try:
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        img_height, img_width, _ = image.shape
        violations = []
        text_results = reader.readtext(image, detail=0)
        
        BANNED = {"Competition": ["win", "prize"], "Financial": ["money-back", "guarantee"], "Urgency": ["now", "hurry"]}
        
        for text in text_results:
            t_lower = text.lower()
            for cat, words in BANNED.items():
                for w in words:
                    if w in t_lower: violations.append(f"{cat} Violation: '{w}'")

        if img_height / img_width > 1.5:
            if reader.readtext(image[0:200, :], detail=0): violations.append("Header Violation")
            if reader.readtext(image[img_height-250:, :], detail=0): violations.append("Footer Violation")

        if violations: return {"status": "FAIL", "violations": violations}
        return {"status": "PASS", "message": "Compliant"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/tools/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        input_image = Image.open(io.BytesIO(contents))
        output_image = remove(input_image)
        img_byte_arr = io.BytesIO()
        output_image.save(img_byte_arr, format='PNG')
        return Response(content=img_byte_arr.getvalue(), media_type="image/png")
    except Exception as e:
        return {"status": "error", "message": str(e)}

# --- 🌟 THE SMART GENERATOR ---
@app.post("/tools/generate-bg")
async def generate_bg(prompt: str = Form(...)):
    print(f"🎨 [REQUEST] {prompt}")

    # 1. OPTIMIZE PROMPT (Gemini Text)
    # Even if Image gen is blocked, Text gen usually works
    final_prompt = prompt
    try:
        res = text_model.generate_content(f"Refine this into a photography prompt (max 15 words): {prompt}")
        if res.text: final_prompt = res.text.strip()
    except: pass

    # 2. TRY GOOGLE IMAGEN (DIRECT API)
    # This bypasses the 'AttributeError' by using raw HTTP
    url = f"https://generativelanguage.googleapis.com/v1beta/models/imagen-3.0-generate-001:predict?key={GEMINI_API_KEY}"
    headers = {"Content-Type": "application/json"}
    payload = {"instances": [{"prompt": final_prompt}], "parameters": {"sampleCount": 1, "aspectRatio": "3:4"}}

    try:
        print("⚡ Attempting Google Imagen 3...")
        response = requests.post(url, headers=headers, json=payload)
        
        if response.status_code == 200:
            # SUCCESS!
            result = response.json()
            b64_data = result['predictions'][0]['bytesBase64Encoded']
            image_data = base64.b64decode(b64_data)
            print("✅ [GOOGLE] Success")
            return Response(content=image_data, media_type="image/jpeg")
        else:
            print(f"❌ [GOOGLE BLOCK] {response.status_code}. Switching to Fallback...")
    except Exception as e:
        print(f"❌ [GOOGLE ERROR] {e}")

    # 3. FALLBACK: STABLE DIFFUSION (SDXL TURBO)
    # If Google blocks you, this runs automatically.
    # This is NOT Flux. It is Stable Diffusion.
    try:
        print("🔄 Falling back to Stable Diffusion (SDXL)...")
        seed = random.randint(1, 99999)
        safe_prompt = requests.utils.quote(final_prompt)
        # using model=turbo (SDXL Turbo)
        url = f"https://image.pollinations.ai/prompt/{safe_prompt}?width=768&height=1152&seed={seed}&nologo=true&model=turbo"
        
        img_res = requests.get(url, timeout=20)
        if img_res.status_code == 200:
            print("✅ [SDXL] Success")
            return Response(content=img_res.content, media_type="image/jpeg")
    except:
        pass

    return {"status": "error", "message": "Google blocked the request and fallback failed."}

@app.post("/tools/generate-copy")
async def generate_copy(product_name: str = Form(...)):
    try:
        prompt = f"Write 3 short, punchy 3-word ads for: {product_name}. Separated by commas."
        res = text_model.generate_content(prompt)
        headlines = [h.strip() for h in res.text.split(',')]
        return {"status": "success", "headlines": headlines[:3]}
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
