from flask import Flask, jsonify
import docker
from mongoengine import connect

app = Flask(__name__)

# Підключення до MongoDB
connect(host="mongodb://mongo:27017/mydb")

@app.route('/test', methods=['GET'])
def test():
    client = docker.from_env()
    containers = client.containers.list()
    containers_list = [{"name": container.name, "status": container.status} for container in containers]
    return jsonify({"containers": containers_list, "db_status": "connected"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
