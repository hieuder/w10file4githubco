import gdown

# URL file Google Drive
url = "https://drive.google.com/uc?id=1WlzOMBtITNea7X8Qu-EIo0rErRq4SAg_"

# Đường dẫn lưu file sau khi tải
output = "/mnt/win10.zip"  # Đổi tên file tùy ý

# Tải file
gdown.download(url, output, quiet=False)

print(f"File đã được tải về và lưu tại: {output}")
