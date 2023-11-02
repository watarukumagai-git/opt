# review
## title
- Power load forecasting model based on CEEMDAN-VMD multiple noise reduction decomposition optimization DBO-LTSM

## japanese content
### [abstract]
- 本論文は、組み合わせた予測モデルが構築される、電力負荷データの時間的•空間的なゆらぎやランダム性を扱うために。
- 予測モデルはmultilevel noise reduction、 variational modal decomposition、Dung beetle optimizer (DBO)を組み込んだlong-term and short-term memory network (LSTM)に基づいている。
- まず、オリジナルデータのノイズ除去のために適応フィルタを使う。そのとき最初に、Complete Ensemble Empirical Mode Decomposition with Adaptive Noise (CEEMDAN)とdecomposed intrinsic mode functions (IMFs) によって、データが合成される。
- これらは、common IMFs (Co-IMFs)を形成するために、sample entropyとK-Means clusteringの手法によって統合されている。
- 次に、高周波であるCo-IMF0は、variational mode decomposition (VMD)で処理される。 
- 最後に、dung beetle optimization algorithmがLSTMのパラメータを最適化するために使われた後、合成されたデータは予測され、重ね合わされる。
- これは合成モデルだが、データのマルチレベルノイズ削減とLSTMの最適化によって実現され、予測精度はより改善される。
- 実験データは、そのモデルのRMSE, MAPE, MAE, R-spureが1.90, 3.82, 0.90 and 0.99を示しており、短期および中期の電力負荷を予測する提案の合成モデルの有効性を示唆している。


### [1. Introduction]
- 現代の電力技術では、正確な短期電力負荷予測は、電力会社における将来電力発電計画のための重要な指針としてよく提供される。
- しかし、電力負荷予測は電力需要に関する様々な要因の影響でかなり複雑である。例えば、天候条件、休日、社会経済状況などである。
- 伝統的な電力負荷予測モデルは、初期には比較的簡易的な処理方法を用いて、過去の負荷データの時系列性に頼っている。
- 知られているテクニックは、将来のトレンドや状態を推測するgradient ruleである。
- 回帰モデルでは、負荷やその要因がそれぞれ独立変数と依存変数として考慮される。
- この2つの関係は、将来の負荷値を予測するために、回帰式を作ることで分析される。
- これらの間では、時系列手法が予測手法として最も知られている。the Autoregressive Integrated Moving Average (ARIMA)や Seasonal Autoregressive Integrated Moving Average (SARIMA) modelsのように。
- 加えて、gray modelsやneural network modelsも一部で使われる。
- しかしながら、これらの伝統的な手法は、非定常かつ非線形データを扱う能力が限定された状態なので、簡易な数学的関係として過去と将来データをしばしば見る。

- 近年、データ解析技術や深層学習の発展で、機械学習が電力負荷予測に適用されるようになった。
- 特に、Support Vector Machine (SVM)、Back Propagation (BP) neural network、K-Nearest Neighbor (KNN) neural network、Recurrent Neural Network (Gated Recurrent Unit)などは、この分野における古典的なモデルで、最も既存の電力負荷予測手法として組み込まれている。
- しかし、これらの伝統的なモデルは、ハイパーパラメータが適切に調整されていなければ、局所解やトレーニングにおけるオーバーフィッティングの課題に出くわす。
- この問題に対処するため、近年の研究では、優れた最適化アルゴリズムを予測手法に組み込んだ手法が提案されている。
- 例として、Sparrow Search Algorithm (SSA)によって最適化された、Least Squares Support Vector Machine (LSSVM)、Improved Particle Swarm Optimization (IPSO)によって最適化されたSVM、Improved Hunter-Prey Algorithm (LHPO)によって最適化されたKernel Extreme Learning Machine (KELM)、Spatial Autocorrelation and Convolutional Long Short-Term Memory (SAC-ConvLSTM)に基づく最新の手法、特異スペクトル分解に基づくCuckoo Searchによって最適化されたSVM、スマートメータデータに基づく分散型電力負荷予測のための非同期型連合学習、などが挙げられる。
- これらの優れた最適化アルゴリズムは、自動的なパラメータ最適化によって、モデルの処理速度と予測精度を高める。
- しかし、短期電力負荷データにおける一時的な変動、ノイズ、外れ値などのデータは、予測処理に干渉し、モデルが要求精度に達する上で難しくさせる。
- つまり、いくつかのデータ処理手法が負荷予測モデルで適用されてきた。Empirical Mode Decomposition (EMD)、Ensemble Empirical Mode Decomposition (EEMD)、 Complementary EEMD (CEEMD)、 Adaptive Noise Ensemble Empirical Mode Decomposition、the improved CNN model based on Encoder-Decoderなど。

- 上記の分析に基づき、この研究は短期予測モデルの精度を高めるために、データ前処理のために、the fully adaptive noise ensemble empirical mode decomposition methodの改善したバージョンを適用する。
- その後、LSTM neural networkのハイパーパラメータのために、DBOによって最適化された統合した予測モデルを構築する。
- 初めに、生データからノイズ除去するためにCEEMDAN-VMDが使われる。
- そして、優れたDBOの最適化戦略がLSTMのハイパーパラメータを自動的に最適化するために活用される。
- 結果的なモデルは、各要素を個別に予測するために使われる。
- 最後に、個別の予測結果は、最終的な予測データを得るために、集約されて組み合わせられる。


### [2. データ処理]



### [3. DBO最適化]


### [4. 分析とシミュレーションの例]


### [5. Conclusion]
- 現代の電力システムにおける短期的な電力負荷予測の課題への対処について、本研究はベンチマークとして関連する気象データかつ一時的なデータに沿って、年度の電力負荷データを使った。
- この研究は、短中期の電力負荷予測のために、CEEMDAN-VMD multi-level noise reductionとDBO-LSTMに基づく結合モデルを導入した。
- さらにこのモデルは、multiple network models and optimization algorithm modelsと比べて検証された。
- 主要な結論は以下の通り:
- (1) 古典的な予測モデルとは異なり、この研究は、風力フォームの風力発電の時系列データをノイズ削減された成分に逐次的に分解するために、CEEMDAN-VMDを組み込む。このアプローチは、同じ方式の環境下で新たに設立された風力発電基地からの特徴の統合を容易にする。その後、予測モデルは要素毎に、特に統合モデルの予測精度を改善するために開発された。
- (2) 他のモデルのデータ比較に基づき、電力予測タスクにおけるCEEMDAN-VMD-DBO-LSTMモデルの優位性が検証された。このモデルは予測精度と誤差削減という観点で長所を示している。将来の研究やモデル強化のためのロバスト基盤を提供することで。
- (3) このモデルは、様々な環境に適用可能である。水処理予測において、水需要に応じて合理的な計画を支援する。仮想的には、電力網負荷予測において、このモデルは酷い干ばつ、台風、激しい雨のような激しい天候条件に置かれた課題に取り組む上で、共同体を効率的に支援する。これは、異なるセクターがよりスムーズに予測したり、電力網を安定化させるのに役立つ。



# [comments]
## [major comment1]
- 本論文の大きな目的は短期電力負荷予測の精度を改善だが、サブの目的は何か？いくつかのアルゴリズムを組み合わせて提案手法を構築した理由は、電力負荷データの時間的•空間的なゆらぎやランダム性を扱うためだと推察する。このため、Chapter1では、上記を扱うことで精度改善を図ることを目的とする、と明記すべきだ。
- 機械学習のハイパーパラメータを上位の最適化機能によって自動調整するアイディアは新しくない。

## [major comment2]
- 本論文の新規性•創造性はそれぞれ何か？In my understanding, 本論文の新規性はアルゴリズムCEEMDE-VMDを開発したこと？

## [major comment3]
- 各TableとFigureの周辺スペース(本文とのスペース、Table同士のスペース、captionとのスペース)がかなり狭い。
- これらは、TEEEの論文フォーマットで指定されているはずなので、確認して必要なら修正すべき。

## [major comment4]
- 4.5.1節から4.5.3節は一つの節に統合すべきだろう。
現在の原稿では、各節の小さな目的に対応して、Table4からTable6、Fig.2からFig.4のそれぞれで、予測性能を比較しているが、全体的な性能の比較がしにくい。
- さらに、4.5.1節から4.5.3節の目的に対して、各Tableにおける比較対象は不適切だと思われる。
- 例えば、4.5.3節は、LSTMのハイパーパラメータチューニングのために用いた最適化アルゴリズムの影響を調べるパートである。このため、SSA,MVO,PSO,DBOの4種をLSTMに適用した手法同士を調べるのが平等である。しかし、Table6では、SSA,MVO,PSO-LSTMと他の技術が含まれる提案手法を比較されている。
- よって、Table4からTable6は、全て一つの表に統一した上で、各検証目的に応じて、比較手法を適切に選び、結果を考察するのが良いだろう。

## [major comment5]


## [major comment6]
- 4.5.4節のFig.6とTable7は、他の手法との比較があるほうが適切だと思われる。


## [minor comment1]
- correspondenceの引用マークは、タイトルではなく、correspondence authorで引用されるべきだ。
