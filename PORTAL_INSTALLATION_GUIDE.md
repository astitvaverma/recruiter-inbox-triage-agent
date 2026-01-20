# 🚀 PORTAL APK INSTALLATION - QUICK START GUIDE

## The Problem
Your Droidrun installation is missing the Portal APK, causing this error:
```
Portal returned error: Failed to parse state data from ContentProvider
```

## ✅ SOLUTION: Download and Install Portal APK

### Step 1: Download the Portal APK

**Option A: Direct Download from GitHub Releases (RECOMMENDED)**

1. Visit: https://github.com/droidrun/droidrun-portal/releases/latest
2. Download the APK file (usually named `app-release.apk` or `portal.apk`)
3. Save it to: `c:\Users\royvi\Desktop\droidrun\portal.apk`

**Option B: Download from GitHub Actions**

1. Go to: https://github.com/droidrun/droidrun-portal/actions
2. Click on the latest successful workflow run
3. Scroll down to "Artifacts"
4. Download the APK artifact
5. Extract and save to: `c:\Users\royvi\Desktop\droidrun\portal.apk`

### Step 2: Install the Portal APK

Once you have downloaded `portal.apk`, run:

```powershell
cd c:\Users\royvi\Desktop\droidrun
python manual_install_portal.py
```

This script will:
- ✅ Find your connected Android device
- ✅ Uninstall any existing Portal installation
- ✅ Install the new Portal APK
- ✅ Grant necessary permissions

### Step 3: Configure Portal on Your Phone

1. **Open the Portal app** on your phone (check app drawer)
2. **Grant all permissions** when prompted:
   - Accessibility Service
   - Storage permissions
   - Any other requested permissions
3. **Keep the app running** in the background

### Step 4: Run Your Droidrun Agent

```powershell
python gmail_recruiter_agent.py
```

## 🔧 Alternative: Manual ADB Installation

If you prefer to install manually using ADB:

```powershell
# Check device connection
adb devices

# Uninstall old version
adb uninstall com.droidrun.portal

# Install Portal APK
adb install -r -g portal.apk

# Verify installation
adb shell pm list packages | findstr portal
```

## 📱 Verify Portal is Working

After installation, you can verify Portal is running:

```powershell
# Check if Portal package is installed
adb shell pm list packages | findstr portal

# Check Portal service status
adb shell dumpsys package com.droidrun.portal
```

## ❓ Troubleshooting

### Portal app crashes on startup
- Check Android version compatibility (requires Android 7.0+)
- Try reinstalling: `adb uninstall com.droidrun.portal` then reinstall
- Check logs: `adb logcat | findstr Portal`

### Still getting "Failed to parse state data" error
1. Restart the Portal app on your phone
2. Restart ADB: `adb kill-server && adb start-server`
3. Reconnect your USB cable
4. Make sure Accessibility Service is enabled for Portal

### Device not detected
- Enable USB debugging in Developer Options
- Authorize this computer on your phone
- Try a different USB cable/port
- Install/update ADB drivers

## 📚 Additional Resources

- Portal Repository: https://github.com/droidrun/droidrun-portal
- Droidrun Documentation: https://droidrun.ai
- Latest Release: https://github.com/droidrun/droidrun-portal/releases/latest

## 🎯 Quick Summary

1. Download Portal APK from: https://github.com/droidrun/droidrun-portal/releases/latest
2. Save as: `c:\Users\royvi\Desktop\droidrun\portal.apk`
3. Run: `python manual_install_portal.py`
4. Open Portal app on phone and grant permissions
5. Run: `python gmail_recruiter_agent.py`

---

**Need Help?** Check the Droidrun documentation or open an issue on GitHub.
