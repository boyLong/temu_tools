import os
import sys
import uvicorn
import subprocess
from server import app
from common.config import server_config


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.abspath(__file__)))
subprocess.Popen("node encrypt/temu_api.js", shell=True)

subprocess.Popen(f"uvicorn captcha.api:app --port {server_config['captcha_port']}", shell=True)

uvicorn.run(app, host="0.0.0.0", port=server_config['server_port'])