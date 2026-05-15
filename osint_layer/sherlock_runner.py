import subprocess

def run_sherlock(username: str) -> dict:

    try:
        command = [
             "python",
            "sherlock/sherlock_project/sherlock.py",
            username,
            "--print-found",
            "--no-color"
        ]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=180
        )

        output_lines = result.stdout.splitlines()
        accounts = []

        for line in output_lines:
            line = line.strip()

            if line.startswith("[+]"):
                parts = line[4:].split(": ", 1)

                if len(parts) == 2:
                    platform = parts[0].strip()
                    url = parts[1].strip()

                    accounts.append({
                        "platform": platform,
                        "url": url
                    })

        return {
            "status": "success",
            "total_found": len(accounts),
            "accounts": accounts
        }

    except subprocess.TimeoutExpired:
        return {"status": "error", "accounts": [], "total_found": 0}

    except Exception:
        return {"status": "error", "accounts": [], "total_found": 0}