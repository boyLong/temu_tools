kill -9 $(ps -ef | pgrep captcha.api:app)
kill -9 $(ps -ef | pgrep node encrypt/temu_api.js)
kill -9 $(ps -ef | pgrep node start_server.py)