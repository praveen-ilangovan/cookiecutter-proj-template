"""
This script runs after cookiecutter is done setting up the project.
"""

import sys

def setup_vcs():
    """
    Initialize a git repo and do an initial commit.
    """
    print("..Setting up VCS: git")
    import subprocess

    subprocess.call(['git', 'init'])
    subprocess.call(['git', 'add', '*'])
    subprocess.call(['git', 'commit', '-m', 'Initial commit'])
    print("..VCS setup: done")

def main():
    """Main function"""
    if "{{cookiecutter.setup_vcs}}" == 'y':
        setup_vcs()

if __name__ == "__main__":
    print("Running post cookiecutter hook..")
    sys.exit(main())