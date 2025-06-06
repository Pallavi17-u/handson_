import subprocess

def run_command(command):
    try:
        # subprocess.run() returns a CompletedProcess instance
        result = subprocess.run(
            command, 
            shell=True, 
            check=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Command '{command}' failed with error:\n{e.stderr}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    output = run_command("ls -l")
    if output is not None:
        print(output)
