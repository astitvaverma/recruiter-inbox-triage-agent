"""
Droidrun Portal APK Installation Script
Automatically finds and installs the Droidrun Portal APK to your Android device.
"""

import os
import sys
import subprocess
import time
import droidrun
from pathlib import Path

def find_adb():
    """Find ADB executable on the system."""
    # Try system adb first
    try:
        subprocess.run(["adb", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=5)
        return "adb"
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    
    # Check common locations
    common_paths = [
        r"C:\adb\platform-tools\adb.exe",
        r"C:\platform-tools\adb.exe",
        r"C:\Users\royvi\Downloads\platform-tools\adb.exe",
        r"C:\Users\royvi\AppData\Local\Android\Sdk\platform-tools\adb.exe"
    ]
    
    for path in common_paths:
        if os.path.exists(path):
            return path
            
    return None

def check_device_connection(adb_cmd):
    """Verify that a device is connected and authorized."""
    print("\n🔧 Checking device connection...")
    try:
        result = subprocess.run(
            [adb_cmd, "devices"],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        lines = result.stdout.strip().split('\n')
        devices = [line for line in lines[1:] if line.strip() and '\tdevice' in line]
        
        if not devices:
            print("❌ No devices connected or authorized")
            print("\n📱 Please ensure:")
            print("  1. Your phone is connected via USB")
            print("  2. USB debugging is enabled in Developer Options")
            print("  3. You've authorized this computer on your phone")
            print("  4. Try running: adb kill-server && adb start-server")
            return False
        
        print(f"✅ Found {len(devices)} connected device(s)")
        for device in devices:
            print(f"   📱 {device}")
        return True
        
    except Exception as e:
        print(f"❌ Error checking devices: {e}")
        return False

def uninstall_existing_portal(adb_cmd):
    """Remove any existing Portal installation."""
    print("\n🗑️  Checking for existing Portal installation...")
    try:
        result = subprocess.run(
            [adb_cmd, "shell", "pm", "list", "packages", "com.droidrun.portal"],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if "com.droidrun.portal" in result.stdout:
            print("   Found existing installation, removing...")
            subprocess.run(
                [adb_cmd, "uninstall", "com.droidrun.portal"],
                capture_output=True,
                timeout=30
            )
            print("   ✅ Removed existing Portal")
            time.sleep(2)
        else:
            print("   No existing installation found")
            
    except Exception as e:
        print(f"   ⚠️  Warning: {e}")

def grant_permissions(adb_cmd):
    """Grant necessary permissions to Portal."""
    print("\n🔐 Granting permissions...")
    
    permissions = [
        "android.permission.WRITE_EXTERNAL_STORAGE",
        "android.permission.READ_EXTERNAL_STORAGE",
    ]
    
    for permission in permissions:
        try:
            subprocess.run(
                [adb_cmd, "shell", "pm", "grant", "com.droidrun.portal", permission],
                capture_output=True,
                timeout=10
            )
        except Exception:
            pass  # Some permissions may not be grantable
    
    print("✅ Permissions granted")

def verify_installation(adb_cmd):
    """Verify Portal is installed correctly."""
    print("\n🔍 Verifying installation...")
    try:
        result = subprocess.run(
            [adb_cmd, "shell", "pm", "list", "packages", "com.droidrun.portal"],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if "com.droidrun.portal" in result.stdout:
            print("✅ Portal is installed and ready!")
            return True
        else:
            print("❌ Portal not found after installation")
            return False
            
    except Exception as e:
        print(f"⚠️  Could not verify: {e}")
        return False

def install_portal():
    """Main installation workflow."""
    print("=" * 70)
    print("  🤖 Droidrun Portal APK Installation")
    print("=" * 70)
    
    # Step 1: Find ADB
    adb_cmd = find_adb()
    if not adb_cmd:
        print("\n❌ Could not find 'adb' command.")
        print("\n💡 Solutions:")
        print("  1. Install Android SDK Platform Tools")
        print("  2. Add ADB to your system PATH")
        print("  3. Download from: https://developer.android.com/tools/releases/platform-tools")
        return False
        
    print(f"✅ Found ADB: {adb_cmd}")
    
    # Step 2: Check device connection
    if not check_device_connection(adb_cmd):
        return False
    
    # Step 3: Find Portal APK
    print("\n🔍 Searching for Portal APK...")
    package_dir = os.path.dirname(droidrun.__file__)
    portal_path = None
    
    for root, dirs, files in os.walk(package_dir):
        for file in files:
            if "portal" in file.lower() and file.endswith(".apk"):
                portal_path = os.path.join(root, file)
                break
        if portal_path:
            break
            
    if not portal_path:
        print("❌ Could not find portal.apk in droidrun package")
        print(f"   Searched in: {package_dir}")
        return False
        
    print(f"✅ Found Portal APK: {portal_path}")
    print(f"   Size: {os.path.getsize(portal_path) / 1024:.1f} KB")
    
    # Step 4: Uninstall existing
    uninstall_existing_portal(adb_cmd)
    
    # Step 5: Install Portal
    print("\n📲 Installing Portal to device...")
    try:
        result = subprocess.run(
            [adb_cmd, "install", "-r", "-g", portal_path],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        print(result.stdout)
        
        if result.returncode == 0 and "Success" in result.stdout:
            print("✅ Installation successful!")
        else:
            print(f"❌ Installation failed")
            if result.stderr:
                print(f"   Error: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ Installation timed out")
        return False
    except Exception as e:
        print(f"❌ Installation error: {e}")
        return False
    
    # Step 6: Grant permissions
    grant_permissions(adb_cmd)
    
    # Step 7: Verify
    if not verify_installation(adb_cmd):
        return False
    
    # Success!
    print("\n" + "=" * 70)
    print("  ✅ SUCCESS! Portal is ready to use")
    print("=" * 70)
    print("\n📱 Next steps:")
    print("  1. Open the 'Portal' app on your phone (check app drawer)")
    print("  2. Grant any permissions it requests")
    print("  3. Keep the app running in the background")
    print("  4. Run your Droidrun agent:")
    print("     python gmail_recruiter_agent.py")
    print("\n💡 Tip: If you still get errors, try:")
    print("  - Restarting the Portal app on your phone")
    print("  - Running: adb kill-server && adb start-server")
    print("  - Reconnecting your USB cable")
    
    return True

if __name__ == "__main__":
    try:
        success = install_portal()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Installation cancelled")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
