import requests
import json
import time

url = "https://gitpod.io/public-api/gitpod.v1.WorkspaceService/StartWorkspace"

payload = json.dumps({
  "workspaceId": "miyan0001-xmiyan-dms2gcxv5yd"
})

headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'Content-Type': "application/json",
  'sec-ch-ua-platform': "\"Android\"",
  'sec-ch-ua': "\"Chromium\";v=\"130\", \"Android WebView\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
  'sec-ch-ua-mobile': "?1",
  'connect-protocol-version': "1",
  'origin': "https://gitpod.io",
  'x-requested-with': "mark.via.gp",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "cors",
  'sec-fetch-dest': "empty",
  'referer': "https://gitpod.io/start/",
  'accept-language': "en,en-US;q=0.9",
  'priority': "u=1, i",
  'Cookie': "GCLB=CLywvJmSpcmx5wEQAw; gitpod_hashed_user_id=172092a222c5d6679cc05bc4f22ec36b; _gitpod_io_ws_f1b76a45-f5ba-4fa2-ba62-41aa445b97a8_owner_=nIONmqY4r5E2bEZ01UX3PbpBiWiB0jvx; _gitpod_io_ws_abc2e73d-bd53-44dc-89b6-35b2499b4afc_owner_=7SXecVKS2EpGRR2.ko4UvK70ok9dNxrB; _gitpod_io_ws_ceafc0b3-640c-4369-865b-fb854f106f3e_owner_=sbJx65Bp.DyTE_QdVybxKs13V_Czs3ub; _gitpod_io_ws_49440a94-b2a9-45fa-a0c9-e6a76363154b_owner_=PPuzgkGfGa_Hx9nBck4JM3GT2mMMan_W; __Host-_gitpod_io_jwt2_=eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6IjAwMDEifQ.eyJpYXQiOjE3MjY5OTU5NTEsImV4cCI6MTcyNzYwMDc1MSwiaXNzIjoiaHR0cHM6Ly9naXRwb2QuaW8iLCJzdWIiOiI5YWIzMTNjOC02MThhLTQ2NWMtYTJkZS1lYjYzYzU5NTI4NDEifQ.Ym4A_5rlSHTle88rJ401Y5rf8COwy-7tBz4TqO0_y4fAG540wFY1tbwubA0mPI1LCnr1VLLiMSFYeFsPcstpLPQiFvWZY7FLdMg1Z6VNpCls-tTA5IUb03hgpljPSs7fUbOhXMJNVMbqIuSTu3PcCRGn0ZeeuWLlfMl9LXOCAMvIWPZdroxJ085FMEirP9rbEe43JMAIiutSCXsAsRBIzJ4u5Rqd2xY1lDYeIADQVZVWxwLCWcgc_TraFFIwvpV5e70I9jTb8sXxfQJB_9aT-lA69BsqBZHRYUUrRVMs6qd31uyZwJ2hDDMBYaAp7xDOAhWWAz5_JAw2-Ee3Vtl7NpeDLDYes1LWZP55-uK_3Xam9Zmk9NtWAHXYSlt0YwMkJ2aNG5zytHWHw0vW4X6weI7EzT51Xck4-naePzcW2XEOmK2wYlHKcm9AZChEOpLkMEOi03c7QCnZ-w58LTrFM0KpydQ7F-HcWVjGxcTLIAsUGsoOo9jXZE-7-37TgWfsxJd2leUdIJsn6-Nk3UNxQ54ekp-A0KpupGDWWc0GpA7Yz14Lrhn42FILxzhG_AdauBBqTXTjsNAAxjBOO0YP6-pMtiNA6m2M-lQxCA06YarXPwhtyVvr1gnXtTpzkb5o5S2nLLUz_NCTwkgnScr5JI5k-zaLgRBdoXzuoaQSmtk; _gitpod_io_ws_9d3e464c-50fc-473c-a584-e0c8b9cebb8e_owner_=cFNb3HHoPusQpPe6SaDly596m1wlCjx9"
}
while True:
    response = requests.post(url, data=payload, headers=headers).text
    time.sleep(5)