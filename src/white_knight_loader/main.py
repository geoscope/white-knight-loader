import sys

from white_knight_loader import wkconfig

# Load configuration
config = wkconfig.LoadConfiguration()

if not config:
    print("Failed to load configuration")
    sys.exit()

# Command line argument required: source file path
if len(sys.argv) < 2:
    print("Please provide a source file path, e.g. python main.py /tmp/cve")
    sys.exit()

print("\nProcessing path: ", sys.argv[1])
