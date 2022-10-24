from datetime import datetime
import os

# Get directory name
month = datetime.now().strftime("%b") # Get month
year = datetime.now().year # Get year

directory = f"{month} {year}"

# TODO Get path
parent = "C:\\Users\\redexe\\OneDrive\\Documents\\Receipts"

# Make directory if possible
try:
  os.mkdir(os.path.join(parent, directory))
  print(f"Created directory '{directory}' in {parent}")
except:
  print(f"Directory '{directory}' in {parent} already exists")