import subprocess
import sys

# Get the user input
branch = input("Enter the branch name or press enter for default branch: ")

# Get the default branch name
default_branch = subprocess.run(["git", "symbolic-ref", "refs/remotes/origin/HEAD"], capture_output=True, text=True).stdout.strip().split("/")[-1]

# If no user input, switch to default branch
if not branch:
    subprocess.run(["git", "checkout", default_branch])
    print(f"Switched to {default_branch}")
    sys.exit(0)

# Get the list of remote branches
remote_branches = subprocess.run(["git", "branch", "-r"], capture_output=True, text=True).stdout.split()

# Check if the user input matches an existing branch
if f"origin/{branch}" in remote_branches:
    # Switch to the matching branch
    subprocess.run(["git", "checkout", "-t", f"origin/{branch}"])
    print(f"Switched to {branch}")
else:
    # Print an error message and exit
    print(f"No such branch: {branch}")
    sys.exit(1)