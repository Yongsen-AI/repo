import os


def create_folder_path(dir: str = ''):
    """
    若 dir 路径存在，返回 True；
    若不存在，则创建该路径，返回 False。
    """
    if os.path.exists(dir):
        return True
    else:
        os.makedirs(dir, exist_ok=True)
        return False