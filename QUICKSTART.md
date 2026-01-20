# Quick Start - Run in 5 Minutes

## 1️⃣ Install ADB (Android Debug Bridge)

### Download Standalone ADB:
1. Go to: https://developer.android.com/tools/releases/platform-tools
2. Download "SDK Platform-Tools for Windows"
3. Extract the ZIP file
4. Add to PATH or note the location

### Add to PATH (Optional but Recommended):
```powershell
# Press Win + X → System → Advanced System Settings → Environment Variables
# Edit "Path" variable and add:
C:\path\to\platform-tools
```

## 2️⃣ Set Up Android Device

### Option A: Use Android Emulator
1. Download **BlueStacks** (easiest): https://www.bluestacks.com/
   - OR use **Android Studio** emulator
2. Install and launch
3. Enable ADB in BlueStacks:
   - Settings → Advanced → Enable Android Debug Bridge (ADB)

### Option B: Use Your Phone
1. Settings → About Phone → Tap "Build Number" 7 times
2. Settings → Developer Options → Enable "USB Debugging"
3. Connect phone to laptop via USB
4. Accept "Allow USB Debugging" on phone

## 3️⃣ Verify Connection

```powershell
cd c:\Users\royvi\Desktop\droidrun

# Check if ADB works
adb devices
```

You should see:
```
List of devices attached
emulator-5554   device
```

## 4️⃣ Install Dependencies

```powershell
pip install llama-index-llms-openai openai python-dotenv
```

## 5️⃣ Set OpenAI API Key

```powershell
# Set for current session
$env:OPENAI_API_KEY="sk-your-actual-openai-api-key"

# OR create .env file
echo OPENAI_API_KEY=sk-your-key-here > .env
```

Get your API key from: https://platform.openai.com/api-keys

## 6️⃣ Run the Agent!

```powershell
python gmail_recruiter_agent.py
```

## 🎥 What You'll See:

1. Console shows: "Loading LLM..." → "Running Agent..."
2. Your Android device/emulator screen will show:
   - Gmail opening automatically
   - Emails being opened one by one
   - Labels being applied
   - Stars appearing on urgent emails
   - Reply drafts being created

## ⚠️ Common Issues:

### "adb not found"
```powershell
# Use full path to adb
C:\path\to\platform-tools\adb.exe devices
```

### "No devices attached"
- Restart emulator/phone
- Run: `adb kill-server` then `adb start-server`
- Check USB cable

### "OPENAI_API_KEY not set"
```powershell
$env:OPENAI_API_KEY="sk-..."
```

### Gmail not installed
- Install Gmail from Play Store on your emulator/phone
- Sign in manually first

## 🎬 Record Demo for Hackathon:

1. Press `Win + G` (Windows Game Bar)
2. Click record button
3. Run the agent
4. Show the inbox before and after
5. Stop recording
6. Video saved to: `C:\Users\royvi\Videos\Captures\`

---

**That's it! You're ready to go! 🚀**

For detailed troubleshooting, see `SETUP_GUIDE.md`
