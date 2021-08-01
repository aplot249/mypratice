#@author: sareeliu
#@date: 2021/5/6 20:53
from flask import Flask,request,make_response,jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources=r'/*')
@app.route('/index/',methods=['POST'])
def index():
    name = request.values['name']
    passwd = request.values["passwd"]

    with open("./account.properties") as f:
        lines = f.readlines()
    print(lines)
    origin_line_num = len(lines)
    new_line_list = []
    for line in lines:
        if name == line.split(".")[0] and passwd == line.split("=")[1].rstrip("\n"):
            break
        new_line_list.append(line)
    print(new_line_list)
    current_line_num = len(new_line_list)
    with open("./account.properties",'w+') as f:
        [f.write(line) for line in new_line_list]
    if origin_line_num != current_line_num:
        t = {
            'status':'success',
            'name':name
        }
    else:
        t = {
            'status':'fail',
            'name':name
        }
    resp = make_response(jsonify(t))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
    #return json.dumps(t)

def SortData(request):
    if request.json['sort'] == 'data':
        print(request.json['reversed'])
        if request.json['reversed']:
            data = DataKiftHandle(True).sortByDate()
        else:
            data = DataKiftHandle(False).sortByDate()
    if request.json['sort'] == 'data':
        if request.json['reversed']:
            data = DataKiftHandle(True).sortByDate()
        else:
            data = DataKiftHandle(False).sortByDate()
    return json({'status': 'ok', "data": data})


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
