from pathlib import Path
import shutil
import argparse
import os


DEFAULT_SOURCE = Path.cwd()
DEFAULT_DESTINATION = Path("./dist")


def copy_files(source, destination):
    source_folder = Path(source) if source else DEFAULT_SOURCE
    destination_folder = Path(destination) if destination else DEFAULT_DESTINATION

    if not destination_folder.exists():
        print("Destination folder was created in the current directory")
        destination_folder.mkdir()

    for current_path in source_folder.iterdir():
        if current_path.is_dir():
            copy_files(current_path, destination_folder)
        else:
            has_access = check_access(current_path)
            is_new_folder_path = create_folder_by_extension(
                current_path, destination_folder
            )
            if has_access and is_new_folder_path:
                copy_path = check_dublicates(current_path, is_new_folder_path)

                shutil.copy(current_path, copy_path)


def create_folder_by_extension(file_path, destination_folder):
    file_extension = file_path.suffix.lower()

    if file_extension:
        folder_path = destination_folder.joinpath(file_extension[1:])

        if not folder_path.exists():
            folder_path.mkdir()

        return folder_path

    return None


def check_access(file_path):
    try:
        # Check access to read / write / execite current file
        os.access(file_path, os.R_OK | os.W_OK | os.X_OK)
        return True

    except Exception as e:
        print(f"No access rights: {e}")
        return False


def check_dublicates(file_path, destination_folder):
    file_name = file_path.stem
    file_extension = file_path.suffix

    copy_path = destination_folder / f"{file_name}{file_extension}"

    index = 1
    while copy_path.exists():
        unique_name = f"{file_name}_copy_{index}"
        copy_path = destination_folder / f"{unique_name}{file_extension}"
        index += 1

    return copy_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copying files")

    parser.add_argument(
        "--source", type=str, help="The path to the source directory", required=False
    )
    parser.add_argument(
        "--destination",
        type=str,
        help="The path to the destination directory",
        required=False,
    )

    args = parser.parse_args()

    copy_files(args.source, args.destination)
    print("Copying is complete 🎉")
