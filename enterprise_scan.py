import subprocess
import os
from datetime import datetime

model = "llama3.2"
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
report_dir = "garak_reports"

# Create reports directory if it doesn't exist
if not os.path.exists(report_dir):
    os.makedirs(report_dir)

print(f"Starting Enterprise Garak Scan on {model}...")
print("This may take a few minutes. Running prompt injection and leakage probes.\n")

# Garak command targeting Ollama with specific vulnerability probes
command = [
    "garak",
    "--model_type", "ollama",
    "--model_name", model,
    "--probes", "promptinject, dan, xss", # Testing injection, jailbreaks, and cross-site scripting in outputs
    "--report_prefix", f"scan_{timestamp}",
    "--report_dir", report_dir
]

try:
    # Run the command and capture output
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    print("\n[SUCCESS] Garak scan completed successfully.")
    print(f"Reports saved to: ./{report_dir}/")
except subprocess.CalledProcessError as e:
    print(f"\n[ERROR] Garak scan failed with exit code {e.returncode}")
    print(e.stderr)
except FileNotFoundError:
    print("\n[ERROR] Garak is not installed. Run 'pip install garak' first.")