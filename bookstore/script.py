# bookstore/scripts.py
def lock():
    import subprocess
    subprocess.run(["poetry", "lock", "--no-update"])
