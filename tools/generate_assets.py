import requests
import base64
import json
import os
import time

# API Configuration
URL = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
HEADERS = {
    "Authorization": "Bearer sk-0qDxPc8CIZv1Lu27CBqLkIDfrd351tSVz7zy4qeRgIqT7xvZ",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

ASSETS_DIR = "/home/hdc0522/agent-world-mvp/assets"

# Generation prompts
CLASS_PROMPTS = {
    "healer": "anime style, gentle female healer, white robe, magic staff, holy glow effect, soft smile, beautiful anime girl, high quality, detailed illustration, fantasy anime, cel shading",
    "tank": "anime style, powerful female warrior, heavy armor, large shield, metal texture, confident stance, beautiful anime girl, high quality, detailed illustration, fantasy anime, cel shading",
    "dps": "anime style, agile female assassin, dual blades, dark cloak, shadow effect, cool expression, beautiful anime girl, high quality, detailed illustration, fantasy anime, dark atmosphere, cel shading"
}

STAGE_PROMPTS = {
    "kindergarten": "pixel art style, cute kindergarten classroom, colorful toys, small children playing, warm cozy atmosphere, game background, 16-bit style",
    "elementary": "pixel art style, Chinese elementary school classroom, desks and chairs, blackboard, sunshine through window, game background, 16-bit style",
    "middle": "pixel art style, Chinese middle school hallway, lockers, afternoon light, nostalgic atmosphere, game background, 16-bit style",
    "high": "pixel art style, Chinese high school classroom, uniform, textbooks on desk, dramatic lighting, game background, 16-bit style",
    "university": "pixel art style, Chinese university campus, cherry blossoms, campus buildings, youthful atmosphere, game background, 16-bit style",
    "career": "pixel art style, modern office workplace, desk setup, computer, city view window, corporate atmosphere, game background, 16-bit style"
}

EQUIP_PROMPTS = {
    "weapon": "pixel art style, glowing sword icon, RPG item, white quality, simple design, transparent background, game asset, 16-bit style",
    "armor": "pixel art style, chestplate armor icon, RPG item, white quality, simple design, transparent background, game asset, 16-bit style",
    "accessory": "pixel art style, ring accessory icon, RPG item, white quality, simple design, transparent background, game asset, 16-bit style"
}

def generate_image(prompt, width, height, output_path):
    """Generate an image using Stability AI API"""
    payload = {
        "text_prompts": [{"text": prompt, "weight": 1}],
        "width": width,
        "height": height,
        "steps": 25
    }
    
    print(f"Generating: {output_path}")
    print(f"Prompt: {prompt[:80]}...")
    
    try:
        response = requests.post(URL, headers=HEADERS, json=payload, timeout=120)
        
        if response.status_code == 403:
            print(f"  [ERROR] 403 Forbidden - likely non-English prompt or permission issue")
            print(f"  Response: {response.text}")
            return False
        
        if response.status_code != 200:
            print(f"  [ERROR] HTTP {response.status_code}: {response.text[:200]}")
            return False
        
        data = response.json()
        
        if "artifacts" not in data or len(data["artifacts"]) == 0:
            print(f"  [ERROR] No artifacts in response")
            print(f"  Response: {str(data)[:200]}")
            return False
        
        img_data = base64.b64decode(data["artifacts"][0]["base64"])
        with open(output_path, "wb") as f:
            f.write(img_data)
        
        print(f"  [SUCCESS] Saved to {output_path} ({len(img_data)} bytes)")
        return True
        
    except requests.exceptions.Timeout:
        print(f"  [ERROR] Request timeout")
        return False
    except Exception as e:
        print(f"  [ERROR] {type(e).__name__}: {str(e)}")
        return False

def main():
    print("=" * 60)
    print("Agent World Asset Generator")
    print("=" * 60)
    
    results = {"success": [], "failed": []}
    
    # 1. Generate character class portraits (1024x1024)
    print("\n[1] Generating Character Class Portraits (1024x1024)...")
    for name, prompt in CLASS_PROMPTS.items():
        output_path = os.path.join(ASSETS_DIR, f"class_{name}.png")
        if generate_image(prompt, 1024, 1024, output_path):
            results["success"].append(output_path)
        else:
            results["failed"].append(f"class_{name}")
        time.sleep(2)  # Rate limiting
    
    # 2. Generate stage scene images (1024x1024)
    print("\n[2] Generating Stage Scene Images (1024x1024)...")
    for name, prompt in STAGE_PROMPTS.items():
        output_path = os.path.join(ASSETS_DIR, f"stage_{name}.png")
        if generate_image(prompt, 1024, 1024, output_path):
            results["success"].append(output_path)
        else:
            results["failed"].append(f"stage_{name}")
        time.sleep(2)
    
    # 3. Generate equipment icons (512x512)
    print("\n[3] Generating Equipment Icons (512x512)...")
    for name, prompt in EQUIP_PROMPTS.items():
        output_path = os.path.join(ASSETS_DIR, f"equip_{name}.png")
        if generate_image(prompt, 512, 512, output_path):
            results["success"].append(output_path)
        else:
            results["failed"].append(f"equip_{name}")
        time.sleep(2)
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Successful: {len(results['success'])}")
    print(f"Failed: {len(results['failed'])}")
    
    if results["failed"]:
        print(f"Failed items: {results['failed']}")
    
    print("\nGenerated files:")
    for f in sorted(results["success"]):
        print(f"  - {f}")
    
    print("\nAll done!")

if __name__ == "__main__":
    main()