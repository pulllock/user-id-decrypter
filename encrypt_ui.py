import csv
import tkinter
from tkinter import filedialog
from tkinter import messagebox

from aes_decrypter import AesEncrypterDecrypter

window = tkinter.Tk()
window.title("加密用户id")
window.geometry("200x50")


def open_file_dialog():
    file_name = tkinter.filedialog.askopenfilename()
    if not file_name.endswith(".csv"):
        messagebox.showerror("错误", "请选择csv文件！")
        return

    try:
        with open("encrypted_user_id.csv", "w", encoding="utf-8", newline="") as out_file:
            with open(file_name, "r") as in_file:
                reader = csv.reader(in_file)
                writer = csv.writer(out_file, dialect=("excel"))
                for row in reader:
                    user_id = row[0]
                    encrypter = AesEncrypterDecrypter(key="1234567890123456")
                    encrypted_user_id = encrypter.encrypt(user_id)
                    user_ids = [encrypted_user_id]
                    writer.writerow(user_ids)
    except Exception as err:
        messagebox.showerror("错误", err)
        return

    messagebox.showinfo("完成", "加密完成！")


button = tkinter.Button(window, text="选择要加密的文件", width=15, height=2, command=open_file_dialog)
button.pack()

window.mainloop()
