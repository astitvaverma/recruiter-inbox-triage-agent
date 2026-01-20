"""
Simple Portal APK Installation Script (No Unicode)
Installs portal.apk to the connected Android device.
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
    print("  Portal APK Installation")
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
        print("\n[ERROR] Portal APK not found!")
        print("\nPlease download portal.apk and place it in:")
        print(f"   {os.getcwd()}")
        return False
    
    print(f"\n[OK] Found APK: {apk_path}")
    print(f"     Size: {os.path.getsize(apk_path) / 1024:.1f} KB")
    
    # Find ADB
    adb = find_adb()
    if not adb:
        print("\n[ERROR] ADB not found")
        return False
    
    print(f"[OK] Found ADB: {adb}")
    
    # Check device
    print("\n[INFO] Checking device...")
    try:
        result = subprocess.run([adb, "devices"], capture_output=True, text=True, timeout=10)
        lines = result.stdout.strip().split('\n')
        devices = [line for line in lines[1:] if line.strip() and '\tdevice' in line]
        
        if not devices:
            print("[ERROR] No devices connected")
            print("\nPlease:")
            print("  1. Connect your phone via USB")
            print("  2. Enable USB debugging")
            print("  3. Authorize this computer on your phone")
            return False
        
        print(f"[OK] Found {len(devices)} device(s)")
        for device in devices:
            print(f"     {device}")
    except Exception as e:
        print(f"[ERROR] {e}")
        return False
    
    # Uninstall existing
    print("\n[INFO] Removing existing installation...")
    try:
        subprocess.run([adb, "uninstall", "com.droidrun.portal"], 
                      capture_output=True, timeout=30)
        print("     Done")
    except:
        print("     No existing installation")
    
    # Install
    print("\n[INFO] Installing Portal APK...")
    print("     This may take 30-60 seconds...")
    try:
        result = subprocess.run(
            [adb, "install", "-r", "-g", apk_path],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        print("\n" + result.stdout)
        
        if result.returncode == 0 and "Success" in result.stdout:
            print("\n" + "=" * 70)
            print("  SUCCESS! Portal installed")
            print("=" * 70)
            print("\nNext steps:")
            print("  1. Open 'Portal' app on your phone")
            print("  2. Grant all permissions (Accessibility, Storage)")
            print("  3. Keep the app running in background")
            print("  4. Run: python gmail_recruiter_agent.py")
            return True
        else:
            print(f"\n[ERROR] Installation failed")
            if result.stderr:
                print(f"Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"\n[ERROR] {e}")
        return False

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\nCancelled")
        sys.exit(1)
