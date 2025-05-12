from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)

PORT = 3000
FILES_DIR = os.path.join(os.path.dirname(__file__), 'files')


if not os.path.exists(FILES_DIR):
    os.makedirs(FILES_DIR)


def get_next_file_name():
    files = [f for f in os.listdir(FILES_DIR) if f.endswith('.json')]
    return f"{len(files) + 1}.json"


@app.route('/files', methods=['POST'])
def create_file():
    file_name = get_next_file_name()
    file_path = os.path.join(FILES_DIR, file_name)
    content = request.get_json()

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(content, f, indent=2, ensure_ascii=False)
        return jsonify({"message": "Файл создан", "fileName": file_name}), 201
    except Exception as e:
        return jsonify({"error": "Ошибка при создании файла", "details": str(e)}), 500


@app.route('/files/<file_name>', methods=['PUT'])
def edit_file(file_name):
    file_path = os.path.join(FILES_DIR, file_name)

    if not os.path.exists(file_path):
        return jsonify({"error": "Файл не найден"}), 404

    new_content = request.get_json()

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(new_content, f, indent=2, ensure_ascii=False)
        return jsonify({"message": "Файл обновлен"})
    except Exception as e:
        return jsonify({"error": "Ошибка при редактировании файла", "details": str(e)}), 500


@app.route('/files/<file_name>', methods=['DELETE'])
def delete_file(file_name):
    file_path = os.path.join(FILES_DIR, file_name)

    if not os.path.exists(file_path):
        return jsonify({"error": "Файл не найден"}), 404

    try:
        os.remove(file_path)
        return jsonify({"message": "Файл удален"})
    except Exception as e:
        return jsonify({"error": "Ошибка при удалении файла", "details": str(e)}), 500


if __name__ == '__main__':
    app.run(host='localhost', port=PORT, debug=True)
