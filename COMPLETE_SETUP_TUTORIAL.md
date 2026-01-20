# 🚀 Complete In-Depth Setup Tutorial
## Recruiter Inbox Triage Agent - From Zero to Running

This guide assumes you're starting from scratch with **NO** prior Android development setup.

---

## 📦 PART 1: Install ADB (Android Debug Bridge)

ADB is the tool that lets your laptop control Android devices. You have two options:

### **Option A: Standalone ADB (Recommended - Faster)**

#### Step 1.1: Download ADB Platform Tools

1. **Open your browser** and go to:
   ```
   https://developer.android.com/tools/releases/platform-tools
   ```

2. **Scroll down** to find "Downloads" section

3. **Click on**: "Download SDK Platform-Tools for Windows"
   - File will be named something like: `platform-tools_r35.0.1-windows.zip`
   - Size: ~10-15 MB

4. **Save the file** to your Downloads folder

#### Step 1.2: Extract ADB

1. **Navigate to** your Downloads folder:
   ```
   C:\Users\royvi\Downloads\
   ```

2. **Right-click** on `platform-tools_r35.0.1-windows.zip`

3. **Select** "Extract All..."

4. **Extract to**: `C:\adb\` (create this folder)
   - Final path should be: `C:\adb\platform-tools\`
   - Inside you'll see files like: `adb.exe`, `fastboot.exe`, etc.

#### Step 1.3: Add ADB to System PATH

This allows you to run `adb` from any folder in PowerShell.

1. **Press** `Win + X` → Select "System"

2. **Click** "Advanced system settings" (on the right side)

3. **Click** "Environment Variables..." button (at the bottom)

4. In **"System variables"** section (bottom half):
   - **Find** the variable named `Path`
   - **Click** on it to select it
   - **Click** "Edit..." button

5. In the Edit window:
   - **Click** "New"
   - **Type**: `C:\adb\platform-tools`
   - **Click** "OK"

6. **Click** "OK" on all remaining windows

7. **IMPORTANT**: Close and reopen PowerShell for changes to take effect

#### Step 1.4: Verify ADB Installation

1. **Open a NEW PowerShell window** (Win + X → Windows PowerShell)

2. **Run**:
   ```powershell
   adb --version
   ```

3. **Expected output**:
   ```
   Android Debug Bridge version 1.0.41
   Version 35.0.1-11580240
   ```

✅ **If you see version info, ADB is installed correctly!**

❌ **If you still see "adb not recognized"**:
   - Make sure you opened a NEW PowerShell window
   - Verify the path is exactly: `C:\adb\platform-tools`
   - Try restarting your computer

---

### **Option B: Install via Android Studio (More Complete)**

If you plan to do more Android development, this is better.

#### Step 2.1: Download Android Studio

1. Go to: https://developer.android.com/studio
2. Click "Download Android Studio"
3. Accept terms and download (~1 GB)

#### Step 2.2: Install Android Studio

1. Run the installer
2. Follow the setup wizard
3. Choose "Standard" installation
4. Wait for SDK components to download (10-20 minutes)

#### Step 2.3: Locate ADB

ADB will be installed at:
```
C:\Users\royvi\AppData\Local\Android\Sdk\platform-tools\
```

Add this path to your System PATH (same steps as Option A, Step 1.3)

---

## 📱 PART 2: Set Up Android Device

You need an Android device to run the agent. Choose ONE option:

### **Option A: BlueStacks Emulator (Easiest for Beginners)**

#### Step 3.1: Download BlueStacks

1. Go to: https://www.bluestacks.com/
2. Click "Download BlueStacks"
3. Download the installer (~600 MB)

#### Step 3.2: Install BlueStacks

1. Run the installer
2. Follow installation steps (takes 5-10 minutes)
3. Launch BlueStacks when installation completes

#### Step 3.3: Enable ADB in BlueStacks

1. **Open BlueStacks**
2. **Click** the hamburger menu (☰) in the top-right
3. **Go to** "Settings"
4. **Click** "Advanced" tab
5. **Find** "Android Debug Bridge (ADB)"
6. **Toggle it ON**
7. **Note the port number** (usually 5555)
8. **Click** "Restart Now"

#### Step 3.4: Connect ADB to BlueStacks

1. **Open PowerShell**
2. **Run**:
   ```powershell
   adb connect localhost:5555
   ```
3. **Expected output**:
   ```
   connected to localhost:5555
   ```

4. **Verify connection**:
   ```powershell
   adb devices
   ```
5. **Expected output**:
   ```
   List of devices attached
   localhost:5555    device
   ```

✅ **If you see "device", you're connected!**

---

### **Option B: Android Studio Emulator (More Realistic)**

#### Step 4.1: Open AVD Manager

1. Open Android Studio
2. Click "More Actions" → "Virtual Device Manager"
   - OR: Tools → Device Manager

#### Step 4.2: Create Virtual Device

1. Click "Create Device"
2. Select a device definition (e.g., "Pixel 5")
3. Click "Next"
4. Select a system image:
   - Recommended: "R" (Android 11) or "S" (Android 12)
   - Click "Download" if not already downloaded
5. Click "Next"
6. Name your AVD (e.g., "Pixel5_API30")
7. Click "Finish"

#### Step 4.3: Start Emulator

1. In Device Manager, click the ▶️ (Play) button next to your device
2. Wait for emulator to boot (1-2 minutes first time)
3. You'll see an Android phone screen

#### Step 4.4: Verify Connection

1. **Open PowerShell**
2. **Run**:
   ```powershell
   adb devices
   ```
3. **Expected output**:
   ```
   List of devices attached
   emulator-5554    device
   ```

✅ **If you see "emulator-5554 device", you're connected!**

---

### **Option C: Physical Android Phone (Most Realistic)**

#### Step 5.1: Enable Developer Options

1. **On your phone**: Go to Settings → About Phone
2. **Find** "Build Number" (might be under "Software Information")
3. **Tap** "Build Number" **7 times rapidly**
4. You'll see: "You are now a developer!"

#### Step 5.2: Enable USB Debugging

1. **Go back** to main Settings
2. **Find** "Developer Options" (usually under System or Advanced)
3. **Toggle ON**: "Developer Options"
4. **Toggle ON**: "USB Debugging"
5. **Accept** the warning dialog

#### Step 5.3: Connect Phone to Laptop

1. **Use a USB cable** to connect phone to laptop
2. **On your phone**: You'll see a popup "Allow USB debugging?"
3. **Check** "Always allow from this computer"
4. **Tap** "Allow"

#### Step 5.4: Verify Connection

1. **Open PowerShell**
2. **Run**:
   ```powershell
   adb devices
   ```
3. **Expected output**:
   ```
   List of devices attached
   ABC123XYZ    device
   ```

✅ **If you see your device serial number with "device", you're connected!**

❌ **If you see "unauthorized"**:
   - Check your phone for the USB debugging prompt
   - Tap "Allow"
   - Run `adb devices` again

---

## 🐍 PART 3: Install Python Dependencies

Now let's install the required Python packages for the agent.

### Step 6.1: Verify Python Installation

```powershell
python --version
```

**Expected**: Python 3.11 or higher

❌ **If Python is not installed**:
1. Go to: https://www.python.org/downloads/
2. Download Python 3.11+
3. **IMPORTANT**: Check "Add Python to PATH" during installation

### Step 6.2: Navigate to Project Directory

```powershell
cd c:\Users\royvi\Desktop\droidrun
```

### Step 6.3: Install OpenAI and LLM Dependencies

```powershell
pip install llama-index-llms-openai openai python-dotenv
```

**This will install**:
- `llama-index-llms-openai` - OpenAI integration for LlamaIndex
- `openai` - OpenAI Python SDK
- `python-dotenv` - For loading environment variables from .env file

**Wait time**: 1-2 minutes

✅ **Success looks like**:
```
Successfully installed openai-1.99.1 llama-index-llms-openai-0.5.6 python-dotenv-1.0.0
```

---

## 🔑 PART 4: Get and Set OpenAI API Key

The agent uses GPT-4o-mini, which requires an OpenAI API key.

### Step 7.1: Get Your API Key

1. **Go to**: https://platform.openai.com/api-keys
2. **Sign in** or create an account
3. **Click**: "Create new secret key"
4. **Name it**: "Droidrun Agent"
5. **Copy** the key (starts with `sk-`)
   - ⚠️ **IMPORTANT**: Save it somewhere safe - you can't see it again!

### Step 7.2: Set API Key (Method 1 - Environment Variable)

**For current PowerShell session only**:
```powershell
$env:OPENAI_API_KEY="sk-your-actual-key-here"
```

**To verify it's set**:
```powershell
echo $env:OPENAI_API_KEY
```

### Step 7.3: Set API Key (Method 2 - .env File) [Recommended]

**Create a .env file**:

1. **In PowerShell**:
   ```powershell
   cd c:\Users\royvi\Desktop\droidrun
   notepad .env
   ```

2. **In Notepad**, type:
   ```
   OPENAI_API_KEY=sk-your-actual-key-here
   ```

3. **Save** and close Notepad

4. **Update the Python script** to load from .env:

---

## 📧 PART 5: Set Up Gmail on Your Device

The agent needs Gmail to be installed and signed in.

### Step 8.1: Install Gmail

**On Emulator**:
1. Open Play Store
2. Search for "Gmail"
3. Install Gmail app

**On Physical Phone**:
- Gmail is usually pre-installed

### Step 8.2: Sign In to Gmail

1. Open Gmail app
2. Sign in with your Google account
3. Grant all requested permissions

### Step 8.3: Prepare Test Emails (Optional but Recommended)

For testing, send yourself 5-10 test emails with different types:

**Example test emails**:
1. **New Candidate**: Subject: "Application for Software Engineer - John Doe"
   - Attach a fake resume
2. **Follow-up**: Subject: "Re: Following up on my application"
3. **Interview**: Subject: "Interview availability - Tomorrow 2 PM?"
4. **Spam**: Subject: "Buy cheap software licenses now!"
5. **Urgent**: Subject: "URGENT: Interview today at 3 PM - Please confirm"

---

## 🎯 PART 6: Update and Run the Agent

### Step 9.1: Update Agent Script to Load .env

Let me update the script to properly load the .env file:

```python
# gmail_recruiter_agent.py
import os
import asyncio
from dotenv import load_dotenv  # Add this
from droidrun import DroidAgent, load_llm, DroidrunConfig
from droidrun.config_manager import AgentConfig

# Load environment variables from .env file
load_dotenv()

# Classification rules from external file
with open("prompts/classification_rules.txt", "r") as f:
    CLASSIFICATION_RULES = f.read()

RECRUITER_GOAL = f"""
You are a recruiter's AI assistant.

Open Gmail.
Find unread emails.
For each unread email:
- Classify it based on these rules:
{CLASSIFICATION_RULES}
- Apply the correct Gmail label (New Candidate, Follow-up, Interview Response, or Spam).
- Star emails that are urgent or time-sensitive.
- Draft a short professional reply if required.

Do NOT send emails automatically.
Stop when all unread emails are processed.
"""

async def main():
    # Check if API Key is set
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("❌ ERROR: OPENAI_API_KEY not found!")
        print("Please set it in .env file or environment variable.")
        return
    
    print("✅ OpenAI API Key found")
    
    # Configure LLM (gpt-4o-mini with low temperature for consistency)
    print("🔄 Loading LLM (GPT-4o-mini)...")
    llm = load_llm("OpenAI", model="gpt-4o-mini", temperature=0.2)
    print("✅ LLM loaded successfully")

    # Configure the Agent
    config = DroidrunConfig(
        agent=AgentConfig(
            max_steps=30,
            reasoning=True  # Manager/Executor loop for better planning
        )
    )

    print("🤖 Initializing Recruiter Inbox Triage Agent...")
    agent = DroidAgent(
        goal=RECRUITER_GOAL,
        llms=llm,
        config=config
    )
    print("✅ Agent initialized")

    print("\n" + "="*60)
    print("🚀 STARTING AGENT EXECUTION")
    print("="*60)
    print("📱 Watch your Android device screen for actions...")
    print("="*60 + "\n")
    
    handler = agent.run()
    
    # Stream events and show progress
    async for event in handler.stream_events():
        # Events will be logged automatically by the agent
        pass

    result = await handler
    
    print("\n" + "="*60)
    print("🏁 AGENT EXECUTION FINISHED")
    print("="*60)
    print(f"✅ Success: {result.success}")
    print(f"📝 Reason: {result.reason}")
    print("="*60)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n⚠️ Agent stopped by user (Ctrl+C)")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        import traceback
        traceback.print_exc()
```

### Step 9.2: Run the Agent!

```powershell
cd c:\Users\royvi\Desktop\droidrun
python gmail_recruiter_agent.py
```

### Step 9.3: What You'll See

**In PowerShell**:
```
✅ OpenAI API Key found
🔄 Loading LLM (GPT-4o-mini)...
✅ LLM loaded successfully
🤖 Initializing Recruiter Inbox Triage Agent...
✅ Agent initialized

============================================================
🚀 STARTING AGENT EXECUTION
============================================================
📱 Watch your Android device screen for actions...
============================================================

🚀 Running DroidAgent to achieve goal: ...
🔄 Step 1/30
📝 Initializing Manager and Executor Agents...
⚡ Running Executor for action...
```

**On Your Android Device**:
1. Gmail app opens automatically
2. Navigates to inbox
3. Opens first unread email
4. Reads the content
5. Opens the label menu
6. Applies appropriate label
7. Stars if urgent
8. Opens reply
9. Types draft response
10. Closes without sending
11. Moves to next email
12. Repeats until all emails processed

---

## 🎬 PART 7: Record Demo Video for Hackathon

### Step 10.1: Using Windows Game Bar (Built-in)

1. **Press** `Win + G`
2. **Click** the record button (⚫)
3. **Position** your Android emulator/phone screen in view
4. **Run** the agent
5. **Let it run** for 1-3 minutes
6. **Press** `Win + G` again and click stop (⏹️)
7. **Video saved to**: `C:\Users\royvi\Videos\Captures\`

### Step 10.2: Using OBS Studio (More Professional)

1. **Download OBS**: https://obsproject.com/
2. **Install** and open OBS
3. **Add Source**: Display Capture or Window Capture
4. **Select** your emulator window
5. **Click** "Start Recording"
6. **Run** the agent
7. **Click** "Stop Recording"
8. **Video saved to**: Check Settings → Output → Recording Path

### Step 10.3: What to Show in Demo

**Good demo structure** (1-3 minutes):
1. **Show inbox before** (10-15 unread emails)
2. **Start the agent** (show PowerShell command)
3. **Show agent working** (emails being opened, labels applied, stars added)
4. **Show inbox after** (organized with labels, starred emails)
5. **Show a draft reply** (open one email and show the drafted response)

---

## 🐛 PART 8: Troubleshooting Common Issues

### Issue 1: "adb not recognized"

**Solution**:
```powershell
# Use full path temporarily
C:\adb\platform-tools\adb.exe devices

# Or add to PATH and restart PowerShell
```

### Issue 2: "No devices attached"

**Solution**:
```powershell
# Restart ADB server
adb kill-server
adb start-server

# For BlueStacks, reconnect
adb connect localhost:5555

# For emulator, restart it
# For phone, unplug and replug USB
```

### Issue 3: "unauthorized" device

**Solution**:
- Check your phone screen for USB debugging prompt
- Tap "Allow"
- Check "Always allow from this computer"
- Run `adb devices` again

### Issue 4: "OPENAI_API_KEY not set"

**Solution**:
```powershell
# Check if it's set
echo $env:OPENAI_API_KEY

# Set it
$env:OPENAI_API_KEY="sk-your-key"

# Or create .env file
echo OPENAI_API_KEY=sk-your-key > .env
```

### Issue 5: Gmail not opening

**Solution**:
- Make sure Gmail is installed on device
- Sign in to Gmail manually first
- Grant all permissions
- Try opening Gmail manually to verify it works

### Issue 6: Agent is stuck or slow

**Solution**:
- Press `Ctrl+C` to stop
- Reduce `max_steps` to 15 in the config
- Check your internet connection
- Verify OpenAI API has credits

### Issue 7: "Module not found" errors

**Solution**:
```powershell
# Reinstall dependencies
pip install --upgrade llama-index-llms-openai openai python-dotenv

# Verify droidrun is installed
python -c "import droidrun; print(droidrun.__version__)"
```

---

## 📊 PART 9: Understanding What the Agent Does

### Agent Workflow:

1. **Manager Agent** (Planning):
   - Analyzes the goal
   - Creates a plan with subgoals
   - Decides next action

2. **Executor Agent** (Action):
   - Executes specific UI actions
   - Taps, swipes, types text
   - Reads screen content

3. **Loop**:
   - Manager checks progress
   - Executor performs next action
   - Repeats until goal achieved or max steps reached

### Example Agent Actions:

```
Step 1: Open Gmail app
Step 2: Tap on first unread email
Step 3: Read email subject and body
Step 4: Classify as "New Candidate"
Step 5: Tap three-dot menu
Step 6: Tap "Label"
Step 7: Select "New Candidate" label
Step 8: Tap star icon
Step 9: Tap reply button
Step 10: Type draft response
Step 11: Close without sending
Step 12: Go back to inbox
Step 13: Repeat for next email
```

---

## 🎯 PART 10: Prepare for Hackathon Submission

### Step 11.1: Create GitHub Repository

1. Go to: https://github.com/new
2. Repository name: `recruiter-gmail-agent`
3. Description: "AI agent for automating recruiter inbox triage using Droidrun"
4. Make it Public
5. Click "Create repository"

### Step 11.2: Organize Your Files

Create this structure:
```
recruiter-gmail-agent/
├── gmail_recruiter_agent.py
├── prompts/
│   └── classification_rules.txt
├── demo/
│   └── demo.mp4
├── README.md
├── requirements.txt
└── .env.example
```

### Step 11.3: Create README.md

```markdown
# Recruiter Inbox Triage Agent

AI-powered mobile agent that automates email classification and response drafting for recruiters.

## Problem Statement
Recruiters receive hundreds of emails daily. Manually classifying, labeling, and responding to each email is time-consuming and error-prone.

## Solution
An autonomous AI agent that:
- Opens Gmail on Android
- Classifies emails (New Candidate, Follow-up, Interview Response, Spam)
- Applies appropriate labels
- Stars urgent emails
- Drafts professional responses
- Never sends emails without human review

## Tech Stack
- **Framework**: Droidrun
- **LLM**: OpenAI GPT-4o-mini
- **Platform**: Android (emulator or physical device)
- **Language**: Python 3.11+

## Features
✅ Automatic email classification
✅ Smart labeling system
✅ Urgency detection
✅ Professional response drafting
✅ Safe (never auto-sends)

## Demo Video
[Watch Demo](./demo/demo.mp4)

## How to Run
See [SETUP_GUIDE.md](./SETUP_GUIDE.md)

## Judging Criteria Alignment
- **Innovation**: First recruiter-focused mobile AI agent
- **Technical Merit**: Real UI automation + LLM reasoning
- **Problem Value**: Saves recruiters 2-3 hours daily
- **Market Feasibility**: Immediate real-world application

## Author
Built for Droidrun DevSprint 2026
```

### Step 11.4: Push to GitHub

```powershell
cd c:\Users\royvi\Desktop\droidrun

# Initialize git (if not already)
git init

# Add files
git add gmail_recruiter_agent.py
git add prompts/
git add README.md
git add requirements.txt
git add SETUP_GUIDE.md

# Commit
git commit -m "Initial commit: Recruiter Inbox Triage Agent"

# Add remote (replace with your repo URL)
git remote add origin https://github.com/yourusername/recruiter-gmail-agent.git

# Push
git push -u origin main
```

### Step 11.5: Submit to Hackathon

1. Wait for submission form from GDG
2. Submit:
   - GitHub repository URL
   - Demo video (upload to YouTube or include in repo)
   - Brief description
3. Deadline: **Jan 19, 11:59 PM IST** (TODAY!)

---

## ⏰ Quick Checklist (If You're Short on Time)

- [ ] Install ADB
- [ ] Set up Android device (emulator or phone)
- [ ] Verify `adb devices` shows your device
- [ ] Install Python packages: `pip install llama-index-llms-openai openai python-dotenv`
- [ ] Get OpenAI API key
- [ ] Set API key in .env file
- [ ] Install Gmail on device and sign in
- [ ] Run: `python gmail_recruiter_agent.py`
- [ ] Record demo video
- [ ] Create GitHub repo
- [ ] Submit before deadline

---

## 🎉 You're Ready!

If you've followed all steps, you should now have:
✅ ADB installed and working
✅ Android device connected
✅ Python dependencies installed
✅ OpenAI API key configured
✅ Gmail set up on device
✅ Agent ready to run

**Just run**:
```powershell
python gmail_recruiter_agent.py
```

**And watch the magic happen!** 🚀

---

## 📞 Need Help?

- **Droidrun Docs**: https://docs.droidrun.ai
- **Discord**: https://discord.gg/ZZbKEZZkwK
- **GitHub Issues**: https://github.com/droidrun/droidrun/issues

Good luck with the hackathon! 🏆
