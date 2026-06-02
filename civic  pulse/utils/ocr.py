import easyocr
import cv2
import os

def process_civic_image(image_path):
    """
    Core OCR engine for Civic Pulse.
    Cleans the image, extracts text, and prints logs directly to the terminal.
    """
    print("\n" + "="*50)
    print(f"⚙️ [CIVIC PULSE ENGINE] Processing: {image_path}")
    print("="*50)

    # 1. Path Safety Verification
    if not os.path.exists(image_path):
        error_msg = f"❌ ERROR: File '{image_path}' not found."
        print(error_msg)
        return error_msg

    # 2. Image Preprocessing for Clean Contrast
    print("📸 Optimizing image layers (Grayscale + Adaptive Thresholding)...")
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    processed_img = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY, 11, 2
    )
    
    # 3. Running Local Engine Extraction
    print("🤖 Scanning text patterns with offline engine...")
    reader = easyocr.Reader(['en'])
    results = reader.readtext(processed_img, detail=0, paragraph=True)
    
    # 4. Compiling Clean String Blocks
    final_text = "\n".join(results)
    
    # 5. Displaying Results Directly to the Terminal Window
    print("\n📝 --- EXTRACTED TEXT TERMINAL DISPLAY ---")
    if final_text.strip():
        print(final_text)
    else:
        print("[System Alert: No readable text detected inside this file]")
    print("------------------------------------------")
    print(f"📊 Extraction Complete. (Total characters parsed: {len(final_text)})")
    print("="*50 + "\n")
    
    return final_text

# ==============================================================================
# INTERACTIVE USER-INPUT BLOCK
# This allows you to type or drag any image file path directly into the terminal.
# ==============================================================================
if __name__ == "__main__":
    print("\n" + "🌟"*15)
    print("  WELCOME TO CIVIC PULSE OCR  ")
    print("🌟"*15)
    
    # Prompt the user to type or drag-and-drop a file path
    user_path = input("👉 Enter the name or full path of the image file: ").strip()
    
    # Clean up quotation marks if the user dragged-and-dropped the file into the terminal
    user_path = user_path.strip("'\"")
    
    if user_path:
        process_civic_image(user_path)
    else:
        print("❌ Error: No file path provided.")