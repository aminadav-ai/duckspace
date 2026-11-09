#!/usr/bin/env python3
"""
Validate a MicroDuck .ONNX locomotion or trick policy for compatibility
with the DuckSpace.org 3D Home Physics Lab (MuJoCo WASM 50Hz).

Usage:
    python3 examples/validate_onnx.py policies/BEST_alpha_walking.onnx
"""

import sys
import numpy as np

try:
    import onnxruntime as ort
except ImportError:
    print("Please install onnxruntime first: pip install onnxruntime numpy")
    sys.exit(1)

EXPECTED_OBS_LEN = 61
EXPECTED_ACT_LEN = 14


def validate_onnx(path: str) -> None:
    print(f"Checking ONNX policy: {path}")
    sess = ort.InferenceSession(path, providers=["CPUExecutionProvider"])
    inputs = sess.get_inputs()
    outputs = sess.get_outputs()

    if len(inputs) != 1 or len(outputs) != 1:
        raise ValueError(f"Expected 1 input and 1 output, got {len(inputs)} inputs / {len(outputs)} outputs")

    in_name = inputs[0].name
    out_name = outputs[0].name

    test_obs = np.zeros((1, EXPECTED_OBS_LEN), dtype=np.float32)
    out = sess.run([out_name], {in_name: test_obs})[0]

    if out.shape != (1, EXPECTED_ACT_LEN):
        raise ValueError(f"Invalid output shape {out.shape}, expected (1, {EXPECTED_ACT_LEN})")

    print(f"OK! Valid DuckSpace.org policy:")
    print(f"  Input : {in_name} -> shape (1, {EXPECTED_OBS_LEN}) float32")
    print(f"  Output: {out_name} -> shape {out.shape} float32")
    print("Ready to upload and test at https://duckspace.org")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 examples/validate_onnx.py <path-to-policy.onnx>")
        sys.exit(1)
    validate_onnx(sys.argv[1])
