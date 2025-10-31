import sys
import subprocess
import os

def configure_env(caper_dir):
    if caper_dir not in sys.path:
        sys.path.append(caper_dir)

    # Source the config.sh file and capture the environment
    result = subprocess.run(
        ['bash', '-c', f'source {caper_dir}/../config.sh && env'],
        capture_output=True,
        text=True
    )

    # Check for errors
    if result.returncode != 0:
        print("Error sourcing config.sh:\n", result.stderr)
    else:
        print("config.sh sourced successfully!")

    # Parse the environment variables
    for line in result.stdout.strip().split('\n'):
        if '=' in line:
            key, value = line.split('=', 1)
            os.environ[key] = value