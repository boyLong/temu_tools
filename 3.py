import threading

import redis

#r = redis.Redis(host='139.196.165.164', port=6379, db=5, password='Kx-boot-server')
r = redis.Redis(
    host="43.143.205.50",
    port=6379,
    db=2,
    password='%^AFGJHJKHj'
)

import json
from common.verify_captcha import VerifyCaptcha

import time

def get_VerifyCaptcha(token,ck):

    while 1:
        try:
            a = VerifyCaptcha(href="https://www.temu.com/",
                              VerifyAuthToken=token,cookie=ck
                              )
            print(a.start())
            return 1
        except:
            import traceback
            traceback.print_exc()
            pass

        break


def cccc():
    while 1:

        try:
            rows = r.spop('t_token_hea')
            print(rows)
            if rows is None:
                time.sleep(10)
                #row = eval(rows)
                continue
            row = eval(rows)
            a=get_VerifyCaptcha( row['Verifyauthtoken'],row['Cookie'])

            if a !=1:
                continue

            row['Cookie']=f"{row['Cookie']}; verifyAuthToken={row['Verifyauthtoken']};"
            del row['Verifyauthtoken']
            del row['anti-content']
            scv =json.dumps(row)
            r.sadd("t_token_hll",scv)
        except:
            import traceback
            traceback.print_exc()
            pass

if __name__ == '__main__':

    cccc()
    i = 1
    while True:
        t1 = threading.Thread(target=cccc)
        t2 = threading.Thread(target=cccc)
        t3 = threading.Thread(target=cccc)
        t4 = threading.Thread(target=cccc)
        t5 = threading.Thread(target=cccc)
        t6 = threading.Thread(target=cccc)
        t7 = threading.Thread(target=cccc)
        t8 = threading.Thread(target=cccc)
        t9 = threading.Thread(target=cccc)

        t1.start()
        t3.start()
        t2.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t9.start()
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        t7.join()
        t8.join()
        t9.join()

        i = i + 1
        print(i)
        if i == 10000:
            break
