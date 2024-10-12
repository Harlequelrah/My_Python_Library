import os
import shutil
import sys
import subprocess


def startproject(project_name):
    project_path = os.path.join(os.getcwd(), project_name)
    os.makedirs(project_path, exist_ok=True)

    # Initialise le dépôt Git
    subprocess.run(["git", "init", project_path])
    print(f"Git repo initialized in {project_path}")

    with open(f"{project_path}/__init__.py", "w") as f:
        f.write("# __init__.py\n")

    sub_project_path = os.path.join(project_path, project_name)
    os.makedirs(sub_project_path, exist_ok=True)

    settings_path = os.path.join(sub_project_path, "settings")
    os.makedirs(settings_path, exist_ok=True)

    script_dir = os.path.dirname(os.path.realpath(__file__))
    source_settings_path = os.path.join(script_dir, "settings")

    if os.path.exists(source_settings_path):
        shutil.copytree(source_settings_path, settings_path, dirs_exist_ok=True)
        print("Le dossier settings a été copié avec succès.")
    else:
        print("Le dossier source 'settings' est introuvable.")

    print(f"Le projet {project_name} a été créé avec succès.")


def startapp(app_name):
    parent_dir = os.getcwd()
    project_folders = [
        f
        for f in os.listdir(parent_dir)
        if os.path.isdir(os.path.join(parent_dir, f)) and not f.startswith(".")
    ]

    if not project_folders:
        print("Aucun projet trouvé. Veuillez d'abord créer un projet.")
        return

    project_folder = os.path.join(parent_dir, project_folders[0])
    app_path = os.path.join(project_folder, app_name)
    os.makedirs(app_path, exist_ok=True)

    script_dir = os.path.dirname(os.path.realpath(__file__))
    sqlapp_path = os.path.join(script_dir, "sqlapp")

    if os.path.exists(sqlapp_path):
        shutil.copytree(sqlapp_path, app_path, dirs_exist_ok=True)
        print(f"L'application {app_name} a été créée avec succès.")
    else:
        print("Le dossier 'sqlapp' est introuvable.")


def generate_appuser():
    parent_dir = os.getcwd()
    project_folders = [
        f
        for f in os.listdir(parent_dir)
        if os.path.isdir(os.path.join(parent_dir, f)) and not f.startswith(".")
    ]

    if not project_folders:
        print("Aucun projet trouvé. Veuillez d'abord créer un projet.")
        return

    project_folder = os.path.join(parent_dir, project_folders[0])
    appuser_path = os.path.join(project_folder, "appuser")
    os.makedirs(appuser_path, exist_ok=True)

    script_dir = os.path.dirname(os.path.realpath(__file__))
    appuser_source = os.path.join(script_dir, "appuser")

    if os.path.exists(appuser_source):
        shutil.copytree(appuser_source, appuser_path, dirs_exist_ok=True)
        print("Le contenu de 'appuser' a été copié avec succès.")
    else:
        print("Le dossier source 'appuser' est introuvable.")


def runserver():
    parent_dir = os.getcwd()
    project_folders = [
        f
        for f in os.listdir(parent_dir)
        if os.path.isdir(os.path.join(parent_dir, f)) and not f.startswith(".")
    ]

    if not project_folders:
        print("Aucun projet trouvé. Veuillez d'abord créer un projet.")
        return

    project_folder = os.path.join(parent_dir, project_folders[0])
    sub_project_folder = os.path.join(project_folder, project_folders[0])
    settings_folder = os.path.join(sub_project_folder, "settings")
    main_file_path = os.path.join(settings_folder, "__main__.py")
    if os.path.exists(settings_folder):
        print(main_file_path)
        module_path = f"{project_folders[0]}.{project_folders[0]}.settings.__main__"
        subprocess.run(
            [
                "uvicorn",
                f"{module_path}:app",
                "--reload",
                "--host",
                "127.0.0.1",
                "--port",
                "8000",
            ]
        )
    else:
        print("Le fichier main.py est introuvable dans le projet.")


def main():
    if len(sys.argv) < 2:
        print("Usage: harlequelrah_fastapi <commande> <nom>")
        sys.exit(1)
    if len(sys.argv) > 2:
        name = sys.argv[2]
    command = sys.argv[1]

    if command == "startproject":
        startproject(name)
    elif command == "startapp":
        startapp(name)
    elif command == "generate" and name == "appuser":
        generate_appuser()
    elif command == "runserver":
        runserver()
    else:
        print(f"Commande inconnue: {command}")


if __name__ == "__main__":
    main()
