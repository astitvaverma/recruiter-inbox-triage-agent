# Android Studio Installation Guide - Complete Steps

## 📦 Part 1: Download Android Studio

### Step 1: Download

1. **Open your browser** and go to:
   ```
   https://developer.android.com/studio
   ```

2. **Click** the big green button: **"Download Android Studio"**

3. **Accept** the terms and conditions (check the box)

4. **Click** "Download Android Studio for Windows"

5. **Save the file** to your Downloads folder
   - File name: `android-studio-2024.x.x.xx-windows.exe`
   - Size: ~1 GB
   - Download time: 5-10 minutes (depending on internet speed)

---

## 💻 Part 2: Install Android Studio

### Step 2: Run the Installer

1. **Go to** your Downloads folder:
   ```
   C:\Users\royvi\Downloads\
   ```

2. **Double-click** on `android-studio-2024.x.x.xx-windows.exe`

3. **Click "Yes"** if Windows asks for permission (User Account Control)

### Step 3: Installation Wizard

1. **Welcome Screen**:
   - Click **"Next"**

2. **Choose Components**:
   - ✅ Keep **all boxes checked** (Android Studio, Android Virtual Device)
   - Click **"Next"**

3. **Configuration Settings**:
   - Leave default settings
   - Click **"Next"**

4. **Choose Install Location**:
   - Default: `C:\Program Files\Android\Android Studio`
   - Click **"Next"**

5. **Choose Start Menu Folder**:
   - Leave default: "Android Studio"
   - Click **"Install"**

6. **Wait for installation** (5-10 minutes)
   - Progress bar will show installation progress

7. **Installation Complete**:
   - ✅ Check "Start Android Studio"
   - Click **"Finish"**

---

## ⚙️ Part 3: First-Time Setup

### Step 4: Android Studio Setup Wizard

1. **Import Settings**:
   - Select: **"Do not import settings"**
   - Click **"OK"**

2. **Welcome Screen**:
   - Click **"Next"**

3. **Install Type**:
   - Select: **"Standard"** (recommended)
   - Click **"Next"**

4. **Select UI Theme**:
   - Choose: **"Darcula"** (dark) or **"Light"** (your preference)
   - Click **"Next"**

5. **Verify Settings**:
   - Review the components to be downloaded:
     - Android SDK
     - Android SDK Platform
     - Android Virtual Device
   - Click **"Next"**

6. **License Agreement**:
   - Click **"Accept"** for each license
   - Click **"Finish"**

7. **Downloading Components** (10-15 minutes):
   - Android SDK
   - System images
   - Build tools
   - **Wait for this to complete** - don't close the window!

8. **Setup Complete**:
   - Click **"Finish"**

---

## 📱 Part 4: Create Android Virtual Device (Emulator)

### Step 5: Open Device Manager

1. **On the Welcome Screen**, click:
   - **"More Actions"** (three dots) → **"Virtual Device Manager"**
   
   OR if you see a different screen:
   - **Tools** → **Device Manager**

### Step 6: Create New Virtual Device

1. **Click** the **"Create Device"** button (or **"+"** icon)

2. **Select Hardware**:
   - Category: **Phone**
   - Device: **Pixel 5** (recommended)
     - Screen: 6.0"
     - Resolution: 1080 x 2340
   - Click **"Next"**

3. **Select System Image**:
   - **Recommended** tab
   - Select: **"R"** (Android 11.0, API Level 30)
     - If you see a **"Download"** link next to it, click it
     - Wait for download to complete (5-10 minutes, ~1 GB)
   - Click **"Next"**

4. **Verify Configuration**:
   - AVD Name: **Pixel_5_API_30** (or keep default)
   - Startup orientation: Portrait
   - Click **"Show Advanced Settings"** (optional, but recommended):
     - RAM: 2048 MB (or higher if you have 8+ GB RAM)
     - Internal Storage: 2048 MB
     - SD Card: 512 MB
   - Click **"Finish"**

### Step 7: Start the Emulator

1. **In Device Manager**, you'll see your new device: **Pixel_5_API_30**

2. **Click the Play button** ▶️ next to it

3. **Wait for emulator to boot** (1-2 minutes first time)
   - You'll see the Android boot animation
   - Then the Android home screen

4. **Emulator is ready!** You should see:
   - Android home screen
   - Navigation buttons at bottom
   - Status bar at top

---

## ✅ Part 5: Verify ADB Connection

### Step 8: Check ADB Connection

1. **Open PowerShell** (new window)

2. **Run**:
   ```powershell
   adb devices
   ```

3. **Expected output**:
   ```
   List of devices attached
   emulator-5554    device
   ```

✅ **If you see "emulator-5554 device" - you're connected!**

❌ **If you see "unauthorized"**:
   - Look at the emulator screen
   - You'll see a popup: "Allow USB debugging?"
   - Check "Always allow from this computer"
   - Click "Allow"
   - Run `adb devices` again

---

## 📧 Part 6: Set Up Gmail

### Step 9: Find and Open Gmail

1. **In the emulator**, swipe up from the bottom to see all apps

2. **Look for Gmail** (red/white envelope icon)
   - Gmail is **pre-installed** on most system images!

3. **Click Gmail** to open it

4. **Sign in**:
   - Enter your Google account email
   - Enter password
   - Accept terms
   - Skip optional steps (backup, etc.)

5. **Gmail is ready!**

### Step 10: Send Test Emails

1. **On your computer** (not emulator), go to Gmail.com

2. **Send yourself 5-10 test emails** with subjects like:
   - "Application for Software Engineer - Resume Attached"
   - "Re: Following up on my application"
   - "Interview Availability - Tomorrow 2 PM"
   - "URGENT: Interview today at 3 PM"
   - "Buy cheap software now!" (spam)

3. **Check emulator Gmail** - you should see the emails appear

---

## 🚀 Part 7: Run the Droidrun Agent

### Step 11: Set Up Environment

1. **Open PowerShell**

2. **Navigate to project**:
   ```powershell
   cd c:\Users\royvi\Desktop\droidrun
   ```

3. **Create .env file** (if not done):
   ```powershell
   notepad .env
   ```
   
   Add this line:
   ```
   OPENAI_API_KEY=sk-your-actual-openai-api-key-here
   ```
   
   Save and close.

4. **Install dependencies** (if not done):
   ```powershell
   pip install llama-index-llms-openai openai python-dotenv
   ```

### Step 12: Run the Agent!

```powershell
python gmail_recruiter_agent.py
```

**Watch the emulator** - Gmail will open and the agent will:
1. ✅ Read unread emails
2. ✅ Classify each one
3. ✅ Apply labels
4. ✅ Star urgent emails
5. ✅ Draft replies

---

## 🎬 Part 8: Record Demo Video

### Step 13: Record Your Demo

1. **Position the emulator** so it's visible on screen

2. **Press Win + G** to open Game Bar

3. **Click the record button** ⚫

4. **Run the agent**:
   ```powershell
   python gmail_recruiter_agent.py
   ```

5. **Show**:
   - Inbox before (unread emails)
   - Agent running (emails being processed)
   - Inbox after (organized, labeled, starred)
   - One drafted reply

6. **Stop recording** (Win + G → Stop)

7. **Video saved to**: `C:\Users\royvi\Videos\Captures\`

---

## 🐛 Troubleshooting

### Issue: "adb not found"
**Solution**: Android Studio's ADB is at:
```
C:\Users\royvi\AppData\Local\Android\Sdk\platform-tools\
```
Add this to your PATH or use the full path.

### Issue: Emulator won't start
**Solution**:
- Make sure virtualization is enabled in BIOS
- Or try: Tools → AVD Manager → Edit device → Change Graphics to "Software"

### Issue: Gmail not pre-installed
**Solution**:
- Download a system image with Google APIs (has Play Store)
- Or install Gmail APK: `adb install gmail.apk`

### Issue: Emulator is slow
**Solution**:
- Allocate more RAM in AVD settings
- Enable hardware acceleration (HAXM)
- Close other programs

---

## ⏰ Time Estimate

- ⏱️ **Download Android Studio**: 5-10 min
- ⏱️ **Install Android Studio**: 5-10 min
- ⏱️ **First-time setup**: 10-15 min
- ⏱️ **Create emulator**: 5-10 min
- ⏱️ **Download system image**: 5-10 min
- ⏱️ **Set up Gmail**: 5 min
- ⏱️ **Run agent**: 10 min
- ⏱️ **Record demo**: 10 min

**Total: ~1 hour** (you have 5+ hours remaining!)

---

## ✅ Quick Checklist

- [ ] Download Android Studio
- [ ] Install Android Studio
- [ ] Complete setup wizard
- [ ] Create Pixel 5 emulator (API 30)
- [ ] Start emulator
- [ ] Verify ADB connection (`adb devices`)
- [ ] Open Gmail and sign in
- [ ] Send test emails
- [ ] Create .env file with API key
- [ ] Install Python dependencies
- [ ] Run `python gmail_recruiter_agent.py`
- [ ] Record demo video
- [ ] Submit to hackathon

---

## 🎯 You're Ready!

Follow these steps in order and you'll have a working demo in about 1 hour!

Good luck! 🚀
