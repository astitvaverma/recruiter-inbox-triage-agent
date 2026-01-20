# Gmail APK Installation Guide for BlueStacks

## Method 1: Download and Install Gmail APK

### Step 1: Download Gmail APK
Go to one of these trusted sources:
- APKMirror: https://www.apkmirror.com/apk/google-inc/gmail/
- APKPure: https://apkpure.com/gmail/com.google.android.gm

Download the latest version and save to your Downloads folder.

### Step 2: Install via ADB

Open PowerShell and run:

```powershell
# Navigate to Downloads folder
cd C:\Users\royvi\Downloads

# List files to find the exact APK name
dir *.apk

# Install Gmail (replace filename with actual name)
adb install gmail.apk
```

### Step 3: Verify Installation

```powershell
adb shell pm list packages | findstr gmail
```

Expected output: `package:com.google.android.gm`

### Step 4: Launch Gmail

In BlueStacks:
1. Go to app drawer
2. Find Gmail app
3. Open and sign in with your Google account

---

## Method 2: Install Google Play Services (May Fix Play Store)

Sometimes installing Google Play Services fixes the Play Store:

```powershell
# Download Google Play Services APK from APKMirror
# Then install:
adb install google-play-services.apk
adb install google-play-store.apk

# Restart BlueStacks
adb reboot
```

---

## Method 3: Use a Different Emulator

If BlueStacks continues to have issues, try:

### Android Studio Emulator (More Reliable)
1. Install Android Studio
2. Create AVD (Android Virtual Device)
3. Gmail comes pre-installed on most system images

### LDPlayer (Alternative to BlueStacks)
1. Download from: https://www.ldplayer.net/
2. Install and launch
3. Gmail usually pre-installed

---

## Troubleshooting

### "INSTALL_FAILED_UPDATE_INCOMPATIBLE"
```powershell
# Uninstall existing Gmail first
adb uninstall com.google.android.gm

# Then install again
adb install gmail.apk
```

### "adb: failed to install"
- Make sure BlueStacks is running
- Check ADB connection: `adb devices`
- Try reconnecting: `adb connect localhost:5555`

### APK architecture mismatch
- Download the ARM version (not ARM64 or x86)
- Or download "universal" APK

---

## Quick Test After Installation

Once Gmail is installed, run:

```powershell
cd c:\Users\royvi\Desktop\droidrun
python gmail_recruiter_agent.py
```

The agent will:
1. Open Gmail app
2. Read unread emails
3. Classify them
4. Apply labels
5. Star urgent ones
6. Draft replies

---

## Need Help?

If you're still having trouble, let me know:
1. What error message you see
2. Screenshot of the issue
3. Which method you tried

We'll get Gmail working! 🚀
