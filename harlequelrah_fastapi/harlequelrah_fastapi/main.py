import os
import argparse
import subprocess


def init_project():
    # Créez le fichier main.py
    with open("main.py", "w") as f:
        f.write("# main.py\n")

    # Créez le dossier routes avec __init__.py
    os.makedirs("routes", exist_ok=True)
    with open("routes/__init__.py", "w") as f:
        f.write("# __init__.py\n")

    # Créez le dossier sqlapp avec __init__.py et ses sous-dossiers
    os.makedirs("sqlapp", exist_ok=True)
    with open("sqlapp/__init__.py", "w") as f:
        f.write("# __init__.py\n")

    os.makedirs("sqlapp/Authentication", exist_ok=True)
    with open("sqlapp/Authentication/__init__.py", "w") as f:
        f.write("# __init__.py\n")
    with open("sqlapp/Authentication/authenticate.py", "w") as f:
        f.write("# authenticate.py\n")
    with open("sqlapp/Authentication/secret.py", "w") as f:
        f.write("# secret.py\n")

    os.makedirs("sqlapp/Cruds", exist_ok=True)
    with open("sqlapp/Cruds/__init__.py", "w") as f:
        f.write("# __init__.py\n")

    os.makedirs("sqlapp/Database", exist_ok=True)
    with open("sqlapp/Database/__init__.py", "w") as f:
        f.write("# __init__.py\n")
    with open("sqlapp/Database/database.py", "w") as f:
        f.write("# database.py\n")

    os.makedirs("sqlapp/Models", exist_ok=True)
    with open("sqlapp/Models/__init__.py", "w") as f:
        f.write("# __init__.py\n")
    with open("sqlapp/Models/models.py", "w") as f:
        f.write("# models.py\n")

    os.makedirs("sqlapp/Schemas", exist_ok=True)
    with open("sqlapp/Schemas/__init__.py", "w") as f:
        f.write("# __init__.py\n")
    with open("sqlapp/Schemas/schemas.py", "w") as f:
        f.write("# schemas.py\n")

    # Initialisez Alembic
    subprocess.run(["alembic", "init", "alembic"])


def main():
    parser = argparse.ArgumentParser(prog="harlequelrah_fastapi")
    subparsers = parser.add_subparsers(dest="command")

    init_parser = subparsers.add_parser("init")
    init_parser.add_argument("project", help="Initialise un nouveau projet")

    args = parser.parse_args()

    if args.command == "init":
        init_project()


if __name__ == "__main__":
    main()
