# english review comments
- This paper constructs the prediction method by combining with the CEEMDAN-VMD and DBO-LSTM algorithms for electrical power load forcasting task. Moreover, it is verified that the prediction performance of this method is superior to several machine learning algorithms through numerical simulation using wind power data. 
- It provides an interesting data through many comparisons, but I think it still needs extensive revisions to be acceptable for publication in terms of originality, creativity, and readability. 
- From this reason, the judgement is "C" (Rereview after major revision). It should be revised according to following major comments and improved as necessary.

## [Major Comments]
## major comment1 (General)
- What is the originality and creativity of this paper?
- The originality and creativity written in the current manuscript may not reach the level required for publication in this journal for the following reasons:
   - CEEMDAN-VMD, LSTM, and DBO algorithm as elements of the prediction method have been developed in other literature.
   - I guess the electrical power load prediction problem is generally well known and this paper do not add special or difficult situaions. Therefore, the problem formulation is existing.
   - The idea is existing which machine learning or deep learning's hyperparamter tuning by high-level optimization function. This has been a necessary task in recent years to bring the performance of deep learning to a practical level in various tasks and be well-known as automated machine learning (AutoML) / Neural Architecture Search (NAS). For example, the exsiting studies [28]-[30] get neural network's hyperparameters by them and improve the prediction performance in various tasks. And, the study[] costructs and uses the LSTM optimized by DBO. Therefore, introducing optimization function is existing. [11] https://ieeexplore.ieee.org/document/10257027.
   - Especially, the referenced paper [26] costructs a prediction method by combining with CEEMDAN and LSTM; and applies this to power load data. the exsiting studies [31]-[33] propose a methodology that LSTM-based prediction model is applied after data prepocessing combined with CEEMDAN and VMD is applied. They are very similar to the prediction methods in this paper.
- 一方、In my understanding, Fig.1に示すように、CEEMDAN-VMDによるデータ処理の構成方法や、このデータ処理法とLSTMによる予測手法の組み合わせ方に、本論文の新規性・創造性があると推察する。
- しかし、本論文が提案している部分や他の文献との差異が明記されていないため、私は本論文の新規性•創造性を判断できない。
- Overall, please specify the originality and creativity of this paper in Chapter 1 with attention to differences from other literature.

## major comment2 (General)
- The main purpose of this paper is to improve the prediction accuracy for short-term power load forcasting task. But what is the secondary purpose or motivation? I guess the reason why this paper uses the prediction method combined with some algorithms is to deal with the time and space fluctuation and randomness of power load data.
- Overall, please describe "The main purpose of this study is to improve the prediction accuracy for short-term power load forcasting task by dealing with the time and space fluctuation and randomness of power load data." in Chapter 1.

## major comment3 (General)
- Please review the current manuscript structure so that the reader can understand the originality and creativity of this paper of this paper. According to the general format, this paper should consist of introduction (Chapter 1), denosing time-series data / prediction method (Chapters 2 and 3), results and discussion (Chapter 4). 
- Overall, please revise the manuscript's structure according to the following my ideas:
   - Chapter 2's title should be revised to "Denoising Time-Series Data" because this part explains the denoising method, not simply data processing.
   - Mathematical equations and algorithms of each methods, which are not directly related to the original or creative ideas of this paper or used as tool, should be removed or transfered to Additional Materials (Appendix) after rewriting them correctly. For example, CEEMDAN algorithm (from Eqs.(1) to (6)), Sample Entropy algorithm (from Eqs.(7) to (10)), Variational Mode Decomposition algorithm (from Eqs.(11) to (16)), and DBO algorithm parts (from Sections 3.1 to 3.3).
   - Explanation of denoising methods combined with CEEMDAN-VMD and Sanple Entropy, which is the part shown at the top of Fig.1, should be added to new Section 2.4.
   - Some sentences for the combined data-processing steps in Section 4.2 should be transfered to new Section 2.4. 
   - Chapter 3's title should be revised to "LSTM-Based Prediction Method" because this part explains the prediction method combined with data-processing method and DBO is simply used as tool.

## major comment4 (Chapter 3, Page 3)
- What is the reason for using DBO as optimization algorithm?
- I would guess that the answer is "because DBO showed the best performance through numerical experiments in Section 4.5", and I believe that this is not valid for any other task.
- If this reason is correct, using DBO is not an original idea for this paper.
- Moreover, there are many misstatements in the DBO algorithm's part of the current manuscript comparing with the DBO's original paper [34]. Details are described in minor comments.
- Overall, please modify the following items:
   - To specify "To determine LSTM’s hyperparameters by an outside optimization function is categorized as a machine learning's hyperparameter tuning problem, i.e, black-box optimization. Although there are many known metaheristic algorithms for black-box optimization, this study uses DBO [34] which had the best performance in Section 4.5." in Chapter 3 citing the DBO's original paper [34].
- Otherwise, please specify why DBO is best choice for the LSTM performance in various tasks.

## major comment5 (Section 3.5, Page 4)
- Parameters and Variables should be 区別しされるべきだ。
- しかし、Table2はこれらを区別せずに表記しており、読者に混乱を生じさせる。
- What are the LSTM's hyperparameters optimized by DBO?
- Section 3.5 explains "the number of iterations, the learning rate, and the number of neurons in the hidden layer of LSTM", but Table 3 shows "Learning rate, the number of neurons in the hidden layer 1, and the number of neurons in the hidden layer 2". They are different.
- Please specify the optimization variables correctly.

## major comment6 (All Figures and Tables)
- The format of some figures and tables does not follow the author’s guidelines. The following items should be modified according to them for publication:
   - There is no explanation or legend about Fig.1. The explanation of configuration of Fig.1 and the expected effects should be added in the current manuscript. The "Appendix 2: Guidelines for Figures, Photographs and Tables Preparation" (https://www.iee.jp/wp-content/uploads/honbu/data-9014/ap02.pdf) says "As all figures and photographs should have captions, it is unacceptable without legend only Fig. ○. or (a)."
   - The font and subfigures in Fig.1 should be larger for visiblity. The "Appendix 2: Guidelines for Figures, Photographs and Tables Preparation" (https://www.iee.jp/wp-content/uploads/honbu/data-9014/ap02.pdf) says "Font size in figures, photographs and tables of 7 point should be used."
   - Although there should be plenty of space around tables and figures for visiblity, it is too small in the current manuscript, i.e., between figure and sentense, figure and it's caption, and tables. The "Appendix 1: Sample of Paper and Technical Note" (https://www.iee.jp/wp-content/uploads/honbu/data-9014/ap01.pdf) says "Double Space" around figures and tables.
   - 図表は上か下に寄せる

## major comment7 (From Sub-Sections 4.5.1 to 4.5.3, Page 7)
- 4.5.1節から4.5.3節は一つの節に統合すべきだろう。
現在の原稿では、各節の小さな目的に対応して、Table4からTable6、Fig.2からFig.4のそれぞれで、予測性能を比較しているが、全体的な性能の比較がしにくい。
- さらに、4.5.1節から4.5.3節の目的に対して、各Tableにおける比較対象は不適切だと思われる。
- 例えば、4.5.3節は、LSTMのハイパーパラメータチューニングのために用いた最適化アルゴリズムの影響を調べるパートである。このため、SSA,MVO,PSO,DBOの4種をLSTMに適用した手法同士を調べるのが平等である。しかし、Table6では、SSA,MVO,PSO-LSTMと他の技術が含まれる提案手法を比較されている。
- 前処理のやり方に新規性があるなら、先行研究の前処理と比べるのが適切では？
- よって、Table4からTable6は、全て一つの表に統一した上で、各検証目的に応じて、比較手法を適切に選び、結果を考察するのが良いだろう。

## major comment8 (From Sub-Sections 4.5.1 to 4.5.3, Page 7)
- 結果の考察がほぼ無い。比較を通して、なぜその有意差が出た理由は？

## major comment9 (Sub-Section 4.5.4, Page 8)
- 4.5.4節のFig.6とTable7は、他の手法との比較があるほうが適切だと思われる。The current manuscript shows the performance of the proposed PSO is superior to the classic GA and PSO in the path planning, but comparing them is questionable.

## major comment10 (Reference)
- 文献の引用を見直せ。例えば、[5][13]、[14][25]、[21][22]が同じ文献になっている。重複せずに引用すべき。



Although the author does not have to revise everything, please refer to the following minor comments for improving the current manuscript:
# [Minor Comments]
## minor comment1 (General)
- There are many misstatements in the current manuscript. While paying attention to the uniformity nd correspondences of symbols or words, please modify the following items:
- DBO algorithm (from Sections 3.1 to 3.3)
   - What is b in Eq.(17)? (Eq.(17), Page 3)
   - In the sentence "Here, t represents the number of iterations now, ...", where is t in Eq.(17)? In my understanding, population’s position at t-th iteration should be x_i(t). (Eq.(17), Page 3)
   - In the sentence "..., p is a constant belonging to (0,1).", where is p in Eq.(17)? (Under Eq.(17), Page 3)
   - Eq.(18) is exactly the same as Eq.(17) and shoulud be modified to the updating equation for dung ball rolling beetle's position if \delta>0.9. (Eq.(18), Page 3)
   - There is no equation for updating brood ball, but only an explanatory note about variable. (Page 4)
   - There are wrong equation numbers; for example, "defined in the aforementioned formula (3)" in top of Eq.(21) and "we know from formula (5)" in top of Eq.(24). (Page 4)
- LSTM (Section 3.4, Page 4)
   - "h_{t-1}" should be mathematical style. (top of Eq.(28))
   - What is the second equation? I guess 1つ目の式だけで十分である。(Eq.(29))
- Evaluation indicators (Section 4.3, Page 6)
   - Four metrics (RMSE, MAPE, MSE, and R-squared) are used in the experimental results, but the sentence "we use three main evaluation metrics in this paper." is written and there is no explanation of Eq.(34). (Top of Eq.(31))
   - In the MAPE definition (Eq.(32)), "n" and "N" are used in the same meaning although it is inferred that "n" is the number of data. Unify the letters. (Eq.(32))
   - In the R definition (Eq.(34)), the sum term on the right side in the denominator is included in the exponential part on the left side. Rewrite it correctly. (Eq.(34))
   - The experimental results use R-squared, but Eq.(34) is the definition equation of "Sample correlation coefficient" or "Pearson's correlation coefficient" between actual and estimated values. Specify the definition formula for R-squared correctly. (Eq.(34))
   - The only explanation for "p" from Eqs.(31) to (34) is "In this formula, p_estimate(i) and p_actual(i) are the predicted and measured values." in the current manuscript. Add the explanation "p is the objective variable of the LSTM model." (Under Eq.(34))
   - The symbols "p_estimate(i)" and "p_actual(i)" are too long for visiblity. Generally, "y" is used as the symbol of measured value of the objective variable and "$\hat{y}$" is used as the symbol of predicted value of the objective variable. I suggest "p_estimate(i)" and "p_actual(i)" are replaced by them.
- Model parameter setting (Section 4.4, Page 6)
   - Section 3.4 explains "the activation function (usually Sigmoid or ReLU)", but what is "selu" in Table 2? (Table 2)
   - What is "BWO"? (Top of Table 3)

## minor comment2 (Title, Page 1)
- Please remove the "1" at the end of the title if there is no particular reason.

## minor comment3 (Chapter 3)
- Although LSTM's hyperparameters is determined by DBO, DBO also has its own hyperparameters. In other words, the hyperparamters of high-level optimization function also affect the LSTM's prediction performance. Although the hyperparameters of metaheuristic algorithms can be flexibly set by the user according to the problem, it is difficult to find an appropriate setting-tuning method in black box problems and it is a common issue in this field.
- But, CMA-ES[35,36] and SHADE[37,38] have the ability to adaptively and automatically adjust its own hyperparameters. They known as novel algorithm and far superior to many algorithms in many benchmark problems or Black-Box functions. The fact is shown as several papers or the competition Black-Box Optimization Benchmarking held at top international conferences IEEE CEC and ACM GECCO[39]. If the authors think a difficulty to solve the machine learning or deep learning's hyperparamter tuning problem, CMA-ES / SHADE based algorithms are also expected to show higher performance than DBO in this case.
- While there is no need to change to these algorithms and revalidate them in this paper, please mention "DBO had the best performance in Section 4.5." as shown in the major comment 4.

## minor comment4 (Fig.1)
- この図を参考にわかりやすく描け
https://github.com/FateMurphy/CEEMDAN-VMD-GRU

## minor comment5 (Sub-Section 4.5.4, Page 8)
- Fig.6に示すように、CEEMDAN-VMD-DBO-LSTMのlong-term forcastingの予測精度は非常に良い。
- しかしながら、DBOの目的関数を学習データ全体の平均誤差(RMSE)としており、これは学習データに過学習する恐れがある。
- 一般的には、汎化性能を高めるために、Cross Validation（例えばK-Fold Cross Validationは，hold-outとLOOCVなど）を用いた評価指標を目的関数として使用する。
- 今後、この手法を色んなデータに適用する際には検討してほしい。

## minor comment6 (Reference)
- The references written in Chinese may be selective, but it is preferable to cite references written in English for this journal. Please cite any references written in English that provides an equivalent basis if possible. Otherwise, please add "(in Chinese)" at the end of Chinese references. For example, "The authors: "title", journal, pages (year) (in Chinese)".

# [Additional References]
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
