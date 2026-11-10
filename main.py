#!/usr/bin/env python3
"""
Main Application Entry Point for Edge AI & Embedded Vision Systems.
Provides unified CLI access for M1 Detect and M2 Optimize pipelines.
"""

import os
import sys

# Auto-switch to project virtual environment if run under system python
_venv_python = os.path.abspath(os.path.join(os.path.dirname(__file__), ".venv/bin/python"))
if os.path.exists(_venv_python) and os.path.realpath(sys.executable) != os.path.realpath(_venv_python):
    os.execv(_venv_python, [_venv_python] + sys.argv)

import argparse
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("MainEntry")


def main():
    parser = argparse.ArgumentParser(
        description="Edge AI & Embedded Vision Inspection System - Individual Assessment (M1 & M2)"
    )
    parser.add_argument(
        "--mode",
        type=str,
        default="baseline",
        choices=["baseline", "optimized", "benchmark-m1", "benchmark-m2", "export-onnx", "capture"],
        help="Execution mode",
    )
    parser.add_argument("--device", type=int, default=0, help="Camera device index")
    parser.add_argument("--conf", type=float, default=0.40, help="Confidence threshold")
    parser.add_argument("--headless", action="store_true", help="Run without GUI window")
    parser.add_argument("--frames", type=int, default=None, help="Number of frames to process")
    parser.add_argument("--iterations", type=int, default=50, help="Benchmark iterations")
    parser.add_argument("--warmup", type=int, default=10, help="Benchmark warm-up runs")
    args = parser.parse_args()

    if args.mode == "baseline":
        logger.info("Starting M1 Baseline YOLOv8 Detection Pipeline...")
        from src.detection.detector import run_pipeline
        run_pipeline(
            weights_path="models/best.pt",
            device_index=args.device,
            conf_threshold=args.conf,
            headless=args.headless,
            max_frames=args.frames,
        )

    elif args.mode == "optimized":
        logger.info("Starting M2 Optimized ONNX Runtime Pipeline...")
        from src.detection.inference import get_inference_engine
        from src.camera.camera_manager import CameraManager
        cam = CameraManager(device_index=args.device, auto_fallback_simulation=True)
        engine = get_inference_engine(backend="onnx", weights_path="models/optimized/best.onnx", conf=args.conf)
        ret, frame = cam.read()
        if ret and frame is not None:
            res = engine.predict(frame)
            logger.info(f"Detected: {res['count']} | Latency: {res['inference_time_ms']:.1f}ms")
        cam.release()

    elif args.mode == "benchmark-m1":
        logger.info("Executing M1 Baseline Benchmark...")
        from src.detection.benchmark import run_baseline_benchmark
        run_baseline_benchmark(iterations=args.iterations, warmup=args.warmup)

    elif args.mode == "benchmark-m2":
        logger.info("Executing M2 Comparative Benchmark (PyTorch vs ONNX Runtime)...")
        from src.optimization.benchmark_comparison import execute_full_comparison
        execute_full_comparison(iterations=args.iterations, warmup=args.warmup)

    elif args.mode == "export-onnx":
        logger.info("Executing M2.1 ONNX Export...")
        from src.optimization.export_onnx import export_and_validate
        export_and_validate()

    elif args.mode == "capture":
        logger.info("Executing M1.1 Camera Capture...")
        from src.camera.capture import main as capture_main
        capture_main()


if __name__ == "__main__":
    main()
