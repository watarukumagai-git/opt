<p>
<script type="text/x-mathjax-config">// <![CDATA[
MathJax.Hub.Config({
  tex2jax: {
    inlineMath: [['$','$'], ['\\(','\\)']],
    displayMath: [ ['$$','$$'], ["\\[","\\]"] ]
  }
});
// ]]></script>
<script type="text/javascript" async="" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML">// <![CDATA[

// ]]></script>
</p>

# 技術動向サーベイ
- 作成者：熊谷 渉（Operational Excellence Gr., Project Design Div.）
- 担当日：2022年8月2日


## 対象論文
- タイトル：Engineering Cel7A carbohydrate binding module and linker for reduced lignin inhibition【[URL][url1]】
- 発行日：2016年6月1日
- 雑誌名：Biotechnology and Bioengineering, Vol.113, No.6, pp.1369–1374
- 著者：K. L. Strobel$^{1}$, K. A. Pfeiffer$^{1}$, H. W. Blanch$^{1}$, D. S. Clark$^{1}$
- 所属
	- 1: University of California (USA)
- 引用数：40（2022年7月25日時点）
- キーワード：バイオマス変換、セルラーゼ、リグニン、タンパク質設計
	- Strobelの学位論文: "Understanding and Engineering Cellulase Binding to Biomass Components", 2015【[URL][url2]】



## Abstruct
セルラーゼのリグニンへの非生産的な結合は、バイオマスの酵素による加水分解を阻害し、酵素の必要量とバイオ燃料のコストを増加させる。
本研究では、Trichoderma Cel7A 炭水化物結合モジュール（CBM）とリンカーの部位特異的変異導入により、リグニンへの吸着機構を調べ、セルロースへの結合特異性を高めたセルラーゼを工学的に作製することを試みた。
CBMに疎水性残基や正電荷残基を付加する変異はセルロースに対する特異性を低下させ、負電荷残基を付加する変異は特異性を増加させた。
予測されるグリコシル化のパターンを変更するリンカー変異は、リグニンへの親和性に選択的な影響を及ぼした。
有益な変異を組み合わせて、セルロース親和性を完全に保持しながらリグニン親和性を2.5倍減少させた変異体が生成された。
この変異体は、アビセルの加水分解において添加したリグニンによる阻害を受けず、希釈酸処理したススキからWild-Type酵素より40%多くグルコースを生成した。


## 背景
- セルラーゼの利用可能濃度を高めることは、リグノセルロース系バイオ燃料のコストを低減することに繋がる。
- その手段として、リグニン吸着を低減するようにセルラーゼを改変することが挙げられる。
    - セルラーゼの効率は、バイオマスの主要な非炭水化物成分であるリグニンへの非生産的な吸着によって著しく阻害される。
    - セルロース（Avicel）にリグニンを添加すると、加水分解収率が80%も低下し、リグニン吸着による有害な影響が強調される[[ref1]](#ref)。
    - 真菌セルラーゼの多くは、触媒ドメイン（CD）とセルロース結合モジュール（CBM）が、柔軟で高度にグリコシル化されたリンカーで接続されている[[ref2]](#ref)。
    - CBMは、セルロースへの結合、その基質上での酵素の濃度の増加[[ref3]](#ref)、およびリグニンへの非生産的吸着の大部分を担う[[ref4,ref5,ref6]](#ref)。


## 先行研究
- セルラーゼのリグニンへの吸着に関する研究は数多くあるが、リグニンとの親和性を低下させるために酵素を設計する試みはほとんど行われていない。
    - 疎水性相互作用と静電相互作用は、リグニン吸着に影響を与えることが知られている。
        - 疎水性相互作用は、リグニン吸着の主要なメカニズムであると仮定されている[[ref6,ref7]](#ref)。
        - 静電相互作用も、リグニン親和性・阻害に影響を与えることが示されている[[ref8,ref9]](#ref)。
    - リグニン阻害を低減する先行研究は、追加材料が必要で、バイオ燃料の製造コストが増加する。
        - バイオマスまたはセルラーゼを追加材料（タンパク質、ポリマー、界面活性剤）で処理する方法[[ref9,ref10,ref11,ref12]](#ref)は、バイオ燃料の製造コストが増加し、下流の処理に影響を与える可能性がある。
        - 例えば、BSAによる前処理は、リグニン吸着をブロックできる[[ref12]](#ref)。
- そこで、リグニン結合性が低いセルラーゼ変異体（リグニン耐性セルラーゼ）を設計すれば、余分なコストや添加物の煩雑さなしで、リグニン阻害を低減できる。


## 本論文の成果
- 本研究では、リグニン耐性セルラーゼの設計に向けて、部分的な残基改変によって、Cel7Aのリグニン結合性の影響を調査した。
- CBMの電荷改変、あるいはリンカーの電荷・グリコシル化改変することで、セルロース選択性が増加し、リグニン存在下での加水分解能力も向上するケースを確認した。
- 最良な変異体は、リグニンを添加しても阻害されず、前処理したススキの加水分解においてWild-Typeよりも優れた結果を示した。
- 主要なセルラーゼは、類似のリンカーとCBMを含むため、Cel7A CBMとリンカーを上手く改変すれば、リグニン吸着耐性セルラーゼカクテルに発展できる。


構成
- 2章：CBMの変異とセルロース選択性
- 3章：リンカーの変異とセルロース選択性
- 4章：最良変異体のセルロース選択性と加水分解能力

## 2章：CBMの変異とセルロース選択性
- 本章では、CBMの変異とセルロース/リグニン吸着量の関係を確認する。
- 本研究では、リグニン存在下でのセルロース加水分解活性の向上には、CBMのリグニンよりもセルロース結合選択性の向上が必要だと仮定している。
- Te-Tr-Cel7A（Te-Tr-chimera）を使用した。
    - Tr-linkerとCBM（1cbh）を合体させたTe-Cel7A CDを酵母で発現させたもの。
    - Te-Tr-chimeraの生成のために、Cel7Aの遺伝子を含むSc（酵母）をSC-Trp（培地）に移植し、培養させた。

菌株（由来微生物）
- _Trichoderma reesei_（_Tr_; トリコデルマ・リーセイ）: 軟腐朽菌の一つ。糸状菌。
- _Talaromyces emersonii_（_Te_; タラロミケス・エメルソニイイ）: 軟腐朽菌の一つ。糸状菌。
- _Phanerochaete chrysosporium_（_Pc_; ファネロケーテ・クリソスポリウム）: 白色腐朽菌の一つ。（我々の実験で使用）
	- 軟腐朽菌: 水分を多く含む木材表面を軟化させ，セルロースとリグニンを分解する（ただし、セルロース分解性が強い）
	- 白色腐朽菌: セルロースとリグニンを分解する（ただし、残留するセルロースを白色に変色させる）
	- 褐色腐朽菌: セルロースのみを分解し、リグニンは分解されずに残留する（ただし、白色よりもセルロース分解性は弱い）

酵母発現系（宿主）
- _Saccharomyces cerevisiae_（_Sc_; サッカロミケス・セレビシエ）: 出芽酵母。エタノール耐性。
- _Pichia pastoris_（ピキア・パストリス）: メタノール資化酵母の一つ。最少培地で高密度培養が可能。（我々の実験で使用予定）

CBM変異体
- 7つの残基について、5グループのCBM変異体（合計24個）を実験した。
    - 4つの残基（Q2、H4、V18、P30）は、ALAスキャンのときのセルロース／リグニン結合選択性の改善のため。これは著者らが以前確認した傾向である[[ref13]](#ref)。
    - 3つの残基（Y5、V27、L28）は、疎水性の影響のため。
    - グループA：ALAスキャン（7個）。Q2A, Y5A, H4A, V18A, V27A, L28A, P30A
    - グループB：正電荷への変異（4個）。Q2K, V18R, L28K, P30K
    - グループC：負電荷への変異（6個）。Q2E, H4E, V18D, V27E, L28D, P30D
    - グループD：疎水化の変異（3個）。Q2L, H4V, Y5W
    - グループE：極性変化の変異（4個）。H4Q, V18N, L28S, P30W

<img src="https://github.com/watarukumagai-git/opt/blob/main/survey/survey_20220802_kumagai/images/fig1b.jpg?raw=true" width="60%">

Fig. 1b: CBM（1cbh）内の変異対象の残基

<img src="https://github.com/watarukumagai-git/opt/blob/main/survey/survey_20220802_kumagai/images/fig1a.jpg?raw=true" width="100%">

Fig. 1a: 各CBM変異体のセルロースあるいはリグニンの分配係数


Fig. 1a
- 各CBM変異体の分配係数。
    - 各変異体のセルロース（アビセル）およびリグニンに対する吸着量を、分配係数で計算して表現した。
    - 分配係数：固相の濃度/液相の濃度[L/g]。本論文では、基質への結合/液中の残留のため、値が高ければ結合量が多いとみなせる。
    - 室温で測定したため、加水分解条件下（通常50〜60℃）では異なる場合がある。
- V27Eは、Te-Tr WTよりも、セルロース吸着量が多い。
- H4V, V18R, P30Kは、Te-Tr WTよりも、リグニン吸着量が多い。
- その他の変異は、吸着量が同等あるいは減少した。

<img src="https://github.com/watarukumagai-git/opt/blob/main/survey/survey_20220802_kumagai/images/fig1c.jpg?raw=true" width="60%">

Fig. 1c: 各CBM変異体の分配係数の散布図


Fig. 1c
- 各CBM変異体の分配係数の散布図。
    - 特異的吸着性（結合選択性）：吸着量の比。散布図中の傾き。
    - 黒線：Te-Tr WTと原点を通る直線。この直線より右下に位置すると、WTよりもリグニン選択性が高く、左上に位置するとWTよりもセルロース選択性が高い。
- 疎水性または正電荷への変異は、リグニン選択性が向上した。
    - 疎水性および静電相互作用の両方がリグニン結合に寄与していることを強く立証している。
- 負電荷への変異の多くは、セルロース選択性が向上した。
    - P30DとV27Eは、試験した変異体の中で最も大きなセルロース選択性を有していた。
- このため、CBMをD（アスパラギン酸ASP）やE（グルタミン酸GLU）の変異でスキャンすることは、より高いセルロース選択性を持つ変異体を見つけるための有益な戦略であろう。




## 3章：リンカーの変異とセルロース選択性
- 本章では、リンカーの変異とセルロース/リグニン吸着量の関係を確認する。
- リンカーはセルロース結合性に影響を与えることが知られている。
    - リンカーはセルロースに吸着することでセルロース結合性を高めることが示されている [[ref14]](#ref)。
    - CBMのグリコシル化のパターンは、セルロース結合性を変えることが示されている[[ref15]](#ref)。
- 3つの変異リンカーを設計し、Scで発現させたときのグリコシル化のパターンを変化させた。


グリコシル化（糖鎖付加）
- 糖類（結合型糖鎖）がタンパク質に付加する反応
- N-結合型グリコシル化：N-結合型糖鎖が、N（アスパラギンASN）側鎖のアミド基のN原子へ付加する。
- O-結合型グリコシル化：O-結合型糖鎖が、S（セリンSer）とT（トレオニンThr）側鎖のヒドロキシ基のO原子へ付加する。


<img src="https://github.com/watarukumagai-git/opt/blob/main/survey/survey_20220802_kumagai/images/fig2a.jpg?raw=true" width="60%">

Fig. 2a: リンカーのWild-Typeと変異体


Fig. 2a
- WTとリンカー変異体（3個）。印はSc発現のもとでグリコシル化が予想される部位。
    - WT: 23列長
    - Link1: {G2S,N2S,R2T}（3点変異、23列長、グリコシル化部位追加、正電荷残基除去）
    - Link2: {T14A,T15A,T16-}（2点変異、22列長、グリコシル化部位削除）
    - Link3: {T14G,T15P,T16-,S17A,S18A}（4点変異、22列長、グリコシル化部位削除）
- グリコシル化部位の予測は、機械学習のプログラム[[ref16]](#ref)を用いた。
    - Random Forestとペアワイズパターンを組み合わせている
    - この予測結果は正しいと仮定して議論を進める

<img src="https://github.com/watarukumagai-git/opt/blob/main/survey/survey_20220802_kumagai/images/fig2b.jpg?raw=true" width="70%">

Fig. 2b: 各リンカー変異体の分配係数の散布図

Fig. 2b
- 各リンカー変異体の分配係数の散布図。
- リンカーのグリコシル化（および電荷改変）は、リグニン結合性に影響を与えたが、セルロース結合性に影響を与えなかった。
    - グリコシル化部位の除去は、リグニン吸着量が増加したが、グリコシル化部位の追加（＋正電荷残基の除去）は、リグニン吸着量が減少した
    - 3つのリンカー変異体は、セルロース吸着量がWild-Typeと同等
    - 最良なリンカー変異体（Link1）は、グリコシル化部位の追加と正電荷除去することを意図して設計した

- セルロース／リグニン結合性の要因としてリンカー糖鎖付加を検討した研究は、我々の知る限り本研究が初めてである。
    - O-結合型糖鎖の数を変えると、リンカーの疎水性が変化し、リグニン吸着に影響を与える可能性がある（？）
    - 糖鎖がマンノースリン酸を含む場合は、リンカーの電荷が変化し、リグニン吸着に影響を与える可能性がある（？）
- しかし、グリコシル化のパターンとリグニン／セルロース結合性の関係を調べるためには、さらなる実験を通じてメカニズムを明らかにする必要がある。（課題）
    - リンカーのグリコシル化パターンを網羅するように、リンカー変異体の数を増やし、変異体の小さなセットを真菌の宿主で発現させれば、セルラーゼ／リグニン結合性に関する理解が深まり、リグニン耐性変異体の開発につながるかもしれない




## 4章：最良変異体のセルロース選択性と加水分解能力
セルロース選択性が最も高かった、2つのCBM変異体（V27E、P30D）とリンカー変異体（Link1）を組み合わせて6個の変異体を作成し、セルロース／リグニン選択性と加水分解能力について検証した。
- Te-Tr Wild-Type（chimera）
- Te-CD
- 1点変異CBM：V27E,P30D（2個）
- リンカー変異：Link1（1個）
- 1点変異CBM+リンカー変異：{P30D,Link1}（1個）
- 2点変異CBM：{V27E, P30D}（1個）
- 2点変異CBM+リンカー変異（トリプル変異体）：{V27E,P30D,Link1}（1個）

<img src="https://github.com/watarukumagai-git/opt/blob/main/survey/survey_20220802_kumagai/images/fig3a.jpg?raw=true" width="70%">

Fig. 3a: 各新変異体の分配係数の散布図

Fig. 3a
- 最良な各変異体のセルロースとリグニンへの分配係数の散布図。
- P30D,Link1：セルロース結合量は維持したまま、リグニン結合量が低下。
- V27E：リグニン結合量を維持したまま、セルロース結合量が増加。
- {P30D,Link1}：各変異の相加的効果ではないが、セルロース結合量は維持したまま、リグニン結合量がさらに低下。
- {V27E, P30D},{V27E,P30D,Link1}：セルロース結合量が増加し、リグニン結合量が減少。
- {V27E,P30D,Link1}：リグニン結合量がTe-Tr WTよりも2.5倍減少し、セルロース結合性がわずかに増加した。最もセルロース選択性が高かった。

<img src="https://github.com/watarukumagai-git/opt/blob/main/survey/survey_20220802_kumagai/images/fig3b.jpg?raw=true" width="60%">

Fig. 3b: 各新変異体のグルコース生成量（アビセル、アビセル＋リグニン）

<img src="https://github.com/watarukumagai-git/opt/blob/main/survey/survey_20220802_kumagai/images/add_fig1.jpg?raw=true" width="55%">

add_Fig. 1: 各新変異体のグルコース生成量比（（アビセル＋リグニン）／アビセル）【[URL][url2]】

Fig. 3b
- セルロース選択性が高い変異体が、リグニンによる阻害を受けるかどうかを調べるために、6つの変異体について、リグニン存在下でアビセルを加水分解する能力を検証した。
	- アビセル単体、アビセル＋リグニンにおけるグルコース生成量
- CBM＋リンカーがリグニンの影響を主要に受け、グルコース生成量が減った。
	- Te-CDは添加リグニンによって全く阻害されなかったが、Te-Tr WTはリグニン存在下で20%少ないグルコースを生成した
- 多くの各変異体は、Te-Tr WTとグルコース生成量がほぼ同じだった。
- 一方、トリプル変異体は、リグニンによって有意に阻害されず、リグニンに関係なく同量のグルコースを生成していた。

<img src="https://github.com/watarukumagai-git/opt/blob/main/survey/survey_20220802_kumagai/images/fig3c.jpg?raw=true" width="60%">

Fig. 3c: 各新変異体のグルコース生成量（ススキ）


Fig. 3c
- セルロース選択性が高い変異体について、商業的に重要な原料である希釈酸処理したススキを加水分解する能力も検証した。
- CBM変異体{V27E,P30D}は、Te-Tr WTよりも25%多くのグルコースを生成した。
- トリプル変異体は、Te-Tr WTよりも40%多くグルコースを生成した。


<img src="https://github.com/watarukumagai-git/opt/blob/main/survey/survey_20220802_kumagai/images/figS1.jpg?raw=true" width="55%">

Fig. S1: 各新変異体のグルコース生成量（ススキ＋BSA前処理）

<img src="https://github.com/watarukumagai-git/opt/blob/main/survey/survey_20220802_kumagai/images/add_fig2.jpg?raw=true" width="60%">

add_Fig. 2: 各新変異体のグルコース生成量比（ススキ／（ススキ＋BSA前処理））【自作】

Fig. S1
- 加水分解能力の向上が、リグニン結合の減少にどの程度起因しているかを調べる。
- リグニン吸着をブロックするために、BSAで前処理したススキに対する各酵素の加水分解能力も調べた[[ref12]](#ref)。
- BSA前処理を通じて、トリプル変異体がリグニン耐性を有することがさらに証明された。
	- BSA前処理がある場合、Te-Tr WTとトリプル変異体は、ほぼ同量のグルコースを生成した
	- 一方、BSA前処理がある場合、無い場合に比べて、Te-Tr WTのグルコース生成量が40%増加したが、トリプル変異体は大きな影響がなかった


まとめ
- アビセルに対する特異的な選択性は、CBMを負電荷強化、リンカーを負電荷強化＋グリコシル化部位追加によって、改善した。
    - CBM変異体{V27E},{P30D}は、天然のTr酵素に移植した場合、リグニン耐性が同等以上に向上することが期待される
    - 本研究で用いたTe-Tr WTは、天然のTr-Cel7A酵素よりもリグニンによる阻害が少ない[[ref14]](#ref)
- 一方、アビセルの加水分解効率が受けるリグニンの影響は、トリプル変異体でしか緩和できず、それ以外の変異体ではWTとほぼ同様であった。
- ススキの加水分解では、CBMを負電荷強化、リンカーを負電荷強化＋グリコシル化部位追加によって、グルコース生成量が増加した。
    - CBM変異体{V27E,P30D}は、Te-Tr WTよりも25%多くのグルコースを生成した
    - トリプル変異体は、Te-Tr WTよりも40%多くグルコースを生成した
- 一方、リンカー変異体は、Trで発現させても同等の改善にはならない可能性がある。
    - ScのO-結合型グリコシル化に差異があるため
    - しかし、Trで上記でデザインされたリンカー変異の限られたセットを発現し、スクリーニングすることによって、改良された変異体が得られると考えられる。



## 疑問点・課題
- CBMの1点変異体で調べているため、残基の影響が割とわかりやすい。
- 本論文では最大2点変異に留まっているため、もし変異数を増やしながら負電荷を強化させて、より改善する結果が得られるなら、研究成果とできる気がする。
- 一方、リンカー変異が選択性に貢献している様子もあったため、そこが設計方針になるのかは考えどころ。
- また、下記論文は本研究を参考に変異体を実験しているため、アドバンスな成果が期待できるかも。
	- X. Lu, X. Feng, X. Li, J. Zhao: "Binding and hydrolysis properties of engineered cellobiohydrolases and endoglucanases", 2018【[URL][url3]】
	- 本研究では、吸着効率と加水分解効率の改善のために、改変型CBHおよびエンドグルカナーゼ（EG）を構築した。
		- 杉本さんの論文も引用している。「Tr-CBHのCBMはセルロースとの親和性が高いため、CBMを特定のタンパク質やセルラーゼに融合させてセルロースとの結合性を高める研究が数多く行われた」
	- 2種類のセルラーゼCBH-TrCBM{V27E,P30D,Link1}およびEG-TrCBM{V27E,P30D,Link1}は、加水分解において良好な性能を発揮することがわかった。
		- EG-TrCBM{V27E,P30D,Link1}は、Wild-Type酵素よりも、リグニンへの吸着能が相対的に低く、セルロース（特にアビセル）との親和性が高い。
		- CBH-TrCBM{V27E,P30D,Link1}は、加水分解の様子が変化し、加水分解プロセスに有利になった（ただし、吸着特性は予想外であった）。
	- 以上から、CBM上の多糖の様々な結合構造が、CBMの機能（基質表面での結合性/処理性/分解性など）の違いを生み出している可能性が示唆された。
	- Tr-CBM{V27E,P30D,Link1}とセルラーゼ（CBH/EG）の融合は、吸着効率と加水分解効率を向上させた。


### <a name="ref">refernce</a>
- [ref1]: Rahikainen JL, Mikander S, Marjamaa K, Tamminen T, Lappas A, Viikari L, Kruus K. : "Inhibition of enzymatic hydrolysis by residual lignins from softwood study of enzyme binding and inactivation on lignin-rich surface," Biotechnol and Bioeng, 108:2823–2834. (2011)【[URL][url_refer1]】
- [ref2]: Payne CM, Knott BC, Mayes HB, Hansson H, Himmel ME, Sandgren M, Ståhlberg J, Beckham GT.: "Fungal cellulases," Chem Rev, 115:1308–1448. (2015)【[URL][url_refer2]】
- [ref3]: Boraston AB, Bolam DN, Gilbert HJ, Davies GJ.: "Carbohydrate-binding modules: Fine-tuning polysaccharide recognition," Biochem J, 382:769–781. (2004)【[URL][url_refer3]】
- [ref4]: Palonen H, Tjerneld F, Zacchi G, Tenkanen M.: "Adsorption of trichoderma reesei CBH I and EG II and their catalytic domains on steam pretreated softwood
 and isolated lignin," Journal Biotechnol, 107:65–72. (2004)【[URL][url_refer4]】
- [ref5]: Pfeiffer KA, Sorek H, Roche C, Strobel K, Blanch HW, Clark DS.: "Evaluating endoglucanase cel7b-lignin interaction mechanisms and kinetics using quartz crystal microgravimetry," Biotechnol Bioeng, DOI: 10.1002/bit.25657. (2015)【[URL][url_refer5]】
- [ref6]: Rahikainen JL, Evans JD, Mikander S, Kalliola A, Puranen T, Tamminen T, Marjamaa K, Kruus K.: "Cellulase-lignin interactions-the role of carbohydrate binding module and ph in non-productive binding," Enzyme Microb Technol, 53:315–321. (2013a)【[URL][url_refer6]】
- [ref7]: Sammond DW, Yarbrough JM, Mansfield E, Bomble YJ, Hobdey SE, Decker SR, Taylor LE, Resch MG, Bozell JJ, Himmel ME, Vinzant TB, Crowley MF.: "Predicting enzyme adsorption to lignin films by calculating enzyme surface hydrophobicity," Journal Biology Chemistory, 289:20960–20969. (2014)【[URL][url_refer7]】
- [ref8]: Nakagame S, Chandra RP, Kadla JF, Saddler JN.: "Enhancing the enzymatic hydrolysis of lignocellulosic biomass by increasing the carboxylic acid content of
 the associated lignin," Biotechnol Bioeng, 108:538–548. (2011) 【[URL][url_refer8]】
- [ref9]: Nordwald EM, Brunecky R, Himmel ME, Beckham GT, Kaar JL.: "Charge engineering of cellulases improves ionic liquid tolerance and reduces lignin inhibition," Biotechnol and Bioeng, 111:1541. (2014)【[URL][url_refer9]】
- [ref10]: Borjesson J, Engqvist M, Sipos B, Tjerneld F.: "Effect of poly (ethylene glycol) on enzymatic hydrolysis and adsorption of cellulase enzymes to pretreated lignocellulose," Enzyme Microb Technol, 41:186–195. (2007)【[URL][url_refer10]】
- [ref11]: Lou H, Zhu JY, Lan TQ, Lai H, Qiu X.: "PH-Induced lignin surface modification to reduce nonspecific cellulase binding and enhance enzymatic saccharification of lignocelluloses," ChemSusChem, 6:919–927. (2013)【[URL][url_refer11]】
- [ref12]: Yang B, Wyman CE.: "BSA treatment to enhance enzymatic hydrolysis of cellulose in lignin containing substrates," Biotechnol Bioeng, 94:611–617. (2006)【[URL][url_refer12]】
- [ref13]: Strobel KL, Pfeiffer KA, Blanch HW, Clark DS.: "Structural insights into the affinity of cel7a carbohydrate-binding module for lignin," J Biol Chem M, 115:673467.(2015)【[URL][url_refer13]】
- [ref14]: Payne CM, Resch MG, Chen L, Crowley MF, Himmel ME, Taylor LE, Sandgren M,
Ståhlberg J, Stals I, Tan Z, Beckham GT.: "Glycosylated linkers in multimodular lignocellulose-degrading enzymes dynamically bind to cellulose," Proc Natl Acad Sci USA, 110:14646–14651.(2013)【[URL][url_refer14]】
- [ref15]: Chen L, Drake MR, Resch MG, Greene ER, Himmel ME, Chaffey PK, Beckham GT, Tan Z.: "Specificity of o-glycosylation in enhancing the stability and cellulose binding affinity of family 1 carbohydrate-binding modules," Proc Natl Acad Sci USA, 111:7612–7617. (2014)【[URL][url_refer15]】
- [ref16]: Hamby SE, Hirst JD.: "Prediction of glycosylation sites using random forests." BMC Bioinformatics, Vol.9, Np.500 (2008).【[URL][url_refer16]】

[url1]: <https://onlinelibrary.wiley.com/doi/10.1002/bit.25889>
[url2]: <https://escholarship.org/uc/item/0tw1f2tz>
[url3]: <https://doi.org/10.1016/j.biortech.2018.06.047>
[url_refer1]: <https://pubmed.ncbi.nlm.nih.gov/21702025/>
[url_refer2]: <https://pubmed.ncbi.nlm.nih.gov/25629559/>
[url_refer3]: <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1133952/>
[url_refer4]: <https://pubmed.ncbi.nlm.nih.gov/14687972/>
[url_refer5]: <https://pubmed.ncbi.nlm.nih.gov/25994114/>
[url_refer6]: <https://pubmed.ncbi.nlm.nih.gov/24034430/>
[url_refer7]: <https://pubmed.ncbi.nlm.nih.gov/24876380/>
[url_refer8]: <https://pubmed.ncbi.nlm.nih.gov/21246506/>
[url_refer9]: <https://pubmed.ncbi.nlm.nih.gov/24522957/>
[url_refer10]: <https://www.sciencedirect.com/science/article/abs/pii/S0141022907000191>
[url_refer11]: <https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/cssc.201200859>
[url_refer12]: <https://pubmed.ncbi.nlm.nih.gov/16673419/>
[url_refer13]: <https://pubmed.ncbi.nlm.nih.gov/26209638/>
[url_refer14]: <https://www.pnas.org/doi/10.1073/pnas.1309106110>
[url_refer15]: <https://www.pnas.org/doi/10.1073/pnas.1402518111>
[url_refer16]: <https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-9-500>