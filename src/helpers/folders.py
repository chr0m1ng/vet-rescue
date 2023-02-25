# Python imports
import os
from typing import Dict, List


UNSUPORTED_FILES = [".DS_Store"]


def build_file_struct(file: str, path: str) -> Dict[str, str]:
    return {"file_name": file, "full_path": f"{path}/{file}"}


def list_subfolders_files(path: str) -> Dict[str, List[Dict[str, str]]]:
    return {
        folder_path.removeprefix(f"{path}/"): sorted(
            [build_file_struct(file, folder_path) for file in files if file not in UNSUPORTED_FILES],
            key=lambda d: d["file_name"],
        )
        for folder_path, _, files in os.walk(path)
        if folder_path != path
    }


def list_folder_files(path: str) -> List[Dict[str, str]]:
    return [build_file_struct(file, path) for file in os.listdir(path) if file not in UNSUPORTED_FILES]
