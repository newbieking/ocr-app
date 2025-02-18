from flask import Flask, request, render_template, send_from_directory, jsonify
import os
import detect
import log

app = Flask(__name__)

# 配置上传文件的保存目录
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['LOG_FILENAME'] = 'app.log'

# 定义允许上传的文件扩展名
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# 显示上传表单
@app.route('/')
def index():
    return render_template('upload.html')


# 处理文件上传请求
@app.route('/upload', methods=['POST'])
def upload_file():
    # 检查请求中是否包含文件
    if 'file' not in request.files:
        return '未找到文件', 400
    file = request.files['file']
    # 检查用户是否选择了文件
    if file.filename == '':
        return '未选择文件', 400
    # 检查文件扩展名是否允许
    if file and allowed_file(file.filename):
        filename = file.filename
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        text = detect.detect(file.read())
        log.logger.info(text)
        result = " ".join([it[1] for it in text])
        return jsonify({
            "result": result,
            "filename": filename,
        })
    else:
        return '不允许的文件类型', 400


# 提供上传文件的下载功能
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(debug=True)
