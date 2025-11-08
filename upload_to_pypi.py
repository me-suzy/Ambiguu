#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Upload package to PyPI using API Token

PyPI no longer supports username/password authentication.
You need to create an API token at: https://pypi.org/manage/account/token/

Usage:
    python upload_to_pypi.py YOUR_API_TOKEN
"""

import sys
import subprocess
from pathlib import Path

def upload_to_pypi(token):
    """Upload package to PyPI using API token"""
    dist_dir = Path(__file__).parent / "dist"
    
    if not dist_dir.exists():
        print("ERROR: dist/ folder not found. Run 'python -m build' first.")
        return False
    
    files = list(dist_dir.glob("*.whl")) + list(dist_dir.glob("*.tar.gz"))
    if not files:
        print("ERROR: No distribution files found in dist/")
        return False
    
    print("=" * 60)
    print("Uploading to PyPI...")
    print("=" * 60)
    print()
    
    # Use __token__ as username and token as password
    cmd = [
        sys.executable, "-m", "twine", "upload",
        "--username", "__token__",
        "--password", token,
        "dist/*"
    ]
    
    try:
        result = subprocess.run(cmd, check=True)
        print()
        print("=" * 60)
        print("✅ Upload successful!")
        print("=" * 60)
        print()
        print(f"Package available at: https://pypi.org/project/bebe-task-recorder/")
        return True
    except subprocess.CalledProcessError as e:
        print()
        print("=" * 60)
        print("❌ Upload failed!")
        print("=" * 60)
        print()
        print("Make sure you have:")
        print("1. Created an API token at: https://pypi.org/manage/account/token/")
        print("2. Used the token (starts with 'pypi-') as the password")
        print("3. Username should be '__token__'")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("=" * 60)
        print("BEBE Task Recorder - PyPI Upload")
        print("=" * 60)
        print()
        print("PyPI requires API Token authentication.")
        print()
        print("Steps:")
        print("1. Go to: https://pypi.org/manage/account/token/")
        print("2. Create a new API token")
        print("3. Copy the token (starts with 'pypi-')")
        print("4. Run: python upload_to_pypi.py YOUR_TOKEN")
        print()
        print("Example:")
        print("  python upload_to_pypi.py pypi-AgEIcGl...")
        print()
        sys.exit(1)
    
    token = sys.argv[1]
    if not token.startswith("pypi-"):
        print("WARNING: Token should start with 'pypi-'")
        response = input("Continue anyway? (y/n): ")
        if response.lower() != 'y':
            sys.exit(1)
    
    success = upload_to_pypi(token)
    sys.exit(0 if success else 1)

