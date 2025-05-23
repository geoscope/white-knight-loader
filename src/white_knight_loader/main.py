import sys

# Command line argument required: source file path
if (len(sys.argv) < 2):
    print("Please provide a source file path, e.g. python main.py /tmp/cve")
    sys.exit()

print("\nProcessing path: ", sys.argv[1])