# Installation Guide: Raspberry Pi 5 Edge AI Deployment

## 1. Prerequisites & Hardware Requirements
- **Host**: Raspberry Pi 5 (4 GB RAM recommended)
- **OS**: Debian GNU/Linux 13 (Trixie) aarch64
- **Power**: Official 27W USB-C PD Power Supply (5.1V / 5.0A)
- **Cooling**: Active Cooler attached to the fan header

---

## 2. Environment Setup (Offline Self-Sufficient)
All dependencies are pre-cached locally on the Raspberry Pi in `/home/juice/.cache/wheelhouse`.

```bash
# Navigate to the workspace
cd ~/yolo_inference

# Activate the local virtual environment
source .venv/bin/activate

# Install all pinned dependencies from the local wheelhouse
pip install --no-index --find-links ~/.cache/wheelhouse -r requirements.txt
```

---

## 3. Verifying Installation
Execute the quick verification command:
```bash
python3 -c "import torch, cv2, ultralytics, onnxruntime; print('All core libraries verified!')"
```

Expected output:
```
All core libraries verified!
```

---

## 4. Hardware Verification
Check camera and SoC sensors:
```bash
# Check USB devices
lsusb

# Check video capture nodes
v4l2-ctl --list-devices

# Check CPU temperature sensor
cat /sys/class/thermal/thermal_zone0/temp
```
