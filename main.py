import requests
import json
import time

url = "https://gitpod.io/public-api/gitpod.v1.WorkspaceService/StartWorkspace"

payload = json.dumps({
  "workspaceId": "miyan0001-xmiyan-kazek3axxe0"
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
  'Cookie': "GCLB=CLywvJmSpcmx5wEQAw; gitpod_hashed_user_id=172092a222c5d6679cc05bc4f22ec36b; _gitpod_io_ws_f1b76a45-f5ba-4fa2-ba62-41aa445b97a8_owner_=nIONmqY4r5E2bEZ01UX3PbpBiWiB0jvx; _gitpod_io_ws_abc2e73d-bd53-44dc-89b6-35b2499b4afc_owner_=7SXecVKS2EpGRR2.ko4UvK70ok9dNxrB; _gitpod_io_ws_ceafc0b3-640c-4369-865b-fb854f106f3e_owner_=sbJx65Bp.DyTE_QdVybxKs13V_Czs3ub; _gitpod_io_ws_49440a94-b2a9-45fa-a0c9-e6a76363154b_owner_=PPuzgkGfGa_Hx9nBck4JM3GT2mMMan_W; _gitpod_io_ws_9d3e464c-50fc-473c-a584-e0c8b9cebb8e_owner_=cFNb3HHoPusQpPe6SaDly596m1wlCjx9; _gitpod_io_ws_06a58abb-93d7-4e72-b5ed-d1ed7b44263a_owner_=8YXzNmB55ZhVG6Jy3A.vJSsCtY.y4sJu; __Host-_gitpod_io_jwt2_=eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6IjAwMDEifQ.eyJpYXQiOjE3MjcwMzkyMTMsImV4cCI6MTcyNzY0NDAxMywiaXNzIjoiaHR0cHM6Ly9naXRwb2QuaW8iLCJzdWIiOiI5YWIzMTNjOC02MThhLTQ2NWMtYTJkZS1lYjYzYzU5NTI4NDEifQ.RAd0TJXGg3Iy8h1cgnFiBChgiPJFjssIEpnXY3D7xquP-EgOXPU2e-N7rJ7QQA6dzL6ZYCxu3zRZ8Fl8RR0gtrM_37CQca8W0e8qkIpsGlB4xcQxa-bxC6laLVwwnhnk_L8YhVqRMDvNwJxxF6H75OlfOPp_sjxpZi1YIk8UXhbT9anp4UIUbygtEnRszy5X9nRNjQKoB2dMxYfo2Mo3aOlZRHz_2-AJ96rXxKCp1HjAUKqDV_r0yyDxXDL6XF9dKTcFAoEZzbc39zdlvrbNqJYW87Nj5vbfnvtFqSxKJ1JSAuWoGRmdiPbuy-lrzFpvzBumJqLkCHgn_Q1ruGKzPBf6dnEjPIEdc2PQ4Uwv34YbigfuA-F24va7BavrKkZKNc-4jQ-F8xbmqejsxb81TLu2LGNGNrGzGcFYoMJUvdIf1AID3cvauVRzOXoGQ3Om3NcfP8Rg_jKrB9Yfwdkm9MbqblDIvyoBmVjndMM-i1HxQVxK-w0FeW7_24yPphR_OipzM-wh-rKAX75itxRox2IKt8Qy_FHW3ZO5OaZoFq4xcaVyJ2tlD95K5GF6625iwR6BEYclMmca-WSNXdXY6-R23i-9suoDdOdV3AdL5eSUHMnx_GaqD1x2RChT3_DfXXz0ySlgYFghRZkjOADW1ijxOKiZpas2kDJLTcLpR3I"
}

while True:
    response = requests.post(url, data=payload, headers=headers).text
    time.sleep(5)