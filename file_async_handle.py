import asyncio
from sanic import Sanic
from sanic.response import json,empty
from sanic.exceptions import NotFound
import time

app = Sanic(name="pyapp")

async def task_sleep():
    print('sleep before', time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())))
    await asyncio.sleep(5)
    save_path = 'F:\\vxdocx_dir' if platform.system() == 'Windows' else '/home/sql_backup/vxdocx'
    wx = WX_doc(vx_link, save_path)
    s_path = wx.main()
    print('sleep after',  time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())))

@app.route('/', methods=['POST'])
async def post_handler(request):
    myLoop = request.app.loop
    myLoop.create_task(task_sleep())
    return json({'hello': 'world'})

if __name__ == '__main__':
    app.error_handler.add(NotFound,lambda r, e: empty(status=404))
    app.run(host='0.0.0.0', port=8008)