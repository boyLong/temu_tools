import subprocess
from captcha.api import app


a = subprocess.Popen("node encrypt/temu_api.js", shell=True)



import uvicorn
uvicorn.run(app, host="0.0.0.0", port=8000)
