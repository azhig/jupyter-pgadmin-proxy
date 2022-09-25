import binascii
import getpass
import os
import site
import subprocess
import sys
from pathlib import Path

TIMEOUT = 120


def setup_pgadmin():
    current_dir = Path(__file__).parent.absolute()
    # add path of config_local.py for pgadmin4 config
    # watch  pgadmin4/config.py import config_local.py for more information
    config_local_path = current_dir / "config_local"
    # if you want all users use one account, then use static login and password
    # remote_user_name = "pgadmin4@pgadmin.com"
    # remote_user_password = "secret"
    remote_user_name = getpass.getuser()
    remote_user_password = binascii.hexlify(os.urandom(12)).decode("ascii")
    os.environ["PGADMIN_SETUP_EMAIL"] = remote_user_name
    os.environ["PGADMIN_SETUP_PASSWORD"] = remote_user_password
    # setup pgadmin to start it in server mode
    pgadmin_path = Path(site.getsitepackages()[0]) / "pgadmin4"
    setup_path = pgadmin_path / "setup.py"
    subprocess.call([sys.executable, setup_path])

    def _get_pgadmin_cmd(port):
        if sys.platform.startswith(("linux", "darwin")):
            gunicorn_path = Path(sys.executable).parent / "gunicorn"
            cmd = [
                "/usr/bin/env",
                f"PYTHONPATH={str(config_local_path)}",
                str(gunicorn_path),
                "-b",
                f"127.0.0.1:{port}",
                "-e",
                "SCRIPT_NAME={base_url}pgadmin",
                "--chdir",
                str(pgadmin_path),
                "pgAdmin4:app",
            ]
        elif sys.platform.startswith("win32"):
            cmd = [
                "waitress-serve",
                "--listen",
                f"127.0.0.1:{port}",
                "pgadmin4.pgAdmin4:app",
            ]
        else:
            raise OSError("OS is not supported")

        return cmd

    icon_path = current_dir / "icons" / "pgadmin.svg"
    return {
        "command": _get_pgadmin_cmd,
        "timeout": TIMEOUT,
        "new_browser_tab": True,
        "absolute_url": True,
        "request_headers_override": {"REMOTE_USER": remote_user_name},
        "launcher_entry": {
            "title": "PgAdmin",
            "icon_path": str(icon_path),
            "enabled": True,
        },
    }
