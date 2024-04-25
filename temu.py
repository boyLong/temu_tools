# # -*- coding: utf-8 -*-
# import re
# import uuid
#
# from urllib.parse import quote_plus, urlparse, parse_qs, urlencode
# import secrets
# import time
# import random
# import json
# import requests
# from common.logger import logger
# from common.config import get_gif_url
# from common.verify_captcha import VerifyCaptcha
# from common.encrypt_tools import AsyncAnti, get_nano, hash_o
# from common.device_generation import DeviceGeneration
# from common.request import AsyncRequest
#
#
# def get_username():
#     return f"{get_id(random.randint(10, 20))}@gmail.com"
#
#
# def get_password():
#     return 'temu_shop_123123'
#
#
# def get_id(e=21):
#     chars = "0123456789abcdefghijklmnopqrstuvwxyz"
#     return "".join(secrets.choice(chars) for _ in range(e))
#
#
# class TemuDetail:
#     def __init__(
#             self,
#             href="https://www.temu.com/",
#             proxy='http://look1234-zone-custom-region-hk:look1234@47.236.40.83:8088',
#             # proxy=None,
#             headers=None,
#     ):
#         self.anti = None
#         self.session = AsyncRequest(proxy=proxy, headers=headers)
#         self.device = DeviceGeneration(self.session.get_headers())
#         self._session_id = get_id(10)
#         self.page_id = f"10005_{int(time.time() * 1000)}_{get_id(10)}"
#         self.__event = {}
#         self.__metrics_counter__ = 0
#         self.__location = href
#         self.__server_time = {}
#
#     async def index(self, href):
#         resp = await self.session.get(href)
#
#         self.session.update_headers({
#             "referer": href,
#         })
#         await self.get_nano()
#         self.session.anti = AsyncAnti(headers=self.session.get_headers(),
#                                       lt_c=[230, 9, 217, 13],
#                                       gt_c=[167, 184, 169, 116],
#                                       _=[
#                                             "T",
#                                             "*",
#                                             "ì",
#                                             "ª"
#                                         ])
#
#         self.location = href
#         self.device.reload(resp.text)
#         return resp.text
#
#     async def get_nano(self):
#         if self.session.get_cookie("_nano_fp"):
#             return self.session.get_cookie("_nano_fp")
#         nano = await get_nano()
#         self.session.update_cookie({"_nano_fp": nano})
#         return nano
#
#     def get_event(self, name):
#         count = self.__event.get(name, 1)
#         self.__event[name] = count + 1
#         return count
#
#     async def gif(self, event_list=None):
#         region = self.session.get_cookie("region", "211")
#         currency = self.session.get_cookie("currency", "USD")
#         language = self.session.get_cookie("language", "en")
#         bg_ud = self.session.get_cookie("_bee")
#         nano = await self.get_nano()
#         width = self.device.screen[0]
#         height = self.device.screen[1]
#         req_event = []
#
#         if self.session.get_cookie("_bee"):
#
#             cookie = (f'api_uid={self.session.get_cookie("api_uid")}; _bee={self.session.get_cookie("_bee")};'
#                       f' njrpl={self.session.get_cookie("njrpl")}; dilx={self.session.get_cookie("dilx")}; hfsc={self.session.get_cookie("hfsc")}')
#         else:
#             cookie = f'api_uid={self.session.get_cookie("api_uid")}'
#         for event in event_list:
#             event_count = self.get_event(event["op"])
#             req_time = str(int(time.time() * 1000))
#             dcf = hash_o(f"{req_time}{event['op']}{event_count}")
#             data = {
#                 "page_sn": "10005",
#                 "page_id": self.page_id,
#                 "cli_timezone": "Asia/Shanghai",
#                 "cli_region": region,
#                 "cli_currency": currency,
#                 "cli_language": language,
#                 "_x_sessn_id": self._session_id,
#                 "time": req_time,
#                 "log_id": f"{req_time}{get_id(16)}",
#                 "user_id": "",
#                 "uin": "",
#                 "app_id": "",
#                 "screen_width": height,
#                 "screen_height": width,
#                 "dpr": "1",
#                 "app_version": "",
#                 "platform": "browser",
#                 "plat_type": "pc",
#                 "cookie_fp": nano,
#                 "storage_fp": nano,
#                 "dcf": f".{event_count}.{dcf}",
#                 "bg_id": bg_ud,
#                 "os_language": self.device.languages[0],
#                 "_ck_h_sequ": str(self.__metrics_counter__),
#                 "support_beacon": "1"
#             }
#             self.__metrics_counter__ += 1
#
#             data.update(event)
#             headers = {
#                 'accept': '*/*',
#                 'content-type': 'text/plain;charset=UTF-8',
#                 'origin': 'https://www.temu.com',
#                 'referer': 'https://www.temu.com/',
#                 "cookie": cookie
#
#             }
#             req_event.append(
#                 self.session.post(get_gif_url(region),
#                               headers=headers,
#                               data=data)
#
#             )
#         await asyncio.gather(*req_event)
#     async def server_time(self):
#         UpdateServerTime = int(time.time() * 1000)
#         server_time = await self.session.get("https://www.temu.com/api/server/_stm")
#
#         self.__server_time = {
#             "ServerTime": server_time.json()["server_time"],
#             "UpdateServerTime": UpdateServerTime,
#             "UpdateFirstServerTime": UpdateServerTime - random.randint(50, 120)
#         }
#         self.session.up_server_time(self.__server_time)
#
#     async def a4(self):
#         await self.get_nano()
#         await self.server_time()
#
#         a3_list =[
#             self.session.get("https://www.temu.com/api/phantom/dm/wl/cg"),
#             self.session.get("https://www.temu.com/api/phantom/xg/pfb/a3"),
#             self.session.get("https://www.temu.com/api/phantom/xg/pfb/b")
#         ]
#         await asyncio.gather(*a3_list)
#         a4 = await self.device.a4()
#         await self.session.post("https://www.temu.com/api/phantom/xg/pfb/a4", json=a4)
#         await self.session.get("https://www.temu.com/api/phantom/xg/pfb/l1")
#
#     async def start(self):
#
#
#         text = await self.index(self.__location)
#         try:
#             pageListId = re.findall('"pageListId":"(.*?)"', text)[1]
#             self.home_page_list_id = pageListId
#         except:
#             logger.error(f'获取pageListId失败, 设备权重过低,不在继续')
#             return {"code": 500, "msg": '获取pageListId失败, 设备权重过低,不在继续'}
#
#         await self.gif(
#             event_list=[
#                 {
#                     "page_url": "https://www.temu.com/",
#                     "refer_url": "",
#                     "op": "pv",
#                     "event": "page_show",
#                 },
#                 {
#
#                     "hit": "0",
#                     "page_el_sn": "225383",
#                     "is_show": "1",
#                     "ndisp_rsn": "",
#                     "op": "impr",
#                 },
#                 {
#                     "hit": "0",
#                     "page_el_sn": "225216",
#                     "op": "impr",
#                 },{
#                     "hit": "0",
#                     "page_el_sn": "228053",
#                     "promo_atmos": "0",
#                     "op": "impr",
#                 }
#             ])
#         await self.a4()
#
#         logger.info(f'开始验证')
#         await self.session.get('https://www.temu.com/api/adx/cm/ttc?scene=1&type=0')
#         url = 'https://www.temu.com/api/alexa/homepage/goods_list'
#         list_id = get_id(21)
#         params = (
#             ('extend_fields', '{}'),
#             ('offset', '0'),
#             ('count', '120'),
#             ('list_id', list_id),
#             ('opt_id', '25'),
#             ('listId', list_id),
#             ('scene', 'home'),
#             ('page_list_id', pageListId),
#         )
#         resp = await self.session.get(url, anti={"event": True}, params=params, verify=self.verify)
#         res_data = resp.json()
#         if not res_data.get('success') or res_data.get('error_code') != 1000000:
#             print(res_data)
#             logger.error(f'获取home_goods_list失败,不在继续')
#             return {"code": 500, "msg": '获取home_goods_list失败,不在继续'}
#         logger.info(f"选择一部分商品进行gif提交")
#         idx = 1
#         env_list = []
#         for good in res_data.get('result')["home_goods_list"][:5]:
#             good_data = good["data"]
#             env_list.append({
#                     "hit": "0",
#                     "login_scene": "202",
#                     "p_rec": json.dumps(good_data["p_rec"],separators=(',', ':')),
#                     "idx": str(idx),
#                     "g_idx": str(idx),
#                     "op": "impr",
#                     "page_el_sn": "200024",
#                     "show_currency": good_data["p_rec"]["show_currency"],
#                     "show_price":  good_data["p_rec"]["show_price"],
#                     "show_sales": good_data["p_rec"]["show_sales"],
#                     "show_skc": "0",
#                     "tag_list": "just bought",
#                     "goods_id": good_data["p_rec"]["g"],
#                     "page_list_id":pageListId,
#             })
#
#         await self.gif(event_list=env_list)
#         spec_ids = ''
#         good_id = '601099518641848'
#         for good in res_data.get('result')["home_goods_list"]:
#             if good["data"].get("sold_quantity_percent"):
#                 spec_ids = good["data"].get("spec_ids", '')
#                 good_id = good["data"].get("goods_id")
#                 break
#         data = {"page_sn": 10005, "_oak_sku_count": 1, "_oak_show_sale_price_suffix": 1,
#          "_oak_show_leaf_category_low_price_tag": "1", "_oak_stage": len(spec_ids.split(",")), "single_sku_ignore_panel": 0,
#          "goods_id": good_id, "_oak_spec_ids": spec_ids, "_oak_page_source": 102,
#          "request_type": 0}
#         resp = await self.session.post("https://www.temu.com/api/oak/integration/sku",
#                                 anti={
#                                     "event":True,
#                                 },verify=self.verify,json=data)
#         if resp.status_code == 200 and resp.json()["success"]:
#             logger.info(f'skuheaders激活成功')
#
#
#             print(self.session.get_headers())
#         else:
#             print(resp.json())
#         # return self.session.get_headers()
#
#     async def verify(self, response):
#
#         if response.status_code == 200 and response.json().get("error_code") == 54001:
#             verify_auth_token = response.json()["verify_auth_token"]
#             logger.info(f'接口出现验证码,开始验证 token:{verify_auth_token}')
#
#             self.session.update_headers({
#                 "verifyauthtoken": verify_auth_token
#             })
#             self.session.update_cookie({
#                 "verifyAuthToken": verify_auth_token
#             })
#
#             self.session.update_headers({
#                 'referer': f'https://www.temu.com/uk/bgn_verification.html?VerifyAuthToken={verify_auth_token}&from='
#                            f'{quote_plus(self.__location)}&type=iframe&iframeMsgId={get_id(21)}'
#             })
#
#             vc = VerifyCaptcha(self.session.get_headers(), self.session, )
#             res = await vc.start()
#
#             url_info = urlparse(self.__location)
#             query = parse_qs(url_info.query)
#             new_query = {}
#
#             for k, v in query.items():
#                 new_query[k] = v[0] if v else ''
#             new_query["_x_sessn_id"] = self._session_id
#             new_query["refer_page_name"] = "bgn_verification"
#             new_query["refer_page_sn"] = self.page_id
#             new_query["refer_page_sn"] = "10005"
#
#             self.__location = url_info._replace(query=urlencode(new_query)).geturl()
#             self.session.update_headers({
#                 'referer': self.__location,
#             })
#             return res
#         return response
#
#
# if __name__ == '__main__':
#     headers = {
#         'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"Windows"',
#         'upgrade-insecure-requests': '1',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#         'service-worker-navigation-preload': '2',
#         'sec-fetch-site': 'cross-site',
#         'sec-fetch-mode': 'navigate',
#         'sec-fetch-user': '?1',
#         'sec-fetch-dest': 'document',
#         'referer': 'https://www.google.com/',
#         'accept-language': 'zh-CN,zh;q=0.9',
#         'priority': 'u=0, i',
#     }
#     import asyncio
#
#     t = TemuDetail(href="https://www.temu.com/", headers=headers)
#
#     import asyncio
#
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     loop.run_until_complete(t.start())
#
# #     '''
# # select a.shop_url from tmp.tmp_ods_tokopedia_sold_list_20240415_shop2 a left join tmp.tmp_ods_tokopedia_sold_list_20240415_shop b on a.shop_id=b.shop_id where b.shop_id is null group by a.shop_url
# #
# #     '''
import asyncio

from common.request import AsyncRequest

async def test():

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36', 'Accept-Encoding': 'gzip, deflate, zstd', 'accept': 'application/json, text/plain, */*', 'Connection': 'keep-alive', 'accept-language': 'zh-CN,zh;q=0.9', 'cache-control': 'no-cache', 'content-type': 'application/json;charset=UTF-8', 'referer': 'https://www.temu.com/?_x_sessn_id=pujkcuiav6&refer_page_name=bgn_verification&refer_page_sn=10005', 'pragma': 'no-cache', 'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'verifyauthtoken': '4rjRTkHF_ijpv5W2oVbtdQ49beeeca1fc1e8c69', 'Cookie': 'timezone=Asia%2FShanghai; currency=USD; language=en; region=211; webp=1; _nano_fp=Xpman09YX5gbn5Xbl9_JrE_Xhd0BCZgiO_DGAVzO; verifyAuthToken=4rjRTkHF_ijpv5W2oVbtdQ49beeeca1fc1e8c69; api_uid=Cm1olmYqNVJGIgBzwhmKAg==; __cf_bm=0yGqQgn66jdiS4uTN7efVdNB5H7sqXrZHMTovlc4rW0-1714042194-1.0.1.1-qLQKkUQlsXlOGZq2YRvXlvpUxNhQZQ88i6p2WrT__Xmcs0IEv7EHpfVAzz5papmlNowr3d7WPZWUHhjKqR3LdQ; _bee=xTLr50vpbpdsm6j0CsVPJCYXGLElvapu; njrpl=xTLr50vpbpdsm6j0CsVPJCYXGLElvapu; dilx=sGOa~~oNCEGn9_Wzcf4vR; hfsc=L3yLfIk06zz50pfPfQ==; _ttc=3.nTbZ4HgI6LuO.1745578228'}
    proxy='http://look1234-zone-custom-region-hk:look1234@47.236.40.83:8088'

    ar = AsyncRequest(headers=headers,proxy=proxy)
    rep = await ar.get("https://www.temu.com/dog-travel-water-bottle-portable-dog-water-bottle-pet-drinking-bottle-drink-cup-dish-bowl-g-601099516773562.html?_oak_mp_inf=ELqJsJmm1ogBGiBhYTQxYzU1ZGZkYjE0YzVjOWFkNzg2ZTc2MGZkZDA3ZSC3i4%2Bn8TE%3D&top_gallery_url=https%3A%2F%2Fimg.kwcdn.com%2Fproduct%2FFancyalgo%2FVirtualModelMatting%2Fb29dab36858f076347f539d3cf06a7ca.jpg&spec_gallery_id=23615339&refer_page_sn=10032&refer_source=0&freesia_scene=1&_oak_freesia_scene=1&_oak_rec_ext_1=NTk4&refer_page_el_sn=200024&refer_page_name=goods&refer_page_id=10032_1714042439494_y9ps3fqt2w&_x_sessn_id=ks912b07b1")
    print(rep.text)

if __name__ == '__main__':

    asyncio.run(test())