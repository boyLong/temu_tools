kill -9 $(ps -ef | pgrep captcha.api:app)
kill -9 $(ps -ef | pgrep encrypt/temu_api.js)
kill -9 $(ps -ef | pgrep start_server.py)