# Camera and Repository Setup
**Milestone:** M1: Detect  
**Task:** Camera and repo  
**Max Marks:** 2 Marks  
**Student Name:** Sai Sanjay R  
**Student ID:** S20  
**GitHub Repository:** [https://github.com/SAISANJAYR/edge_ai_sai](https://github.com/SAISANJAYR/edge_ai_sai)  
**Submission Link:** [https://github.com/SAISANJAYR/edge_ai_sai/tree/main/M1_Detect/camera_and_repo](https://github.com/SAISANJAYR/edge_ai_sai/tree/main/M1_Detect/camera_and_repo)  

---

## 1. Rubric Requirement
> **"I capture a frame on the device and make my own commit with the spec sheet and first frame"**

---

## 2. Hardware Platform & Camera Specifications
The vision pipeline is deployed on a physical Raspberry Pi 5 single-board computer using a native UVC USB webcam.

| Specification Parameter | Hardware Value / Configuration |
|---|---|
| **Host System** | Raspberry Pi 5 Model B Rev 1.0 (BCM2712 SoC) |
| **CPU Architecture** | Quad-Core ARM Cortex-A76 @ 2.4 GHz (64-bit ARMv8.2-A) |
| **Operating System** | Debian GNU/Linux 13 (Trixie) ARM64 (Kernel 6.18.50+rpt-rpi-2712) |
| **System Memory** | 4.0 GiB LPDDR4X SDRAM |
| **Vision Camera** | **Logitech C270 HD Webcam** (USB UVC, Bus 001 Device 003) |
| **Linux Device Node** | `/dev/video0` (V4L2 capture device node) |
| **Native Resolution** | 640 × 480 @ 30 FPS (MJPEG / YUYV) |
| **Field of View** | 60° diagonal FOV |
| **Cooling** | Official Raspberry Pi Active Cooler (Aluminium heatsink + PWM fan) |

See full technical details in [`SPEC_SHEET.md`](./SPEC_SHEET.md).

---

## 3. Individual Proof: First Frame Capture
Captured directly on the Raspberry Pi 5 target device using `python3 capture.py` over the Linux V4L2 backend:

![First Frame Capture on Raspberry Pi 5](./first_frame_capture.jpg)

- **File:** `first_frame_capture.jpg`
- **Resolution:** 640 × 480 × 3 (BGR)
- **Capture Timestamp:** Verified on target hardware
- **Capture Backend:** `cv2.VideoCapture(0, cv2.CAP_V4L2)`

---

## 4. Execution & Verification Commands

```bash
# Clone the repository
git clone https://github.com/SAISANJAYR/edge_ai_sai.git
cd edge_ai_sai/camera_and_repo

# Run first frame capture on the device
python3 capture.py --output first_frame_capture.jpg --device 0
```

---

## 5. Git Commit Proof
- **Initial Spec Sheet & First Frame Commit:** `80e55cd` / `cde0cb6`
- **Author:** Sai Sanjay R (`juice@raspberrypi5.local`)
- **Remote:** `https://github.com/SAISANJAYR/edge_ai_sai`
