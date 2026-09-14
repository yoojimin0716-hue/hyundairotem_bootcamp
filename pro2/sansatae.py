## import pandas as pd

## df = pd.read_csv(r'C:\Users\acorn\Downloads\landslide_train.zip')
# 1. 컬럼(열) 개수
## print(df.shape)        # (행 개수, 열 개수)
## print(df.shape[1])     # 열 개수만

# 2. 양성 비율
## print(df['label컬럼명'].value_counts())
## print(df['label컬럼명'].value_counts(normalize=True))

import zipfile

zip_path = r'C:\Users\acorn\Downloads\landslide_train.zip'
extract_path = r'C:\works\projects\pro2\data' 

with zipfile.ZipFile(zip_path) as z:
    z.extractall(extract_path)

    import json

with open(rf'{extract_path}\train\ls_scene_11_w01\labels\20200512.json', encoding='utf-8') as f:
    sample = json.load(f)

print(sample)

import glob
import json
import pandas as pd

label_files = glob.glob(r'C:\works\projects\pro2\data\train\*\labels\*.json')
print("전체 라벨 파일 개수:", len(label_files))

rows = []
for lf in label_files:
    with open(lf, encoding='utf-8') as f:
        sites = json.load(f)  # 리스트 형태
    for site in sites:
        rows.append({
            'site_id': site['site_id'],
            'visible': site['visible']
        })

df = pd.DataFrame(rows)
print(df.shape)  # (전체 site 개수, 컬럼 수)
print(df['visible'].value_counts())
print(df['visible'].value_counts(normalize=True))