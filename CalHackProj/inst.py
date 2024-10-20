import subprocess
import sys

# List of packages to install
packages = ["embedchain", "python-dotenv"]

# Install packages using pip
for package in packages:
    subprocess.check_call(["pip", "install", package])

    print(sys.version)