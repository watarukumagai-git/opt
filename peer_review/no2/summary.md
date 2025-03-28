# [japanese summary]
## title
- Power load forecasting model based on CEEMDAN-VMD multiple noise reduction decomposition optimization DBO-LTSM

## [abstract]
- 本論文は、組み合わせた予測モデルが構築される、電力負荷データの時間的•空間的なゆらぎやランダム性を扱うために。
- 予測モデルはmultilevel noise reduction、 variational modal decomposition、Dung beetle optimizer (DBO)を組み込んだlong-term and short-term memory network (LSTM)に基づいている。
- まず、オリジナルデータのノイズ除去のために適応フィルタを使う。そのとき最初に、Complete Ensemble Empirical Mode Decomposition with Adaptive Noise (CEEMDAN)とdecomposed intrinsic mode functions (IMFs) によって、データが合成される。
- これらは、common IMFs (Co-IMFs)を形成するために、sample entropyとK-Means clusteringの手法によって統合されている。
- 次に、高周波であるCo-IMF0は、variational mode decomposition (VMD)で処理される。 
- 最後に、dung beetle optimization algorithmがLSTMのパラメータを最適化するために使われた後、合成されたデータは予測され、重ね合わされる。
- これは合成モデルだが、データのマルチレベルノイズ削減とLSTMの最適化によって実現され、予測精度はより改善される。
- 実験データは、そのモデルのRMSE, MAPE, MAE, R-spureが1.90, 3.82, 0.90 and 0.99を示しており、短期および中期の電力負荷を予測する提案の合成モデルの有効性を示唆している。


## [1. Introduction]
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


## [2. データ処理]
### [2.1 CEEMDAN] 
- CEEMDANは、複雑な信号を扱う際に大きな利点をもたらす高度な信号分解手法である。その理論的基礎は主に経験的モード分解（EMD）に基づいており、さらにガウス白色雑音を導入することにより、適応雑音付き完全アンサンブル経験的モード分解（CEEMDAN）へと発展する。この発展により、EMDにおけるモード混合に効果的に対処できるようになった。さらに、CEEMDANは、各分解段階で特定の適応ノイズを組み込むことにより、EEMDアプローチを強化する。これにより、計算効率が向上するだけでなく、優れたモード分解結果が得られる。

### [2.2 Sample Entropy] 
- サンプルエントロピー（SampEn）は、時系列データの複雑さを測定するために用いられる統計手法である。Richmanらによって提案され、その目的はシステムの規則性と複雑性を定量的に記述することである。SampEnのコンセプトは、データの自己相似性と複雑性に基づいて構築されており、時系列データの不規則性を定量化することができる。SampEnの特筆すべき利点は、データの長さに対する依存性が弱いことであり、これは特徴を定量化する際の統計的安定性と適応性の高さにつながる。SampEnは、時系列に新しいパターンが出現する確率に基づいており、その複雑性を測定する。この文脈では、SampEnの値が低いほど、時系列における自己類似性が高く、新しいパターンが発生する確率が低いことを示し、単純であることを意味する。逆に、SampEn値が高いほど、時系列における自己相似性が低いことを意味し、新しいパターン生成の確率が高いことを示し、複雑性が増すことを示唆する。

### [2.3 Variational Mode Decomposition] 
- Variational Mode Decomposition（VMD）は、2014年にDragomiretskiyらによって革新的に設計された時間周波数解析ツールである。VMDの主な利点は、反復プロセス中に生じる可能性のある終点効果や誤解を招く成分の問題に対処しながら、多成分信号を複数の単一成分振幅・周波数変調信号に同時に分解する能力にある。解析的手法として、VMDは非線形で非定常な信号を扱うことができ、複雑な複数周波数信号をN個の固有モード関数（IMF）に分解する。さらに、VMDアルゴリズムの実装では、効果的なノイズ除去を達成するためにWienerフィルタリングが導入されている。各モード関数とその中心周波数を更新するために交互方向乗算法（ADMM）アプローチを利用することにより、各サブ信号は独立した中心周波数を獲得し、同時に帯域幅の推定とサブ信号の最小化が最小化される。これにより、各サブ信号の再構成結果は元の信号に近いものとなる。


## [3. DBO最適化]
- [3.1~3.3 DBO]
- [3.4 LSTM]
- [3.5 DBO-LSTM]

## [4. 分析とシミュレーションの例]
### [4.2 Data Pre-Processing]
- その後、データ処理を開始した。まず、元のデータのノイズ除去を行う必要があるため、本論文ではCEEMDAN法を採用し、元の電気負荷データを分解する。計算の複雑さを軽減し、モデル学習の速度を向上させ、オーバーフィッティングの問題を回避する。各IMFのサンプルエントロピーを求め、クラスタリングにk-means法を用いる。その後、3つの新しい統合された、すなわち、高周波数配列Co-IMF0（imf1-imf4を含む）、中周波数配列Co-IMF1
(imf5-imf7を含む）、低周波配列Co-IMF2（imf8-imf15を含む）である。3つのCo-IMFの変動パターンはいずれも比較的安定しており、各IMFの変動特性をさらに抽出して予測モデルを学習することが容易になる。一方、高周波数シーケンスを正確に予測するために、本論文ではそれらの二次分解のために可変モード分解（VMD）法を実装する。分解過程における分解不足や分解過剰の問題を避けるため、いくつかの異なるk値を試し、異なる中心周波数を計算し比較した。最終的に、VMDモデル分解のパラメータとしてk = 10を選択し、他のパラメータはデフォルト値を使用した。

### [4.5.1 Comparison of Model Prediction Metrics Before and After Optimization] 
- 提案モデルの有効性を検証するため、本論文ではまず同じ実験データを用いて、オリジナルのLSTMモデルとノイズ除去したDBO-LSTMモデルを比較した。実験後、比較結果を表4と図2に示す。

### [4.5.1 Comparison of Model Prediction Metrics Before and After Optimization] 
- 提案モデルの有効性を検証するため、本論文ではまず同じ実験データを用いて、オリジナルのLSTMモデルとノイズ除去したDBO-LSTMモデルを比較した。実験後、比較結果を表4と図2に示す。

### [4.5.2 Comparative Evaluation of Predictive Metrics for Classical Models] 
- 続いて、本稿では他の4つの典型的な予測モデルを選択した。を比較のために選んだ： BPニューラルネットワーク、K-最近傍（K-NN (K-NN）、XGBoost、サポートベクターマシン（SVM）である。これらを 提案するCEEMDAN-VMD-DBO-LSTMモデルと比較する。モデルと比較した。実験結果を表5と図3に示す：

### [4.5.3 Comparative Forecasting Analysis of Optimization Algorithms]
- さらに本稿では、他の3つの最適化アルゴリズムを選択する： SSA、MVO、PSOの3つの最適化アルゴリズムを選択し、提案するLSTMのCEEMDAN-VMD-DBO最適化手法と比較した。実験結果は表6と図4の通りである：
- 実験結果を統合した後、本論文では、RMSE、MAPE、MAEの観点から、他のベンチマークモデルと比較した提案モデルのデータ改善度を計算した。これらの改善点の可視化を図5に示す：
- 本研究で提案された予測モデルは、RMSE、MAPE、MAEにおいて40％以上の削減を達成していることが確認できる。これはモデルの有効性をさらに証明するものである。

### [4.5.4 Validation of Model Performance Over Extended Time Durations]
- 提案モデルの一般性、特に長期間にわたる精度を検証するために、本稿では検証セットとして、その後の7000件のデータを利用した。実験結果は表7と図6の通りである：
- 実験結果は、長期予測シナリオにおいて、モデルが高い精度を維持し続けることを示している。このことは、本稿で提案したモデルが汎用性があり、様々な時間期間にわたる予測タスクに適用可能であることを示唆している。まとめると、実験結果は、従来の予測モデルや最適化アルゴリズムと比較して、CEEMDAN-VMD-DBO-LSTMモデルの精度向上を様々な指標で明確に示している。これは、さまざまな時間スパンにおける電力予測タスクの優位性と汎用性を直接反映している。このモデルは、予測精度とエラー削減において顕著な利点を示し、将来の研究とモデル拡張のための強固な基盤を提供する。

## [5. Conclusion]
- 現代の電力システムにおける短期的な電力負荷予測の課題への対処について、本研究はベンチマークとして関連する気象データかつ一時的なデータに沿って、年度の電力負荷データを使った。
- この研究は、短中期の電力負荷予測のために、CEEMDAN-VMD multi-level noise reductionとDBO-LSTMに基づく結合モデルを導入した。
- さらにこのモデルは、multiple network models and optimization algorithm modelsと比べて検証された。
- 主要な結論は以下の通り:
- (1) 古典的な予測モデルとは異なり、この研究は、風力フォームの風力発電の時系列データをノイズ削減された成分に逐次的に分解するために、CEEMDAN-VMDを組み込む。このアプローチは、同じ方式の環境下で新たに設立された風力発電基地からの特徴の統合を容易にする。その後、予測モデルは要素毎に、特に統合モデルの予測精度を改善するために開発された。
- (2) 他のモデルのデータ比較に基づき、電力予測タスクにおけるCEEMDAN-VMD-DBO-LSTMモデルの優位性が検証された。このモデルは予測精度と誤差削減という観点で長所を示している。将来の研究やモデル強化のためのロバスト基盤を提供することで。
- (3) このモデルは、様々な環境に適用可能である。水処理予測において、水需要に応じて合理的な計画を支援する。仮想的には、電力網負荷予測において、このモデルは酷い干ばつ、台風、激しい雨のような激しい天候条件に置かれた課題に取り組む上で、共同体を効率的に支援する。これは、異なるセクターがよりスムーズに予測したり、電力網を安定化させるのに役立つ。
