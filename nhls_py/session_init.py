import json
from importlib.resources import files
from pathlib import Path
import subprocess
from . import nhls_path


def check_rustup_present():
    try:
        subprocess.run(["rustup"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        return False


def session_init(nhls_path_override=None):
    # Load NHLS version information
    nhls_version_path = files("nhls_py") / "nhls_version.json"
    print(f"nhls_version_path: {nhls_version_path}")
    with open(nhls_version_path, "r") as f:
        nhls_version = json.load(f)

    # Get the info we need
    nhls_branch = nhls_version["branch"]
    nhls_url = nhls_version["url"]
    print(f"nhls branch: {nhls_branch}, url: {nhls_url}")

    # Figure out where checkout should be
    global nhls_path
    if nhls_path_override is None:
        nhls_path = Path(nhls_path).expanduser()
    else:
        nhls_path = nhls_path_override
    print(f"nhls path: {nhls_path}")

    # TODO (rb): Add some better checks here,
    # is commit / branch what we expect?
    # For now though, I don't care
    if nhls_path.exists():
        print("  exists")
    else:
        print("nhls checkout does not exist, cloning...")
        clone_args = [
            "git",
            "clone",
            "--branch",
            nhls_branch,
            "--",
            nhls_url,
            nhls_path,
        ]
        subprocess.run(
            clone_args,
            cwd=nhls_path.parent,
            capture_output=False,
            text=True,
            check=True,
        )

    # Check that rustup is present
    if check_rustup_present():
        print("found rustup...")
    else:
        print("please install rustup!")
        print("https://rustup.rs")
        raise ValueError("Rustup not installed")

    # Ensure correct toolchain is present
    print("checking toolchain...")
    tool_args = [
        "rustup",
        "toolchain",
        "install",
    ]
    subprocess.run(
        tool_args, cwd=nhls_path, capture_output=False, text=True, check=True
    )

    # Run cargo build now
    # get all the incremental build benefits later
    print("building dependencies...")
    build_args = [
        "cargo",
        "build",
        "--release",
    ]
    subprocess.run(
        build_args, cwd=nhls_path, capture_output=False, text=True, check=True
    )

    # Done
    print("nhls_py is ready to go")
