from flask import Flask, jsonify
import redis, os
app = Flask(__name__)

host = localhost


@app.route("/")

def hello():
    output = {}
    return "This will connect to " + host

@app.route('/redis/')
def info():
    output = {}
    output['GET KEY'] = "/redis/get/<key>"
    output['SET KEY'] = "/redis/set/<key>/<value>"
    output['DELETE KEY'] = "/redis/delete/<key>"
    output['HOST'] = host
    return jsonify(output)

def get_connection():
    rr = redis.ConnectionPool(host=host, port=6379, db=0)
    r = redis.Redis(connection_pool=rr)
    return r

@app.route('/redis/get/<keyname>')
def redis_get_key(keyname):
    r = get_connection()
    output = {}
    if r.exists(keyname):
        output['key'] = keyname
        output['value'] = r.get(keyname)

    else:
        output['status'] = "Failed"
        output['reason'] = "Key doesn't exists"

    return jsonify(output)

@app.route('/redis/set/<keyname>/<value>')
def redis_set_key(keyname,value):
    output = {}
    r = get_connection()
    if r.set(keyname,value) == 1:
        output['status'] = "OK"
    else:
        output['status'] = "Failed"
    return jsonify(output)


@app.route('/redis/delete/<keyname>')
def redis_del_key(keyname):
    output = {}
    r = get_connection()
    if r.exists(keyname) == 1:
        if r.delete(keyname) == 1:
            output['status'] = "Success"
        else:
            output['status'] = "Failed"
    else:
        output['status'] = "Failed"
        output['reason'] = "key doesn't exist"
    return jsonify(output)
