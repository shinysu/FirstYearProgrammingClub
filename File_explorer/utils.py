import os
import shutil
import re


def find_all_subdirectories(path, filter_expr):
    directories = []
    files = {}
    total_files = 0
    total_directories = 0
    total_file_size = 0
    expr = replace_wildcards(filter_expr)
    items = os.scandir(path)
    for item in items:
        if item.is_dir():
            if re.match(expr, item.name):
                total_directories += 1
                directories.append(item.name)
        elif item.is_file():
            if re.match(expr, item.name):
                total_files += 1
                file_size = item.stat().st_size
                files[item.name] = file_size
                total_file_size += file_size
    free_disk_space = shutil.disk_usage(path)[2]
    stats = {'total_files': total_files, 'total_directories': total_directories, 'total_file_size': total_file_size,
             'free_disk_space': free_disk_space}
    return directories, files, stats


def find_files(path, filter_expr):
    files = {}
    total_files = 0
    total_file_size = 0
    expr = replace_wildcards(filter_expr)
    items = os.scandir(path)
    for item in items:
        if item.is_file() and re.match(expr, item.name):
            total_files += 1
            file_size = item.stat().st_size
            files[item.name] = file_size
            total_file_size += file_size
    free_disk_space = shutil.disk_usage(path)[2]
    stats = {'total_files': total_files, 'total_file_size': total_file_size, 'free_disk_space': free_disk_space}
    return files, stats


def replace_wildcards(filter_expr):
    return filter_expr.replace('?', '.').replace('*', '.+')