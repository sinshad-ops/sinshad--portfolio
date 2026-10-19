"""Standalone entry point for Multi-task AI Data Annotation."""
from pathlib import Path
import subprocess
import sys

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[2]
    raise SystemExit(subprocess.call(
        [sys.executable, str(root / "analysis.py"), "--project", "annotation", "--print"]
    ))
