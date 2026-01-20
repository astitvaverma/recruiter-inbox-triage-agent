"""
Download Portal APK from GitHub and install it to the connected Android device.
"""

import os
import sys
import subprocess
import urllib.request
import tempfile

def find_adb():
    """Find ADB executable."""
    try:
        subprocess.run(["adb", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=5)
        return "adb"
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    
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

def check_device(adb_cmd):
    """Check if device is connected."""
    print("\n🔧 Checking device connection...")
    try:
        result = subprocess.run([adb_cmd, "devices"], capture_output=True, text=True, timeout=10)
        lines = result.stdout.strip().split('\n')
        devices = [line for line in lines[1:] if line.strip() and '\tdevice' in line]
        
        if not devices:
            print("❌ No devices connected")
            print("\n📱 Please:")
            print("  1. Connect your phone via USB")
            print("  2. Enable USB debugging")
            print("  3. Authorize this computer on your phone")
            return False
        
        print(f"✅ Found {len(devices)} device(s)")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def download_portal_apk():
    """Download Portal APK from GitHub releases."""
    print("\n📥 Downloading Portal APK from GitHub...")
    
    # GitHub raw URL for the Portal APK
    # Note: This URL might need to be updated based on the actual Droidrun repository structure
    urls_to_try = [
        "https://github.com/droidrun/droidrun/raw/main/droidrun/tools/android/portal.apk",
        "https://github.com/droidrun/droidrun/raw/master/droidrun/tools/android/portal.apk",
    ]
    
    temp_dir = tempfile.gettempdir()
    apk_path = os.path.join(temp_dir, "droidrun_portal.apk")
    
    for url in urls_to_try:
        try:
            print(f"   Trying: {url}")
            urllib.request.urlretrieve(url, apk_path)
            
            # Check if file was downloaded and is not empty
            if os.path.exists(apk_path) and os.path.getsize(apk_path) > 1000:
                print(f"✅ Downloaded to: {apk_path}")
                print(f"   Size: {os.path.getsize(apk_path) / 1024:.1f} KB")
                return apk_path
        except Exception as e:
            print(f"   ❌ Failed: {e}")
            continue
    
    return None

def install_apk(adb_cmd, apk_path):
    """Install APK to device."""
    print("\n📲 Installing Portal APK...")
    
    # Uninstall existing first
    try:
        print("   Removing existing installation...")
        subprocess.run([adb_cmd, "uninstall", "com.droidrun.portal"], 
                      capture_output=True, timeout=30)
    except Exception:
        pass
    
    # Install new
    try:
        result = subprocess.run(
            [adb_cmd, "install", "-r", "-g", apk_path],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        print(result.stdout)
        
        if result.returncode == 0 and "Success" in result.stdout:
            print("✅ Installation successful!")
            return True
        else:
            print(f"❌ Installation failed")
            if result.stderr:
                print(f"   Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Main workflow."""
    print("=" * 70)
    print("  🤖 Droidrun Portal APK Download & Installation")
    print("=" * 70)
    
    # Find ADB
    adb_cmd = find_adb()
    if not adb_cmd:
        print("\n❌ ADB not found")
        print("\n💡 Please install Android SDK Platform Tools")
        return False
    
    print(f"✅ Found ADB: {adb_cmd}")
    
    # Check device
    if not check_device(adb_cmd):
        return False
    
    # Download APK
    apk_path = download_portal_apk()
    if not apk_path:
        print("\n❌ Could not download Portal APK")
        print("\n💡 Alternative: Please manually download portal.apk and place it in:")
        print("   c:\\Users\\royvi\\Desktop\\droidrun\\")
        return False
    
    # Install APK
    if not install_apk(adb_cmd, apk_path):
        return False
    
    # Success
    print("\n" + "=" * 70)
    print("  ✅ SUCCESS!")
    print("=" * 70)
    print("\n📱 Next steps:")
    print("  1. Open the 'Portal' app on your phone")
    print("  2. Grant all permissions")
    print("  3. Keep it running in the background")
    print("  4. Run: python gmail_recruiter_agent.py")
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Cancelled")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
