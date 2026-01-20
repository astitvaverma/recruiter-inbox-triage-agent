# Recruiter Inbox Triage Agent - Setup Guide

## 🎯 What This Agent Does

An AI mobile agent that:
- Opens Gmail on your Android device
- Reads unread emails
- Classifies them (New Candidate, Follow-up, Interview Response, Spam)
- Applies Gmail labels automatically
- Stars urgent emails
- Drafts professional replies (without sending)

---

## 📋 Prerequisites

### 1. **Python Installation**
- Python 3.11 or higher
- Check: `python --version`

### 2. **Android Device Setup**
You need **ONE** of these:

#### Option A: Android Emulator (Recommended for Testing)
1. Install **Android Studio** from https://developer.android.com/studio
2. Open Android Studio → Tools → AVD Manager
3. Create a new Virtual Device (e.g., Pixel 5, Android 11+)
4. Start the emulator

#### Option B: Physical Android Phone
1. Enable **Developer Options**:
   - Go to Settings → About Phone
   - Tap "Build Number" 7 times
2. Enable **USB Debugging**:
   - Settings → Developer Options → USB Debugging (ON)
3. Connect phone to laptop via USB cable
4. Accept the "Allow USB Debugging" prompt on your phone

### 3. **ADB (Android Debug Bridge)**
ADB is required to communicate with your Android device.

#### Install ADB on Windows:
```powershell
# Option 1: Via Android Studio (comes bundled)
# ADB will be at: C:\Users\<YourName>\AppData\Local\Android\Sdk\platform-tools\

# Option 2: Standalone ADB
# Download from: https://developer.android.com/tools/releases/platform-tools
# Extract and add to PATH
```

#### Verify ADB Installation:
```powershell
adb --version
```

If not found, add to PATH:
```powershell
# Add this to your PATH environment variable:
C:\Users\royvi\AppData\Local\Android\Sdk\platform-tools
```

---

## 🚀 Installation Steps

### Step 1: Verify Droidrun Installation
```powershell
cd c:\Users\royvi\Desktop\droidrun
python -c "import droidrun; print(droidrun.__version__)"
```
Expected output: `0.4.22`

### Step 2: Install OpenAI Package
```powershell
pip install llama-index-llms-openai openai python-dotenv
```

### Step 3: Set Up OpenAI API Key
You need an OpenAI API key to use GPT-4o-mini.

1. Get your API key from: https://platform.openai.com/api-keys
2. Create a `.env` file in the project directory:

```powershell
# Create .env file
echo OPENAI_API_KEY=your-api-key-here > .env
```

Or set it as an environment variable:
```powershell
$env:OPENAI_API_KEY="sk-your-actual-api-key-here"
```

### Step 4: Connect Your Android Device
```powershell
# Check if device is connected
adb devices
```

Expected output:
```
List of devices attached
emulator-5554   device
# OR
ABC123XYZ       device
```

If you see "unauthorized", check your phone and accept the USB debugging prompt.

---

## ▶️ Running the Agent

### Basic Run:
```powershell
cd c:\Users\royvi\Desktop\droidrun
python gmail_recruiter_agent.py
```

### What Happens:
1. Agent connects to your Android device
2. Opens Gmail app
3. Navigates to inbox
4. Reads unread emails one by one
5. Classifies each email
6. Applies labels and stars
7. Drafts replies
8. Stops when all emails are processed

---

## 🧪 Testing Without Gmail

If you want to test the setup first without Gmail:

```python
# test_agent.py
import asyncio
from droidrun import DroidAgent, load_llm

async def main():
    llm = load_llm("OpenAI", model="gpt-4o-mini", temperature=0.2)
    
    agent = DroidAgent(
        goal="Open the Settings app and navigate to About Phone",
        llms=llm
    )
    
    result = await agent.run()
    print(f"Success: {result.success}")
    print(f"Reason: {result.reason}")

asyncio.run(main())
```

---

## 🎬 Recording a Demo Video

For the hackathon submission, you need a demo video:

### Using OBS Studio (Free):
1. Download: https://obsproject.com/
2. Add "Display Capture" source
3. Position your Android emulator/phone screen
4. Click "Start Recording"
5. Run the agent
6. Stop recording when done
7. Save as MP4

### Using Windows Game Bar:
1. Press `Win + G`
2. Click the record button
3. Run the agent
4. Stop recording
5. Video saved to: `C:\Users\royvi\Videos\Captures\`

---

## 🐛 Troubleshooting

### Issue: "adb not found"
**Solution**: Install Android SDK Platform Tools and add to PATH

### Issue: "No devices found"
**Solution**: 
- Check USB cable connection
- Enable USB Debugging on phone
- Run `adb kill-server` then `adb start-server`

### Issue: "OPENAI_API_KEY not set"
**Solution**: 
```powershell
$env:OPENAI_API_KEY="sk-your-key-here"
```

### Issue: "Gmail not opening"
**Solution**: 
- Make sure Gmail is installed on the device
- Sign in to Gmail manually first
- Grant necessary permissions

### Issue: Agent is too slow
**Solution**: 
- Reduce `max_steps` in config
- Use faster LLM model
- Test with fewer emails first

---

## 📊 Monitoring Agent Progress

The agent will print logs to console:
```
🚀 Running DroidAgent to achieve goal: ...
🔄 Step 1/30
📝 Initializing Manager and Executor Agents...
⚡ Running Executor for action...
✅ DroidAgent initialized successfully.
```

Watch your Android screen to see the agent in action!

---

## 🎯 Next Steps for Hackathon

1. **Test the agent** with a few test emails
2. **Record a demo video** (1-3 minutes)
3. **Create a GitHub repository** with:
   - `gmail_recruiter_agent.py`
   - `prompts/classification_rules.txt`
   - `README.md` (with problem statement, features, how to run)
   - `requirements.txt`
   - `demo/demo.mp4` (your video)
4. **Submit before Jan 19, 11:59 PM IST**

---

## 💡 Tips for Better Results

1. **Start with 5-10 test emails** in your inbox
2. **Use clear email subjects** for better classification
3. **Monitor the first run** to see how it behaves
4. **Adjust classification rules** in `prompts/classification_rules.txt` if needed
5. **Lower temperature** (0.1) for more consistent classification

---

## 📞 Need Help?

- Droidrun Docs: https://docs.droidrun.ai
- Discord: https://discord.gg/ZZbKEZZkwK
- GitHub Issues: https://github.com/droidrun/droidrun/issues

Good luck with the hackathon! 🚀
