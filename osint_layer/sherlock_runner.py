import subprocess


def run_sherlock(username: str) -> dict:
    """
    Runs Sherlock CLI and parses found accounts into structured format.
    """

    try:
        # Command to run installed Sherlock
        command = [
            "sherlock",
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

        # If sherlock is not installed
        if result.returncode != 0 and "not recognized" in result.stderr.lower():
            return {
                "status": "error",
                "message": "Sherlock is not installed or not in PATH."
            }

        output_lines = result.stdout.splitlines()
        accounts = []

        for line in output_lines:
            line = line.strip()

            # Sherlock prints found accounts like:
            # [+] Instagram: https://instagram.com/username
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
            "username": username,
            "total_found": len(accounts),
            "accounts": accounts,
            "status": "success"
        }

    except subprocess.TimeoutExpired:
        return {
            "status": "error",
            "message": "Sherlock timed out."
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


# -----------------------------------------
# Standalone Execution Support
# -----------------------------------------

if __name__ == "__main__":
    username = input("Enter username to search: ").strip()

    result = run_sherlock(username)

    print("\n===== SHERLOCK RESULTS =====\n")

    if result["status"] == "success":
        print("Username:", result["username"])
        print("Total Accounts Found:", result["total_found"])
        print()

        for account in result["accounts"]:
            print(f"{account['platform']}: {account['url']}")

    else:
        print("Error:", result["message"])