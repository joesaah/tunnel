import subprocess
import sys

PORT = sys.argv[1] if len(sys.argv) > 1 else 8000
print(f"Starting tunnel for port {PORT}...")

# Uses built-in SSH to route traffic through localhost.run
subprocess.run([
    "ssh",
    "-p",
    "443",
    f"-R0:localhost:{PORT}",
    "qr@free.pinggy.io"
])
