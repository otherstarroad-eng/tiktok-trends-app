# ==============================================================================
# Google Colab 1-Click Buildozer APK Builder for "Smart Clipboard & Notes"
# Run this inside a free Google Colab notebook (Runtime -> Change runtime type -> Standard CPU)
# ==============================================================================

# Step 1: Install system packages & build tools
!sudo apt update -y
!sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev build-essential ccache

# Step 2: Install Buildozer and Cython
!pip install --upgrade pip
!pip install --upgrade "cython<3.0.0"
!pip install --upgrade buildozer

# Step 3: Write main.py and buildozer.spec
# (Make sure to upload your main.py or paste your code here)

# Step 4: Run Buildozer to compile the APK
!buildozer -v android debug

# Step 5: Locate and download the generated APK
import glob
from google.colab import files

apk_files = glob.glob("bin/*.apk")
if apk_files:
    print(f"Build successful! Downloading {apk_files[0]}...")
    files.download(apk_files[0])
else:
    print("Build finished, check bin/ folder.")
