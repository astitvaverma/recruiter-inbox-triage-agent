# 🎯 PORTAL APK INSTALLATION - COMPLETE SOLUTION

## What Happened

The error you're seeing:
```
Portal returned error: Failed to parse state data from ContentProvider
```

This occurs because the **Droidrun Portal APK is missing** from your installation. The Portal app is a critical Android component that acts as a bridge between Droidrun (on your PC) and your Android device.

## What is Portal?

Portal is an Android accessibility service that:
- Provides real-time UI element data to Droidrun
- Enables Droidrun to interact with your Android device
- Creates an interactive overlay for debugging
- Handles communication via ADB ContentProvider

Without Portal installed and running on your phone, Droidrun cannot communicate with your device.

## 🚀 QUICK FIX (3 Steps)

### Step 1: Download Portal APK

**Direct Link:** https://github.com/droidrun/droidrun-portal/releases/latest

1. Click the link above
2. Download the APK file (usually `app-release.apk`)
3. Save it as: `c:\Users\royvi\Desktop\droidrun\portal.apk`

### Step 2: Install Portal APK

```powershell
cd c:\Users\royvi\Desktop\droidrun
python manual_install_portal.py
```

The script will automatically:
- ✅ Detect your connected Android device
- ✅ Remove any old Portal installation
- ✅ Install the new Portal APK with all permissions
- ✅ Verify the installation

### Step 3: Enable Portal on Your Phone

1. Open the **Portal** app on your phone
2. Grant **Accessibility Service** permission
3. Grant **Storage** permissions
4. Keep the app running in the background

### Step 4: Run Your Agent

```powershell
python gmail_recruiter_agent.py
```

The "Portal returned error" should now be resolved! ✅

## 📋 Files Created for You

I've created these helper files in your droidrun folder:

1. **`PORTAL_INSTALLATION_GUIDE.md`** - Detailed installation guide
2. **`manual_install_portal.py`** - Automated installation script
3. **`install_portal.py`** - Alternative installation script
4. **`download_and_install_portal.py`** - Download + install script

## 🔍 Why Was Portal Missing?

The Portal APK is maintained in a separate repository (`droidrun/droidrun-portal`) and is not included in the main Droidrun Python package. This is common for Android components that need to be installed separately on the device.

## ⚡ Alternative: Manual ADB Installation

If you prefer to install manually:

```powershell
# 1. Download portal.apk from GitHub releases
# 2. Connect your phone via USB
# 3. Run these commands:

adb devices                              # Verify device is connected
adb uninstall com.droidrun.portal       # Remove old version
adb install -r -g portal.apk            # Install with permissions
adb shell pm list packages | findstr portal  # Verify installation
```

## 🛠️ Troubleshooting

### If Portal crashes:
```powershell
adb logcat | findstr Portal
```

### If device not detected:
```powershell
adb kill-server
adb start-server
adb devices
```

### If still getting errors after installation:
1. Restart the Portal app on your phone
2. Ensure Accessibility Service is enabled for Portal
3. Try reconnecting your USB cable
4. Check that USB debugging is enabled

## 📱 Verify Portal is Working

After installation, verify:

```powershell
# Check if installed
adb shell pm list packages | findstr portal

# Should output: package:com.droidrun.portal
```

## 🎬 Next Steps After Portal is Installed

Once Portal is installed and running:

1. The error "Failed to parse state data" will be resolved
2. Droidrun will be able to communicate with your device
3. Your Gmail Recruiter Agent will be able to run
4. You can record your demo video for the hackathon

## 📚 Resources

- **Portal Repository:** https://github.com/droidrun/droidrun-portal
- **Latest Release:** https://github.com/droidrun/droidrun-portal/releases/latest
- **Droidrun Docs:** https://droidrun.ai
- **GitHub Actions (for latest builds):** https://github.com/droidrun/droidrun-portal/actions

## 💡 Pro Tip

After installing Portal, you might want to:
- Keep Portal running in the background
- Disable battery optimization for Portal
- Add Portal to the "Don't kill" list in your phone's settings

This ensures Portal stays active and responsive during your Droidrun agent execution.

---

## Summary

**The Issue:** Portal APK missing → "Failed to parse state data" error

**The Solution:**
1. Download: https://github.com/droidrun/droidrun-portal/releases/latest
2. Save as: `portal.apk`
3. Run: `python manual_install_portal.py`
4. Open Portal app and grant permissions
5. Run your agent: `python gmail_recruiter_agent.py`

**Result:** Droidrun can now communicate with your Android device! 🎉
