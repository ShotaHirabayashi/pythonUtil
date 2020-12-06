import re
import os
import shutil
import time
import glob


# ある拡張子を含むファイルを取得する（path, 拡張子）
def listup_files(path):
    yield [os.path.abspath(p) for p in glob.glob(path)]


# 拡張子かどうか判断
def is_exc(ext, f_path):
    for file in os.listdir(f_path):
        if file.endswith('.' + ext):
            return True
        else:
            return False


# ファイル移動
def move_file(file_name):
    """
    ダウンロードディレクトリ→操作ファイルまでファイルを移動
    param ファイル名
    ファイルパスを返却(C~ファイル名まで返却される
    """
    new_path = shutil.move('./{}'.format(file_name), './downloads')
    time.sleep(3)
    return new_path


# ファイル削除
def delete_file(download_name):
    """
    ファイルを削除する
    """
    os.remove("." + download_name)


# ファイルが存在するかチェック
def isExist(download_name):
    """
    ディレクトリにファイルがあるかチェック)
    """
    is_exist = os.path.exists("." + download_name)
    return is_exist
