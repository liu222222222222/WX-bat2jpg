from pathlib import Path
import struct
import tkinter as tk
from tkinter import filedialog
from Crypto.Cipher import AES
from Crypto.Util import Padding

# ---------- 密钥 ----------
AES_KEY = 1
XOR_KEY = 1

# ---------- 解密 ----------
def decrypt_dat_v4(path):
    with open(path, "rb") as f:
        header = f.read(0x0F)
        if len(header) != 0x0F:
            raise ValueError("头不足 15 字节")
        _, aes_size, xor_size = struct.unpack("<6sLLx", header)
        aes_size += 16 - aes_size % 16
        body = f.read()
        aes_data = body[:aes_size]
        raw_data = body[aes_size:-xor_size] if xor_size else body[aes_size:]
        xor_data = body[-xor_size:] if xor_size else b''
        xored = bytes(b ^ XOR_KEY for b in xor_data)
    cipher = AES.new(AES_KEY, AES.MODE_ECB)
    plain = Padding.unpad(cipher.decrypt(aes_data), 16)
    return plain + raw_data + xored

# ---------- 主流程 ----------
def main():
    tk.Tk().withdraw()
    root = Path(filedialog.askdirectory(title='选择含“类似9e20f478899ed29eb19741386f92143c8”的 DAT 根目录'))
    if not root:
        return

    export_dir = root / "导出"
    export_dir.mkdir(exist_ok=True)

    total = 0
    for date_folder in root.iterdir():
        if not date_folder.is_dir() or date_folder.name == "导出":
            continue
        date_str = date_folder.name
        dat_files = sorted(date_folder.glob("Img/*.dat"))
        for idx, dat in enumerate(dat_files, 1):
            try:
                jpg = decrypt_dat_v4(dat)
                jpg_path = export_dir / f"{date_str}-{idx:02d}.jpg"
                jpg_path.write_bytes(jpg)
                total += 1
                print(f"[✓] {jpg_path.name}")
            except Exception as e:
                print(f"[✗] {dat.name} 原因：{e}")

    print(f"\n🎉 完成！共导出 {total} 张图片到 {export_dir}")

if __name__ == "__main__":
    main()