# BlueStacks ADB Setup - Quick Steps

## You're at this step now! ✅ BlueStacks is installed

### Step 1: Launch BlueStacks
Click the "Launch" button you see in the popup

### Step 2: Enable ADB in BlueStacks

1. **Look for the hamburger menu (☰)** in the top-right corner of BlueStacks
   - It might also be a gear icon ⚙️

2. **Click Settings**

3. **Go to "Advanced" tab**

4. **Find "Android Debug Bridge (ADB)"**
   - Toggle it **ON**
   - Note: Port is usually **5555**

5. **Click "Restart Now"** or "Save"

6. **Wait for BlueStacks to restart** (30 seconds)

---

## Step 3: Install ADB Tools (If not done yet)

You still need ADB command-line tools on your laptop.

### Quick Install:

1. **Download ADB Platform Tools**:
   - Go to: https://developer.android.com/tools/releases/platform-tools
   - Click "Download SDK Platform-Tools for Windows"
   - Save the ZIP file

2. **Extract**:
   - Right-click the downloaded ZIP
   - Extract to: `C:\adb\`
   - Final path: `C:\adb\platform-tools\`

3. **Add to PATH**:
   - Press `Win + X` → System
   - Advanced system settings
   - Environment Variables
   - Edit "Path" (System variables)
   - Add: `C:\adb\platform-tools`
   - Click OK on all windows

4. **Restart PowerShell** (important!)

---

## Step 4: Connect ADB to BlueStacks

Open PowerShell and run:

```powershell
# Connect to BlueStacks
adb connect localhost:5555
```

Expected output:
```
connected to localhost:5555
```

Then verify:
```powershell
adb devices
```

Expected output:
```
List of devices attached
localhost:5555    device
```

✅ **If you see "device" - you're connected!**

---

## Step 5: Install Gmail on BlueStacks

1. **Open Play Store** in BlueStacks
2. **Sign in** with your Google account
3. **Search** for "Gmail"
4. **Install** Gmail
5. **Open Gmail** and sign in

---

## Step 6: Install Python Dependencies

```powershell
cd c:\Users\royvi\Desktop\droidrun
pip install llama-index-llms-openai openai python-dotenv
```

---

## Step 7: Set OpenAI API Key

Create `.env` file:
```powershell
notepad .env
```

Add this line:
```
OPENAI_API_KEY=sk-your-actual-api-key-here
```

Get your key from: https://platform.openai.com/api-keys

---

## Step 8: Run the Agent!

```powershell
python gmail_recruiter_agent.py
```

---

## 🎬 Step 9: Record Demo

1. Press `Win + G`
2. Click record
3. Run the agent
4. Show it working
5. Stop recording

---

## Troubleshooting

### "adb not recognized"
- Make sure you extracted ADB to `C:\adb\platform-tools\`
- Make sure you added it to PATH
- **Restart PowerShell** (very important!)

### Can't connect to BlueStacks
- Make sure ADB is enabled in BlueStacks settings
- Make sure BlueStacks is running
- Try: `adb kill-server` then `adb connect localhost:5555`

### Different port number
If BlueStacks shows a different port (like 5565), use that:
```powershell
adb connect localhost:5565
```

---

## ⏰ Time Check

You have about **8.5 hours** until deadline (11:59 PM IST)

Estimated time remaining:
- ⏱️ 15 min: Enable ADB + install ADB tools
- ⏱️ 15 min: Connect and verify
- ⏱️ 15 min: Install Gmail and dependencies
- ⏱️ 10 min: Set API key
- ⏱️ 20 min: Test run the agent
- ⏱️ 30 min: Record demo
- ⏱️ 30 min: Create GitHub repo
- ⏱️ 30 min: Submit

**Total: ~3 hours** (you have plenty of time!)

---

## Next Immediate Action:

1. ✅ Click "Launch" in BlueStacks popup
2. ⏳ Wait for it to start
3. 📸 Take a screenshot when you see the BlueStacks home screen
4. 🔧 Enable ADB in settings

Let me know when BlueStacks is running and I'll help with the next step!
