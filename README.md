# user-id-decrypter
使用AES对用户id进行加密的程序，支持对单个用户id进行加密和解密；支持使用图形界面对csv文件中的用户id进行批量机密并导出成加密的csv文件。

# 开始
此程序使用python进行开发，所以在运行程序之前需要将python环境安装好，python版本3.x，环境配置完成后，可以继续下面步骤。

## 获取项目

```
git clone https://github.com/dachengxi/user-id-decrypter
```



## 安装

```
pip install -r requirements.txt
```

# 使用

## 加密单个用户id

```
py encrypt_user_id.py 123456
```

## 解密单个用户id

```
py decrypt_user_id XmAdqki4dMjdid==
```

## 使用图形界面进行csv批量加密

### 安装打包exe工具

```
pip install pywin32
pip install pyinstaller
```

### 打包

```
pyinstaller -F -w -i icon.ico encrypt_ui.py
```

打包生成exe文件可在dist目录中找到。

## 贡献

暂无

## 作者

* **ChengXi** - ** - [dachengxi](https://github.com/dachengxi)

## License

This project is licensed under the MIT License！