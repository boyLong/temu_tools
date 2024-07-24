
import os
import sys
import uvicorn
import subprocess

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'temu_new'))

from common.config import server_config


if __name__ == '__main__':
    subprocess.Popen("node encrypt/temu_api.js", shell=True)
    uvicorn.run(app='temu_new.server:app', host="0.0.0.0", port=server_config['server_port'], workers=8)
