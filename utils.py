import glob
import os
from zipfile import ZipFile
import requests


def make_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def get_url(target_zip_id):
    base_url = "https://digitalcorpora.s3.amazonaws.com/corpora/files/CC-MAIN-2021-31-PDF-UNTRUNCATED/zipfiles"
    # 目標のZIP IDから範囲を生成する
    target_num = int(target_zip_id)
    start_range = (target_num // 1000) * 1000
    end_range = start_range + 999

    # 範囲を文字列で表現
    output_range = f"{start_range}-{end_range}"

    url = f"{base_url}/{output_range}/{target_zip_id}.zip"

    return url


def download_and_extract_zip(target_url, target_dir):
    # ZIPファイルをダウンロードするための一時ファイル名を生成
    temp_zip_path = os.path.join(target_dir, "temp.zip")

    # URLからZIPファイルをダウンロード
    response = requests.get(target_url)
    response.raise_for_status()  # エラーが発生した場合は例外を発生させる

    # ダウンロードした内容を一時ファイルに保存
    with open(temp_zip_path, 'wb') as temp_zip:
        temp_zip.write(response.content)

    # ZIPファイルを解凍
    with ZipFile(temp_zip_path, 'r') as zip_ref:
        zip_ref.extractall(target_dir)

    # 一時ファイルを削除
    os.remove(temp_zip_path)


def remove_irrelevant_pdf(target_zip_id, file_name_list):
    for pdf_path in glob.glob(f"data/{target_zip_id}/*.pdf"):
        filename = pdf_path.split("/")[-1]
        if filename not in file_name_list:
            os.remove(pdf_path)


def download_pdf(target_zip_id, file_name_list):
    target_dir = f"data/{target_zip_id}"

    make_dir(target_dir)
    if len(glob.glob(f"{target_dir}/*.pdf")) > 0:
        print("already finished")
        return
    target_url = get_url(target_zip_id)
    download_and_extract_zip(target_url, target_dir)
    remove_irrelevant_pdf(target_zip_id, file_name_list)
