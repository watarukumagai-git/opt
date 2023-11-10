# english review comments
## [main comments]
- This paper validates a forcasting/prediction method by being applied in electrical power load data.
- The prediction method is combined with the CEEMDAN-VMD and DBO-LSTM algorithms.
- Moreover, it is verified that the prediction performance of this method is superior to several machine learning algorithms through numerical simulation using wind power data.
- It provides an interesting data through many comparisons, but I think it still needs extensive revisions to be acceptable for publication in terms of originality, creativity, and readability.
- From this reason, the judgement is "C" (Rereview after major revision).
- It should be revised according to following major comments and improved as necessary.

## [major comments]
## major comment1 (General)
- What is the originality and creativity of this paper?
- The originality and creativity written in the current manuscript may not reach the level required for publication in this journal for the following reasons:
   - CEEMDAN-VMD, LSTM, and DBO algorithm as elements of the prediction method have been developed in other literature.
   - Morever, I guess the electrical power load prediction problem is generally well known and this paper do not add special or difficult situaions. Therefore, the problem formulation is existing.
   - The idea is existing which machine learning or deep learning's hyperparamter tuning by high-level optimization function. This has been a necessary task in recent years to bring the performance of deep learning to a practical level in various tasks and be well-known as automated machine learning (AutoML) / Neural Architecture Search (NAS). For example, the exsiting studies [28]-[30] get neural network's hyperparameters by them and improve the prediction performance in various tasks. Therfore, introducing optimization function is existing. 
   - Especially, the referenced paper [26] costructs a prediction method by combining with CEEMDAN and LSTM; and applies this to power load data. the exsiting studies [31]-[33] propose a methodology that LSTM-based prediction model is applied after data prepocessing combined with CEEMDAN and VMD is applied. They are very similar to the prediction methods in this paper.
- 一方、In my understanding, Fig.1に示すように、CEEMDAN-VMDによるデータ処理の構成方法や、このデータ処理法とLSTMによる予測手法の組み合わせ方に、本論文の新規性・創造性があると推察する。
- Overall, please specify the originality and creativity of this paper in Chapter 1 with attention to differences from other literature.

## major comment2 (General)
- The main purpose of this paper is to improve the prediction accuracy for short-term power load forcasting task.
- But what is the secondary purpose or motivation?
- I guess the reason why this paper uses the prediction method combined with some algorithms is to deal with the time and space fluctuation and randomness of power load data.
- Overall, please describe "The main purpose of this study is to improve the prediction accuracy for short-term power load forcasting task by dealing with the time and space fluctuation and randomness of power load data." in Chapter 1.

## major comment3 (General)
- Please review the current manuscript structure.
- According to the general format, this paper should consist of introduction (Chapter 1), denosing time-series data / prediction method (Chapters 2 and 3), results and discussion (Chapter 4).
- Overall, please revise the manuscript's structure according to the following my ideas:
   - Chapter 2's title should be revised to "Denoising Time-Series Data" because this part explains the denoising method not simply data processing.
   - Chapter 3's title should be revised to "LSTM-Based Prediction Method" because this part explains the prediction method.
   - Mathematical equations and algorithms of each methods, which are not directly related to the ideas of this paper or used as tool, should be removed or transfered to Additional Materials, i.e., Appendix after rewriting them correctly, e.g., CEEMDAN algorithm (from Eqs.(1) to (6)), Sample Entropy algorithm (from Eqs.(7) to (10)), Variational Mode Decomposition algorithm (from Eqs.(11) to (16)), and DBO algorithm parts (from Sections 3.1 to 3.3).
   - Explanation of denoising methods for time-series data by combined CEEMDAN-VMD, which is the part shown at the top of Fig.1, should be added to new Section 2.4.
   - Some sentences for the combined data-processing steps in Section 4.2 be transfered to Section 2.4. 

## major comment4 (Chapter 3, Page 3)
- What is the reason for using DBO as optimization algorithm?
- I would guess that the answer is "because DBO showed the best performance through numerical experiments in Section 4.5", and I believe that this is not valid for any other task.
- If this reason is correct, using DBO is not an original idea for this paper.
- Moreover, there are many misstatements in the DBO algorithm's part of the current manuscript comparing with the DBO's original paper [34]. Details are described in minor comments.
- Overall, please modify the following items:
   - To specify "To determine LSTM’s hyperparameters by an outside optimization function is categorized as a machine learning's hyperparameter tuning problem, i.e, black-box optimization. Although there are many known metaheristic algorithms for black-box optimization, this study uses DBO [34] which had the best performance in Section 4.5." in Chapter 3 citing the DBO's original paper [34].
- Otherwise, please specify why DBO is best choice for the LSTM performance in various tasks.

## major comment5 (Section 3.5, Page 4)
- What are the LSTM's hyperparameters optimized by DBO?
- Section 3.5 explains "the number of iterations, the learning rate, and the number of neurons in the hidden layer of LSTM", but Table 3 shows "Learning rate, the number of neurons in the hidden layer 1, and the number of neurons in the hidden layer 2". They are different.
- Please specify the optimization variables correctly.

## major comment6 (Fig.1, Page 5)
- There is no explanation about Fig.1.
- Please add an explanation of configuration of Fig.1 and the expected effects after making the text and subfigures in Fig.1 larger for visible. 

## major comment7 (All Figures and Tables, Pages 6 to 8)
- 各TableとFigureの周辺スペースがかなり狭い。
- 具体的には、Figureと本文のスペース、Figureとcaptionとのスペース、Table同士のスペース。
- これらは、TEEEの論文フォーマットで指定されているはずなので、確認して必要なら修正すべきだ。

## major comment8 (From Sub-Sections 4.5.1 to 4.5.3, Page 7)
- 4.5.1節から4.5.3節は一つの節に統合すべきだろう。
現在の原稿では、各節の小さな目的に対応して、Table4からTable6、Fig.2からFig.4のそれぞれで、予測性能を比較しているが、全体的な性能の比較がしにくい。
- さらに、4.5.1節から4.5.3節の目的に対して、各Tableにおける比較対象は不適切だと思われる。
- 例えば、4.5.3節は、LSTMのハイパーパラメータチューニングのために用いた最適化アルゴリズムの影響を調べるパートである。このため、SSA,MVO,PSO,DBOの4種をLSTMに適用した手法同士を調べるのが平等である。しかし、Table6では、SSA,MVO,PSO-LSTMと他の技術が含まれる提案手法を比較されている。
- よって、Table4からTable6は、全て一つの表に統一した上で、各検証目的に応じて、比較手法を適切に選び、結果を考察するのが良いだろう。

## major comment9 (From Sub-Sections 4.5.1 to 4.5.3, Page 7)
- 結果の考察がほぼ無い。比較を通して、なぜその有意差が出た理由は？

## major comment10 (Sub-Section 4.5.4, Page 8)
- 4.5.4節のFig.6とTable7は、他の手法との比較があるほうが適切だと思われる。

## major comment11 (Sub-Section 4.5.4, Page 8)
- 学習データ全体の平均誤差（RMSE）を目的関数と設定することは、学習データに過学習する恐れがある。一般的には、汎化性能を高めるために、Cross Validation（例えばK-Fold Cross Validationは，hold-outとLOOCVなど）を用いた評価指標を目的関数として使用する。しかしながら、Fig.6に示すように、CEEMDAN-VMD-DBO-LSTMのlong-term forcastingの予測精度は良い。本論文ではどうしているのか？もし


Although the author does not have to revise everything, please refer to the following minor comments for improving the current manuscript:
# [minor comments]
## minor comment1 (General)
- There are many misstatements in the current manuscript. While paying attention to the uniformity nd correspondences of symbols or words, please modify the following items:
- DBO algorithm (from Sections 3.1 to 3.3)
   - What is b in Eq.(17)? (Eq.(17), Page 3)
   - In the sentence "Here, t represents the number of iterations now, ...", where is t in Eq.(17)? In my understanding, population’s position at t-th iteration should be x_i(t). (Eq.(17), Page 3)
   - In the sentence "..., p is a constant belonging to (0,1).", where is p in Eq.(17)? (Under Eq.(17), Page 3)
   - Eq.(18) is exactly the same as Eq.(17) and shoulud be modified to the updating equation for dung ball rolling beetle's position if \delta>0.9. (Eq.(18), Page 3)
   - There is no equation for updating brood ball, but only an explanatory note about variable. (Page 4)
- LSTM (Section 3.4, Page 4)
   - "h_{t-1}" should be mathematical style. (top of Eq.(28), Page 4)
   - What is the second equation? I guess 1つ目の式だけで十分である。(Eq.(29), Page 4)
- Evaluation indicators (Section 4.3, Page 6)
   - In the MAPE definition (Eq.(32)), "n" and "N" are used in the same meaning although it is inferred that n is the number of data. Unify the letters. (Eq.(32))
   - In the experimental results, four metrics (RMSE, MAPE, MSE, and R-squared) are used, but the words "three main metrics" is used in the text describing the evaluation indicators. (Top of Eq.(31))
   - In the R definition (Eq.(34)), the sum term on the right side in the denominator is included in the exponential part on the left side. (Eq.(34))
   - The experimental results use R-squared, but Eq.(34) is the definition equation of Sample correlation coefficient or Pearson's correlation coefficient between actual and estimated values. Specify the definition formula for R-squared. (Eq.(34))
   - The only explanation for "p" from Eqs.(31) to (34) is "In this formula, p_estimate(i) and p_actual(i) are the predicted and measured values." in the current manuscript. Please add that "p is the objective variable of the LSTM model." (Under Eq.(34))
   - The caption symbols "p_estimate(i)" and "p_actual(i)" from Eqs.(31) to Eq.(34) are too long. のpのmeasured/predicted valueの変数は、下付けが長すぎる。一般的には、measured valueの変数としてp、predicted valueの変数としてp^\hatを用いることが多い。また、これらを使うことで数式がきれいに見えるだろう。
- Model parameter setting (Section 4.4, Page 6)
   - Section 3.4 explains "the activation function (usually Sigmoid or ReLU)", but what is "selu"? in Table 2? (Table 2)
   - What is "BWO"? (Top of Table 3)

## minor comment2 (Title, Page 1)
- Please remove the "1" at the end of the title if there is no particular reason.

## minor comment3 (Chapter 3)
- DBOによって、LSTMのハイパーパラメータを調整しているが、DBOアルゴリズムにもハイパーパラメータが存在する。
- つまり、上位の最適化機能におけるハイパーパラメータの設定も、LSTMの予測性能に影響を与える。
- メタヒューリスティクスのハイパーパラメータはユーザが対象問題に応じて柔軟に設定できるが、ブラックボックスの問題において適切な設定•調整方法が困難であることは、この分野で一般的に知られている課題である。
- 一方、文献[29]のブラックボックス最適化のコンペティションが開催されている。
- このランキング上位のアルゴリズムとして、CMA-ES[30]やSHADE[31]が知られており、これらのアルゴリズムは、自身のハイパーパラメータを適応的かつ自動的に調整する機能を有しており、様々なブラックボックスの問題において高い性能を示す。
- このため、本論文のLSTMのハイパーパラメータ自動調整問題において、私はDBOよりもCMA-ESやSHADEが適切だと考えられる。
- 本論文では、これらのアルゴリズムに変更して検証し直す必要はないが、DBOがベストな選択肢ではなく、この問題でたまたま最善であったことを言及する必要があるだろう。

## minor comment4 (Reference)
- referenced paperが中国語で執筆された文献に集中している恐れがある。このジャーナルは国際的なもので英文で執筆されるため、英文で執筆された文献を引用することが望ましい。同等の根拠を示す上で、適切な英文文献が無ければ、中国語文献の末尾に"(in Chinese)"と追記せよ。

- [28]: J. Waring et al.: "Automated machine learning: Review of the state-of-the-art and opportunities for healthcare,
   Artificial Intelligence in Medicine, Vol. 104, page 101822 (2020)
- [29]: R. Luo et al.: "Neural Architecture Optimization", Advances in Neural Information Processing Systems, Vol. 31, pp. 1–12 (2018)
- [30]: P. Ren et al.: "A comprehensive survey of neural architecture search: Challenges and solutions", ACM Computing Surveys, Vol. 54, No. 4, Article No.76, pp. 1–34 (2021)
- [31]: "TCN Short-Term Water Level Prediction Based on CEEMDAN-VMD Time-Frequency Double Layer Feature Extraction",
- [32]: "Precipitation prediction based on CEEMDAN–VMD–BILSTM combined quadratic decomposition model",
- [33]: "Ultra-Short-Term Power Prediction of a Photovoltaic Power Station Based on the VMD-CEEMDAN-LSTM Model", 
- [34]: : "Dung beetle optimizer: a new meta-heuristic algorithm for global optimization", (2023).
- [35]: N. Hansen et. al: "Impacts of Invariance in Search: When CMA-ES and PSO Face Ill-Conditioned and Non-Separable Problems", Journal of Applied Soft Computing, pp. 5755-5769 (2011)
- [36]: N. Hansen: "Benchmarking a BI-population CMA-ES on the BBOB-2009 function testbed", Workshop Proceedings of the GECCO Genetic and Evolutionary Computation Conference, pp. 2389–2396 (2009)
- [37]: R. Tanabe and A. Fukunaga: "Success-History Based Parameter Adaptation for Differential Evolution," Proceedings of the 2013 IEEE Congress on Evolutionary Computation, pp. 71-78 (2013)
- [38]: R. Tanabe and A. Fukunaga: “Improving the Search Performance of SHADE Using Linear Population Size Reduction,” Proceedings of the 2014 IEEE Congress on Evolutionary Computation, pp. 1658-1665 (2014)
- [39]: The Black-box Optimization Benchmarking (BBOB) Workshop, http://numbbo.github.io/workshops/index.html
