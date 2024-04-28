
pro_id=`ps -ef | grep captcha.api:app | grep -v grep | awk '{print $2}'`
# 判断进程id是否为空，若不为空，则杀掉进程
if [[ $pro_id != ""]];then
	echo "kill the " "captcha.api:app" "process_id is " $pro_id
	kill -9 $pro_id
fi


pro_id=`ps -ef | grep encrypt/temu_api.js | grep -v grep | awk '{print $2}'`
# 判断进程id是否为空，若不为空，则杀掉进程
if [[ $pro_id != ""]];then
	echo "kill the " "<temu_api>" "process_id is " $pro_id
	kill -9 $pro_id
fi

pro_id=`ps -ef | grep start_server.py | grep -v grep | awk '{print $2}'`
# 判断进程id是否为空，若不为空，则杀掉进程
if [[ $pro_id != ""]];then
	echo "kill the " "<start_server>" "process_id is " $pro_id
	kill -9 $pro_id
fi
