"""
Simple Portal APK Installation Script
Assumes you have already downloaded portal.apk to the current directory.
"""

import os
import sys
import subprocess

def find_adb():
    """Find ADB executable."""
    try:
        subprocess.run(["adb", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=5)
        return "adb"
    except:
        pass
    
    paths = [
        r"C:\adb\platform-tools\adb.exe",
        r"C:\platform-tools\adb.exe",
        r"C:\Users\royvi\Downloads\platform-tools\adb.exe",
        r"C:\Users\royvi\AppData\Local\Android\Sdk\platform-tools\adb.exe"
    ]
    
    for path in paths:
        if os.path.exists(path):
            return path
    return None

def main():
    print("=" * 70)
    print("  🤖 Portal APK Manual Installation")
    print("=" * 70)
    
    # Check for APK file
    apk_paths = [
        "portal.apk",
        "droidrun_portal.apk",
        os.path.join(os.getcwd(), "portal.apk"),
    ]
    
    apk_path = None
    for path in apk_paths:
        if os.path.exists(path):
            apk_path = path
            break
    
    if not apk_path:
        print("\n❌ Portal APK not found!")
        print("\n📥 Please download portal.apk and place it in:")
        print(f"   {os.getcwd()}")
        print("\n💡 Download from:")
        print("   https://github.com/droidrun/droidrun/tree/main/droidrun/tools/android")
        print("\nOr search for 'droidrun portal.apk' online")
        return False
    
    print(f"\n✅ Found APK: {apk_path}")
    print(f"   Size: {os.path.getsize(apk_path) / 1024:.1f} KB")
    
    # Find ADB
    adb = find_adb()
    if not adb:
        print("\n❌ ADB not found")
        return False
    
    print(f"✅ Found ADB: {adb}")
    
    # Check device
    print("\n🔧 Checking device...")
    try:
        result = subprocess.run([adb, "devices"], capture_output=True, text=True, timeout=10)
        lines = result.stdout.strip().split('\n')
        devices = [line for line in lines[1:] if line.strip() and '\tdevice' in line]
        
        if not devices:
            print("❌ No devices connected")
            print("\n📱 Please connect your phone and enable USB debugging")
            return False
        
        print(f"✅ Found {len(devices)} device(s)")
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    
    # Uninstall existing
    print("\n🗑️  Removing existing installation...")
    try:
        subprocess.run([adb, "uninstall", "com.droidrun.portal"], 
                      capture_output=True, timeout=30)
        print("   Done")
    except:
        print("   No existing installation")
    
    # Install
    print("\n📲 Installing Portal...")
    try:
        result = subprocess.run(
            [adb, "install", "-r", "-g", apk_path],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        print(result.stdout)
        
        if result.returncode == 0 and "Success" in result.stdout:
            print("\n✅ SUCCESS!")
            print("\n📱 Next steps:")
            print("  1. Open 'Portal' app on your phone")
            print("  2. Grant all permissions")
            print("  3. Keep it running")
            print("  4. Run: python gmail_recruiter_agent.py")
            return True
        else:
            print(f"\n❌ Installation failed")
            if result.stderr:
                print(f"Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Cancelled")
        sys.exit(1)
