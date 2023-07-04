# 管理方法
- gitのremote repository上で共通のソースコードを管理する。
- local repositoryで改造し、remoteへコミットすることで、各作業者が使える状態にする。
- マスターデータやモデルファイルを入れ直せば、その問題で最適化計算が可能。

# 必要なもの
- git for windows 
- git GUI: source treeを推奨（guiが不要な人はgit-bashでOK）
- python3系

# repository
- local repository: 各自のlocal環境で構築
- remote repository: https://jp.ykgw.net/project02/C24/INV-WR_OpEx/NAWI/repository/task1.git

# directory structure
task1 - readme.txt
      - src_opt - LVMWD - input folder - input files
                        - opt_module folder - optimization modules
                        - opt_problem folder - definition of optimization problem and prediction model
                        - output folder - output files
                        - pkg folder - other packages
                        - alg_param.ini: algorithm parameter
                        - generate_param.py: make parameter.csv from masterdata.csv
                        - optimize_schedule.py: calculate scheduling optimization
                        - readme.txt: explanation of processing and file
                        - requirements.txt: required python library/package and version
                - OCWD  - [same as LVMWD]

# 最適化モジュールの使い方
1. generate_param.pyを実行し、parameter.csvを生成する
2. optimize_schedule.pyを実行し、最適化結果を得る

# gitのインストール方法
下記などを参照
https://www.curict.com/item/60/60bfe0e.html

1. インストーラーをダウンロードする
2. インストーラーで実行する
3. 