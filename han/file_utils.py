import os

# 韩
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


def list_files(folder: str, ext: str = None, recursive: bool = False):
    """
    列出文件夹中的文件路径。

    参数：
        folder:     目标文件夹路径
        ext:        可选，按扩展名过滤，如 '.png'、'.txt'
        recursive:  是否递归遍历子文件夹

    返回：
        符合条件的文件路径列表
    """
    result = []

    if not os.path.exists(folder):
        return result

    if recursive:
        for root, _, files in os.walk(folder):
            for f in files:
                if ext is None or f.lower().endswith(ext.lower()):
                    result.append(os.path.join(root, f))
    else:
        for f in os.listdir(folder):
            full_path = os.path.join(folder, f)
            if os.path.isfile(full_path):
                if ext is None or f.lower().endswith(ext.lower()):
                    result.append(full_path)

    return result


def get_filename(path: str, with_ext: bool = True):
    """
    获取文件名。

    参数：
        path:     文件路径
        with_ext: True 返回带扩展名，False 只返回主名

    返回：
        文件名（字符串）
    """
    name = os.path.basename(path)
    if with_ext:
        return name
    else:
        return os.path.splitext(name)[0]


def get_extension(path: str):
    """
    获取文件扩展名（含点，如 '.png'）。
    """
    return os.path.splitext(path)[1]


def list_subfolders(folder: str):
    """
    列出文件夹下的所有子文件夹路径。
    """
    if not os.path.exists(folder):
        return []
    return [
        os.path.join(folder, d)
        for d in os.listdir(folder)
        if os.path.isdir(os.path.join(folder, d))
    ]


def get_file_size(path: str):
    """
    获取文件大小（字节）。
    """
    if os.path.isfile(path):
        return os.path.getsize(path)
    return 0
