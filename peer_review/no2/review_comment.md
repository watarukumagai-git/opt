# english review comments
- This paper constructs the prediction method by combining with the CEEMDAN-VMD and DBO-LSTM algorithms for electrical power load forcasting task. Moreover, it is verified that the prediction performance of this method is superior to several machine learning algorithms through numerical simulation using wind power data. 
- It provides an interesting data through many comparisons, but I think it still needs extensive revisions to be acceptable for publication in terms of originality, creativity, and readability. 
- From this reason, the judgement is "C" (Rereview after major revision). It should be revised according to following major comments and improved as necessary.

## [Major Comments]
## major comment1 (General)
- What is the originality and creativity of this paper? The originality and creativity written in the current manuscript may not reach the level required for publication in this journal for the following reasons:
   - CEEMDAN-VMD, LSTM, and DBO algorithm as elements of the prediction method have been developed in other literature.
   - I guess the electrical power load prediction problem is generally well known and this paper do not add special or difficult situaions. Therefore, the problem formulation is existing.
   - The idea of machine learning or deep learning's hyperparamter tuning by high-level optimization function already exists. This has been a necessary task in recent years to bring the performance of deep learning to a practical level in various tasks and be well-known as automated machine learning (AutoML) / Neural Architecture Search (NAS). For example, the exsiting studies [28-30] get neural network's hyperparameters by them and improve the prediction performance in various tasks. The study [31] costructs the LSTM optimized by DBO and applies it to short-term load forecasting task. Therefore, introducing optimization function is existing. 
   - The idea which time-series data is denoised by combined with some decomposition or integration before prediction already exists. The exsiting studies [32-35] propose a methodology that prediction model is applied after data prepocessing combined with multiple decompositions, which is the secondary decomposition to highest frequency sequences after signal decomposition, and be well-known as two-stage decomposition, . Especially, [34] apply VMD to highest frequency sequences after CEEMDAN and k-means clustering using Sample Entropy. They are very similar to the denosing method in this paper.
- On the other hand, I guess the originality and creativity of this paper are related to how to carry out denosing time-series data by combining with CEEMDAN, VMD, and Sample Entropy-based clustering. However, I cannot judge the originality and creativity because it does not clearly state the proposal parts and the difference from other literature. 
- Overall, please specify the originality and creativity of this paper in Chapter 1 with attention to differences from other literature.


## major comment2 (General)
- The main purpose of this paper is to improve the prediction accuracy for short-term power load forcasting task. But what is the secondary purpose or motivation? I guess the reason why this paper uses the prediction method combined with some algorithms is to deal with the time and space fluctuation and randomness of power load data.
- Overall, please describe "The main purpose of this study is to improve the prediction accuracy for short-term power load forcasting task by dealing with the time and space fluctuation and randomness of power load data." in Chapter 1.


## major comment3 (General)
- Please review the current manuscript structure so that the reader can understand the originality and creativity of this paper of this paper. According to the general format, this paper should consist of introduction (Chapter 1), related methodology (Chapter 2), proposed method (Chapters 3), results and discussion (Chapter 4).
- Overall, please revise the manuscript's structure according to the following my ideas:
   - Chapter 2's title should be revised to "Related Methodology" and Chapter 2 should include the element of the combined methods; i.e., CEEMDAN, Sample Entropy, Variational Mode Decomposition, and LSTM.
   - Chapter 3's title should be revised to "Proposed Method" and Chapter 3 should include an explanation of how to combine with denoising time-series data and prediction methods. The denosing method is combined with CEEMDAN, Sample Entropy, and VMD, which is the part shown at the top of Fig.1 and some sentences for the combined data-processing steps in Section 4.2 in my understanding. The prediction method is combined with LSTM and DBO.
   - Some mathematical equations and algorithms of each methods are not directly related to the original or creative ideas of this paper or used as tool. Moreover, there are many misstatements in them of the current manuscript comparing with the original paper. Details are described in minor comments. They should be removed from the current manuscript or transfered to Additional Materials (Appendix) after rewriting them correctly. For example, CEEMDAN algorithm (from Eqs.(1) to (6)), Sample Entropy algorithm (from Eqs.(7) to (10)), Variational Mode Decomposition algorithm (from Eqs.(11) to (16)), and DBO algorithm parts (from Sections 3.1 to 3.3).
   - For overall performance comparisons, Subsections 4.5.1 through 4.5.3 should be combined into a single section, Table 4 through Table 6 into a single table, and Fig.2 through Fig.4 into a single figure for short-term prediction using two-column wide table and subfigure configuration (Fig.2(a),(b),(c)) as needed. The combined Subsection 4.5.1 shows short-term prediction and the new Subsection 4.5.2 shows long-term prediction.


## major comment4 (Chapter 3, Page 3)
- What is the reason for using DBO as optimization algorithm? I would guess that the answer is "because DBO showed the best performance through numerical experiments in Section 4.5", and I believe that this is not valid for any other task.
- If this reason is correct, using DBO is not an original idea for this paper. Overall, please specify "To determine LSTM’s hyperparameters by an outside optimization function is categorized as a machine learning's hyperparameter tuning problem, i.e, black-box optimization. Although there are many known metaheristic algorithms for black-box optimization, this study uses DBO [37] which had the best performance in Section 4.5." in Chapter 3 citing the DBO's original paper [37].
- Otherwise, please specify why DBO is best choice for the LSTM performance in various tasks.


## major comment5 (Section 3.5, Page 4)
The parameters and variables for LSTM's optimization should be distinguished and correctly. But, Table2 does not distinguish between them and it creats confusion for the reader. Please specify them correctly according to the following items:
   - What are the LSTM's hyperparameters optimized by DBO? Section 3.5 explains "the number of iterations, the learning rate, and the number of neurons in the hidden layer of LSTM", but Table 3 shows "Learning rate, the number of neurons in the hidden layer 1, and the number of neurons in the hidden layer 2". They are different. I guess "the number of iterations" is DBO's loop times and given by the users. Please specify the optimization variables correctly. 
   - What does "Fitness Function: RMSE=1" mean in Table2? It shows the type of evaluation index as the objective function for DBO, not value.
   - Although "Neuron number of range" is [10, 100] in Table2, "Number number in Layer2" is 213 in Table3. It shows the network violates the constraints.
   - A collumn for attribute should be added to left side of Table2. The legend of the attributes are "DBO's hyperparameter", "Fixed LSTM's hyperparameter", and "Upper and lower range of LSTM hyperparameter". The first includes population size to stealing cockroach ratio, the second includes "Fitness Function" and Activation Function, and the third includes "Learning Rate Range" and "Neuron Number Range".


## major comment6 (Chapter 4)
I also doubt the usability of CEEMDAN-VMD-DBO-LSTM is varified from the results and The comparison/discussion of results is very questionable. Please revise it with attention to the following points:
   - There is no discussion for the results. What is the reason there is the difference between CEENDAN-VMD-DBO-LSTM and the others?
   - The compared methods is questiable. Table4 shows the effect of denoising method, Table5 shows the superioty of LSTM-based prediction method, and Table6 shows the superiority of DBO-based optimization method. But if the denoising time-series data method of CEEMDAN-VMD-DBO-LSTM is the originality of this paper, please provide an additional results using the other denosing methods [21-26,32-36].
   - Why is there no comparison with other methods for long-term forcasting task? To validate the superiority of CEEMDAN-VMD-DBO-LSTM, the paper needs to compare CEEMDAN-VMD-DBO-LSTM with other methods for long-term forcasting task.
   - I cannot understand the logic that if long-term forcasting in one term is accurate, it has high generality. To show and validate the generality of CEEMDAN-VMD-DBO-LSTM, please provide an additional results using data from each season even short-term forecast task.


## major comment7 (All Figures and Tables)
The format of some figures and tables does not follow the author’s guidelines. The following items should be modified according to them for publication:
   - There is no explanation or legend about Fig.1. The explanation of configuration of Fig.1 and the expected effects should be added in the current manuscript.
   - The font and subfigures in Fig.1 should be larger for visiblity. The "Appendix 2: Guidelines for Figures, Photographs and Tables Preparation" (https://www.iee.jp/wp-content/uploads/honbu/data-9014/ap02.pdf) says "Font size in figures, photographs and tables of 7 point should be used."
   - Although there should be plenty of space around tables and figures for visiblity, it is too small in the current manuscript, i.e., between figure and sentense, figure and it's caption, and tables. The "Appendix 1: Sample of Paper and Technical Note" (https://www.iee.jp/wp-content/uploads/honbu/data-9014/ap01.pdf) says "Double Space" around figures and tables.
   - The position of figures, photographs and tables inserted should be at the tops and bottoms of columns. Avoid placing them in the middle of columns. (https://www.iee.jp/wp-content/uploads/honbu/32-doc-kenq/guideline.pdf)


## major comment8 (Reference)
Review the citation of references accoding to the following items:
- The referenced papers [5][13], [14][25], [21][22] are the same references. They should be cited without duplication.(Chapter 1)
- "if hyperparameters are not properly adjusted (Feng J., Yang J., 2021)[12].", but the authour's name may be "(Fan, G.-F. et al. 2023)[12]" (Chapter 1).
- "Examples include the Least Squares Support Vector Machine (LSSVM) model optimized by Sparrow Search Algorithm (SSA)[13]-[14]", but the reference paper [14] may use the arithmetic optimization algorithm (AOA), not SSA (Chapter 1).
- "the new algorithm based on Spatial Autocorrelation and Convolutional Long Short-Term Memory (SAC-ConvLSTM)[17]-[18]", but the reference paper [17] do not use SAC-ConvLSTM (Chapter 1).



# [Minor Comments]
Although the author does not have to revise everything, please refer to the following minor comments for improving the current manuscript:

## minor comment1 (General)
There are many misstatements in the current manuscript. While paying attention to the uniformity and correspondences of symbols or words, please modify the following items:
- DBO algorithm (from Sections 3.1 to 3.3)
   - What is b in Eq.(17)? (Eq.(17), Page 3)
   - In the sentence "Here, t represents the number of iterations now, ...", where is t in Eq.(17)? In my understanding, population’s position at t-th iteration should be x_i(t). (Eq.(17), Page 3)
   - In the sentence "..., p is a constant belonging to (0,1).", where is p in Eq.(17)? (Under Eq.(17), Page 3)
   - Eq.(18) is exactly the same as Eq.(17) and shoulud be modified to the updating equation for dung ball rolling beetle's position if \delta>0.9. (Eq.(18), Page 3)
   - There is no equation for updating brood ball, but only an explanatory note about variable. (Page 4)
   - There are wrong equation numbers; for example, "defined in the aforementioned formula (3)" in top of Eq.(21) and "we know from formula (5)" in top of Eq.(24). (Page 4)
- LSTM (Section 3.4, Page 4)
   - "h_{t-1}" should be mathematical style. (top of Eq.(28))
   - What is the second formula in Eq.(29)? I guess the first formula is sufficient. (Eq.(29))
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
Please remove the "1" at the end of the title if there is no particular reason.


## minor comment3 (Chapter 3)
- Although LSTM's hyperparameters is determined by DBO, DBO also has its own hyperparameters. In other words, the hyperparamters of high-level optimization function also affect the LSTM's prediction performance. Although the hyperparameters of metaheuristic algorithms can be flexibly set by the user according to the problem, it is difficult to find an appropriate setting-tuning method in black-box problems and it is a common issue in this field.
- But, CMA-ES[37,38] and SHADE[39,40] have the function of adaptive and automatic adjusting its own hyperparameters. They known as novel algorithm and far superior to many algorithms in many benchmark problems or black-box functions. The fact is shown as several papers or the competition Black-Box Optimization Benchmarking held at top international conferences IEEE CEC and ACM GECCO[41]. If the authors think a difficulty to solve the machine learning or deep learning's hyperparamter tuning problem, CMA-ES / SHADE based algorithms are also expected to show higher performance than DBO in this case.
- While there is no need to change to these algorithms and revalidate them in this paper, please mention "DBO had the best performance in Section 4.5." as shown in the major comment 4.


## minor comment4 (Fig.1)
Please redraw Fig.1 for clarity refering to the figure about denosing steps in the exsisting studies [32-35].


## minor comment5 (Subsection 4.5.4, Page 8)
Fig.6 shows the prediction accuracy of CEEMDAN-VMD-DBO-LSTM for long-term forcasting case (about 2.5 months) is quite high although the objective function of DBO is set as the mean error (RMSE) of the entire training data. I guess it is may this could an over-fitting for the training data. In general, the evaluation index based on the cross validation (e.g., K-fold, hold-out, and LOOCV) is used for the objective function.
- Please consider applying this method to various types of data in the future.


## minor comment6 (Reference)
The references written in Chinese may be selective, but it is preferable to cite references written in English for this journal. Please cite any references written in English that provides an equivalent basis if possible. Otherwise, please add "(in Chinese)" at the end of Chinese references. For example, "The authors: "title", journal, pages (year) (in Chinese)".


# [Additional References]
- [28]: J. Waring et al.: "Automated machine learning: Review of the state-of-the-art and opportunities for healthcare,
   Artificial Intelligence in Medicine, Vol. 104, page 101822 (2020)
- [29]: R. Luo et al.: "Neural Architecture Optimization", Advances in Neural Information Processing Systems, Vol. 31, pp. 1–12 (2018)
- [30]: P. Ren et al.: "A comprehensive survey of neural architecture search: Challenges and solutions", ACM Computing Surveys, Vol. 54, No. 4, Article No.76, pp. 1–34 (2021)
- [31]: Y. Zhang et al.: "Short-Term Load Forecasting Based on DBO-LSTM Model", 2023 3rd International Conference on Energy Engineering and Power Systems (EEPS), pp. 972-977 (2023)
- [32]: X. Zhang et al.: "Precipitation prediction based on CEEMDAN–VMD–BILSTM combined quadratic decomposition model", Water Supply, Vol.23, No.9, pp.3597–3613 (2023)
- [33]: S. Wang et al.: "Ultra-Short-Term Power Prediction of a Photovoltaic Power Station Based on the VMD-CEEMDAN-LSTM Model", Frontiers in Energy Research, Vol.10 (2022)
- [34]: F. Zhou et al.: "Carbon price forecasting based on CEEMDAN and LSTM", Applied Energy, Vol.311, p 118601 (2022) (https://github.com/FateMurphy/CEEMDAN-VMD-GRU) 
- [35] Y. Zheng et al.: "Multi-Step Forecasting for Household Power Consumption", IEEJ Trans. Electrical and Electronic Engineering, Vol.18, No.8, pp.1255-1263 (2023)
- [36]: J. Xue and B. Shen: "Dung beetle optimizer: a new meta-heuristic algorithm for global optimization", the journal of Supercomputing, Vol.79, pp.7305–7336, (2023)
- [37]: N. Hansen et. al: "Impacts of Invariance in Search: When CMA-ES and PSO Face Ill-Conditioned and Non-Separable Problems", Journal of Applied Soft Computing, pp. 5755-5769 (2011)
- [38]: N. Hansen: "Benchmarking a BI-population CMA-ES on the BBOB-2009 function testbed", Workshop Proceedings of the GECCO Genetic and Evolutionary Computation Conference, pp. 2389–2396 (2009)
- [39]: R. Tanabe and A. Fukunaga: "Success-History Based Parameter Adaptation for Differential Evolution," Proceedings of the 2013 IEEE Congress on Evolutionary Computation, pp. 71-78 (2013)
- [40]: R. Tanabe and A. Fukunaga: “Improving the Search Performance of SHADE Using Linear Population Size Reduction,” Proceedings of the 2014 IEEE Congress on Evolutionary Computation, pp. 1658-1665 (2014)
- [41]: The Black-box Optimization Benchmarking (BBOB) Workshop, http://numbbo.github.io/workshops/index.html

