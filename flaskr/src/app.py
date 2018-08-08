
from flask import render_template, jsonify
import connexion
from src import images

app = connexion.App(__name__, specification_dir='./')


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/images', methods=['GET'])
def get_all():
    return jsonify(images.get_all())


@app.route('/images/<image_name>', methods=['GET'])
def get(image_name):
    return jsonify(images.get_one(image_name))


@app.route('/images', methods=['PUT'])
def post(image_name, image_url):
    return images.create(image_name, image_url)


@app.route('/images/<image_name>', methods=['DELETE'])
def delete(image_name):
    return images.delete(image_name)


@app.route('/images/<image_name>', methods=['PUT'])
def put(image_name, up_image_name, image_url):
    return images.update(image_name, up_image_name, image_url)


if __name__ == "__main__":
    app.run(port=4555, debug=True)


