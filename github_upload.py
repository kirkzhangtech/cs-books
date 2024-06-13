import os
import subprocess

# 设置 GitHub 仓库的相关信息
github_repo = "https://github.com/kirkzhangtech/cs-books"
github_branch = "main"

# 设置本地文件夹路径
local_folder_path = r"C:\Users\kirkzhang\cs-books"

# 遍历文件夹下的 PDF 文件
pdf_files = [f for f in os.listdir(local_folder_path) if f.endswith(".pdf")]

for file_name in pdf_files:
    # 删除文件名中的空格
    new_file_name = file_name.replace(" ", "_")
    new_file_path = os.path.join(local_folder_path, new_file_name)
    os.rename(os.path.join(local_folder_path, file_name), new_file_path)

    # 检查文件大小是否小于 100MB
    file_size = os.path.getsize(new_file_path)
    max_file_size = 100 * 1024 * 1024  # 100MB
    if file_size > max_file_size:
        print(f"Skipping {new_file_name} because it's larger than 100MB.")
        continue

    # 添加文件到 Git 暂存区
    subprocess.run(["git", "add", new_file_path], check=True)

    # 提交文件到 Git 仓库
    subprocess.run(["git", "commit", "-m", f"Add {new_file_name}"], check=True)

    # 推送到 GitHub
    subprocess.run(["git", "push", "origin", github_branch], check=True)

    print(f"Pushed {new_file_name} to GitHub")

print("All eligible PDF files have been pushed to GitHub.")