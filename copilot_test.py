import os
import platform
import subprocess

def get_system_uptime():
    system = platform.system()
    try:
        if system == "Windows":
            # Use 'net stats srv' and parse output for uptime
            output = subprocess.check_output("net stats srv", shell=True, text=True)
            for line in output.splitlines():
                if "Statistics since" in line:
                    return f"System Uptime (Windows): {line.strip()}"
            return "Could not determine uptime on Windows."
        elif system == "Linux":
            # Read /proc/uptime
            with open("/proc/uptime") as f:
                uptime_seconds = float(f.readline().split()[0])
            hours = int(uptime_seconds // 3600)
            minutes = int((uptime_seconds % 3600) // 60)
            seconds = int(uptime_seconds % 60)
            return f"System Uptime (Linux): {hours}h {minutes}m {seconds}s"
        elif system == "Darwin":
            # Use 'uptime' command on macOS
            output = subprocess.check_output("uptime", shell=True, text=True)
            return f"System Uptime (macOS): {output.strip()}"
        else:
            return f"Unsupported OS: {system}"
    except Exception as e:
        return f"Error retrieving system uptime: {e}"

if __name__ == "__main__":
    print(get_system_uptime()
