# Smart Clipboard & Notes - Android APK Builder

This repository contains the Python application code, Buildozer configuration, and an automated GitHub Actions workflow to build a downloadable Android APK directly in the cloud (no heavy local Android Studio required).

---

## 🚀 How to Build & Download Your APK in 3 Steps

### 1. Push This Repository to GitHub
Create a new GitHub repository and push these files:
```bash
git init
git add .
git commit -m "Initial commit of Smart Clipboard & Notes"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/clipboardhub.git
git push -u origin main
```

### 2. Automated Cloud Build Trigger
- Go to the **Actions** tab on your GitHub repository.
- You will see the workflow **"Build Android APK with Buildozer"** running automatically on GitHub's cloud servers.
- The build process takes approximately 10–15 minutes for the first compilation (caches SDK/NDK for fast future builds).

### 3. Download Your APK
- Click into the completed workflow run.
- Scroll down to the **Artifacts** section at the bottom.
- Click **`clipboardhub-debug-apk`** to download your ready-to-install Android APK file!
- Transfer the `.apk` to your Android phone, enable *Install Unknown Apps* if prompted, and tap to install.

---

## 📱 Testing Locally on Mobile with Pydroid 3
If you want instant on-device testing before compiling the APK:
1. Install **Pydroid 3** and the **Pydroid repository plugin** from Google Play Store.
2. In Pydroid 3, open the menu (three bars) ➔ **Pip** ➔ Quick install or search for:
   ```
   kivy, pyperclip
   ```
3. Paste the contents of `main.py` into Pydroid 3.
4. Tap the yellow **Play (▶)** button to launch your app natively on your phone screen!

---

## ⚙️ App Configuration Details
- **App Name:** `Smart Clipboard & Notes`
- **Package:** `org.mobileapps.clipboardhub`
- **Version:** `1.0.0`
- **Requirements:** `python3, kivy, pyperclip`
- **Target Android SDK:** `34`
- **Orientation:** `portrait`
