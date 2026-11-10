# Troubleshooting Guide: Edge AI Inspection System

## 1. Camera Issues

### 1.1 Physical Webcam Not Detected
- **Symptom**: `CameraManager` outputs `[SIMULATION FALLBACK] No physical camera recognized on /dev/video0`.
- **Diagnostic Command**:
  ```bash
  lsusb
  v4l2-ctl --list-devices
  ```
- **Resolution**:
  1. Plug USB webcam into a blue USB 3.0 port or black USB 2.0 port.
  2. Verify that the camera device is recognized in `lsusb`.
  3. Verify permissions: ensure current user belongs to the `video` group:
     ```bash
     sudo usermod -aG video $USER
     ```

---

## 2. Model & Checkpoint Issues

### 2.1 RuntimeError: data.pkl not in a subdirectory
- **Cause**: PyTorch C++ zip reader requires internal files to reside under an `archive/` prefix.
- **Resolution**: The verified archive structure is provided in `models/best.pt`. Use `models/best.pt` for all inference commands.

### 2.2 Ultralytics Settings Directory Permissions
- **Symptom**: Warning regarding `/home/juice/.config/Ultralytics/settings.json`.
- **Resolution**: The code automatically suppresses or catches read-only filesystem warnings during offline execution.

---

## 3. Performance & Thermal Management

### 3.1 High SoC Temperatures (> 80°C)
- **Symptom**: Thermal warnings during extended benchmarking.
- **Diagnostic Command**:
  ```bash
  cat /sys/class/thermal/thermal_zone0/temp
  vcgencmd measure_temp
  ```
- **Resolution**: Ensure the official Raspberry Pi 5 Active Cooler is firmly mounted and the fan connector is plugged into the 4-pin fan header.
