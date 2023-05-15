import subprocess
def is_git_repository():
    try:
        output = subprocess.check_output(['git', 'rev-parse', '--is-inside-work-tree']).strip().decode('utf-8')
        return output == 'true'
    except subprocess.CalledProcessError:
        return False
# Check if the current directory is inside a Git repository
if is_git_repository():
    print("Current directory is inside a Git repository")
else:
    print("Current directory is not inside a Git repository")