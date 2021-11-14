import requests
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image
from io import BytesIO
from pprint import pprint
from requests.models import Response


# ================
# 金鑰 端點 區域
# ================
key = ""
region = 'westus2'
endpoint = 'https://aien140001visionservice.cognitiveservices.azure.com/'
endpointUrl=f'{endpoint}vision/v3.0/ocr'

# ================
# 讀取圖片路徑
# ================
image_path = "./cute_image/output_address.jpg"
image_data = open(image_path, "rb").read()


# ================
# ocr 必要參數
# ================
headers = {'Ocp-Apim-Subscription-Key': key,
           'Content-Type': 'application/octet-stream'}
params = {
    # Request parameters
    'language': 'zh-Hant',
    'detectOrientation': 'true',
}

# ================
# response 用json 讀取辨識的字元資料
# ================
response = requests.post(
    endpointUrl, headers=headers, params=params, data=image_data)
response.raise_for_status()
analysis=response.json()
pprint(analysis)

# ================
# 行列式
# ================
line_infos = [region["lines"] for region in analysis["regions"]]
pprint(line_infos)


# ================
# 行列式存成list
# ================
word_infos = []
for line in line_infos:
    for word_metadata in line:
        for word_info in word_metadata["words"]:
            word_infos.append(word_info)



print(word_infos)


print(word_infos[0]["text"])
print(word_infos[1]["text"])
print(word_infos[2]["text"])
