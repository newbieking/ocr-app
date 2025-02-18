# EasyOCR + Flask 图片文字识别项目

## 项目简介
本项目结合了 `EasyOCR` 和 `Flask` 框架，实现了一个简单的图片文字识别应用程序。用户可以通过上传图片，应用程序将使用 `EasyOCR` 识别图片中的文字内容并返回识别结果。

## 功能特点
- 支持多种图片格式的上传。
- 利用 `EasyOCR` 强大的文字识别能力，可识别多种语言的文字。
- 基于 `Flask` 框架，提供简单易用的 Web 接口。

## 环境要求
- Python 3.8.10
- 所需 Python 库：
  - `Flask`：用于构建 Web 应用程序。
  - `easyocr`：用于图片文字识别。
  - `Pillow`：用于处理图片数据。

## 安装步骤
1. **克隆项目代码**
```bash
git clone https://github.com/newbieking/ocr-app.git
cd ocr-app

## 开始
### Windows
```ps1
python -m venv venv
venv\Scripts\activate
```
### Linux/Mac
```ps1
python3 -m venv venv
source venv/bin/activate
```

## 安装依赖库
```ps1
pip install -r requirements.txt
```

## 启动
```ps1
python server-app.py
```

应用启动后，会在终端显示运行地址，默认是 http://127.0.0.1:5000

### 上传图片进行识别
- 打开浏览器，访问 http://127.0.0.1:5000，会看到一个简单的文件上传表单。
- 点击 “选择文件” 按钮，选择要识别的图片文件。
- 点击 “上传” 按钮，应用程序将上传图片并进行文字识别。
- 识别完成后，页面将显示识别出的文字内容。
