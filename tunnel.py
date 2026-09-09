import subprocess
import sys

PORT = sys.argv[1] if len(sys.argv) > 1 else 8000
print(f"Starting tunnel for port {PORT}...")

# Uses built-in SSH to route traffic through localhost.run
subprocess.run(["ssh", "-R", f"80:localhost:{PORT}", "nokey@localhost.run"])
