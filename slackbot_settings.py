# coding: utf-8
import os


# botアカウントのトークンを指定
API_TOKEN = os.environ["API_KEY"]

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "藤原竜也です"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']
