# 定义需要检查的进程列表
processes=("temu_captch.api:app" "encrypt/temu_api.js" "start_server.py" "/temu/bin/python")

# 循环检查并杀死进程
for process in "${processes[@]}"; do
    pro_ids=($(ps -ef | grep "$process" | grep -v grep | awk '{print $2}'))
    # 判断进程id数组是否为空，若不为空，则逐个杀掉进程
    if [ ${#pro_ids[@]} -gt 0 ]; then
        for pro_id in "${pro_ids[@]}"; do
            echo "kill the $process process_id is $pro_id"
            kill -9 $pro_id
        done
    fi
done