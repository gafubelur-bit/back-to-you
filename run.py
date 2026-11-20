"""
Root convenience launcher for Back to You Global Lost & Found Management System.
Allows running the project seamlessly from either the repository root or the group-no1 directory.
"""

import sys
from pathlib import Path
from runpy import run_path

# Add group-no1 to Python path
PROJECT_DIR = Path(__file__).resolve().parent / "group-no1"
if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

if __name__ == "__main__":
    run_path(str(PROJECT_DIR / "run.py"), run_name="__main__")
