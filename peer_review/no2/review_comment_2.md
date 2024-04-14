Re-review D

I checked the revised manuscript and author's response to reviewer's comments.
Although some points have improved, this paper has still very difficult problem to be acceptable for publication and is not revised enough based on the comments.
From this reason, the final judgement is "D" (reject).
I think this paper needs to be radically rewritten after reconsidered deeply in terms of originality and usability.
Detailed reasons and comments are as follows: 


# [major reasons]
## major reason1 (General)
According to the reviewer’s comment, the authors added the following sentences to the manuscript about the originality and usability:
- In Section 1, "A significant contribution of this work is the development of a composite forecasting model that uniquely integrates a Dragonfly Bio-inspired Optimization(DBO) algorithm to optimize the hyperparameters of Long Short-Term Memory (LSTM) neural networks." and "Overall, this paper's originality lies in its unique combination of advanced denoising methods, application of bio-inspired optimization strategy to LSTM neural networks, and novel approach to data aggregation." as the originality.
- In Subsection 2.5, DBO is better than other optimizers as citing the DBO's original paper[29].

But, I judge this paper does not achieve the level of acceptance according to the following reasons:
- Reviewer B listed similar literatures; e.g., [37] proposes DBO-LSTM for short-term power load forcasting task, [38] proposes VMD-CEEMDAN-LSTM, and [39, 40] proposes CEEMDAN-VMD-GRU with K-means and Sample Entropy because the authors have to explain and compare the latest and similar combined existing methods. However, the authors ignore the Reviewer B’s point and did only the basic elements method (LSTM, CEEMDAN-VMD, and DBO) in the revised manuscript. There is no essential difference between this paper and [39, 40] because the forecasting framework is very similar to them. Therefore, I cannot understand the originality, creativity, and usability of this paper.
- Especially, the only difference between this paper and [39, 40] is to use the LSTM whose hyperparameter and architecture are tuned by DBO. However, it is general to use LSTM and neural network tuned by Black-box Optimization or Neural Architecture Search[41, 42, 43]. These techniques are very well known.
- The authors appear confused because the above sentence says "Dragonfly Bio-inspired Optimization (DBO) algorithm" while Section 2.5 explains "Dung-Beetle Optimizer algorithm". This is a fatal error and evidence that the authors are not serious about the originality of the proposed method. 
- Reviewer B major comment (4) and minor comment (3) pointed out (i) determining LSTM’s hyperparameters is formulated as black-box problem and there are many excellent black-box algorithm, e.g., CMA-ES and SHADE and (ii) DBO has a fixed self-hyperparameter (rolling cockroach ratio or small cockroach ratio) while CMA-ES and SHADE have the auto-tuning function for self-hyperparameters. Furthermore, although DBO’s original paper[29] shows DBO is superior to PSO, HHO, WOA, MVO, SCA, SSA, and GWO using CEC-BC-2017 test problems, the SHADE based algorithm (L-SHADE+BOC) has the 2nd rank among excellent black-box algorithms using the same problems[44]. DBO is a new algorithm but likely inferior to SHADE. Therefore, the authors select an optimization algorithm without a good understanding of the results of the DBO’s original paper[29] and it is not originality and creativity of this paper.


## major reason2 (General)
The revised manuscript's structure still has some problems although Reviewer B's major comment (3) pointed out the author should revise it so that the reader can understand the originality and creativity of this paper. 
Examples are shown bellow:
- There is an only Section 3.7, but no Sections 3.1-3.6 in Chapter 3 of the revised manuscript. 
- The subsection 4.5.1 of STFT's principle should be moved to Appendix because STFT is not proposed, but only compared in this paper.
- Table8 should be deleted from the manuscript because Table9 includes Table8.
- CEEMDAN-VMD-DBO-LSTM is written across two rows in Table 9 while its indicator value (RMSE=4.09 and 7.78) is written per row in right side. They do not correspond.


## major reason3 (Format)
You do not satisfy to follow the writing format of TEEE correctly according to Reviewer B’s major comment (7). 
Examples are shown bellow:
- Fig.1 is smaller than that in the first manuscript although Reviewer B poined out "The font and subfigures in Fig.1 should be larger for visiblity." and provided the TEEE guidelines.
- The blank space around tables and figures is too narrow, i.e., between figure and sentense, figure and it's caption, and tables although Reviewer B poined out "there should be plenty of space around tables and figures for visiblity."
- Table 2's format is different from the other tables.


## major reason4 (Section4)
The usability of the proposed method is slightly improved according to reviewer's comment. But, I cannot judge that it reaches the level of acceptance because it has not yet been verified enough although Reviewer B's major comment (6) and minor comment (5) pointed out it. 
Examples are shown bellow:
- In Subsection 4.5.2, I cannot understand if STFT is an appropriate comparison method because no several reasons and explanations. The authors should pay more attention to select the comparing method considering the originality of the proposed method and similar existing methods; e.g., CEEMDAN-VMD-GRU[38,39].
- Table7 and 9 compare the proposed method, DBO-, SSA-, MVO-, and PSO-LSTM. But, it should compare the proposed method,  CEEMDAN-VMD-SSA-LSTM, CEEMDAN-VMD-MVO-LSTM, and CEEMDAN-VMD-PSO-LSTM considering the effect of data pre-processing by CEEMDAN-VMD.
- I cannot understand the general versatility of the proposed method. Table10 shows the results for long-term forecast task using K-fold cross-validation about only the proposed method. Moreover, some results using cross-validation in Table10 is inferior to the other methods in Table9, e.g., RMSE=7.78 of the proposed method and RMSE=8.97 of DBO-LSTM (I guess). To verify the general versatility, all methods should use cross-validation fairy or several data from several periods (4 seasons) even short-term forecast task.


## major reason5 (General)
There are still many misstatements in the revised manuscript although Reviewer B’s minor comment1. I found the quality to be extremely low. Examples are shown bellow:
- In left side of Page4, "Additionaly, three engineering design problems were tackled with the proposed DBO algorithm to assess its effectiveness in practical applications.", but the paper does not propose the DBO algorithm.
- In right side of Page4, "Specifically, the boundary of the optimal feeding area can be defined by the following formula:In these formulas,…", but there are no formulas between their sentences.
- In right side of Page4, "other parameters remain consistent with those defined in the aforementioned formula (19-20).", but formulas (19-20) are not DBO’s, they are VMD’s.
- In left side of Page5, "other parameters are consistent with those defined in the aforementioned formula (21)-(22).", but formulas (21-22) are not other parameters, they are updating position x formulas.


## Additional References
- [37]: Y. Zhang et al.: "Short-Term Load Forecasting Based on DBO-LSTM Model," 3rd International Conference on Energy Engineering and Power Systems (2023)
- [38]: S. Wang et al.: "Ultra-Short-Term Power Prediction of a Photovoltaic Power Station Based on the VMD-CEEMDAN-LSTM Model", Frontiers in Energy Research, Vol.10 (2022)
- [39]: F. Zhou et al.: "Carbon price forecasting based on CEEMDAN and LSTM", Applied Energy, Vol.311, p 118601 (2022) (https://github.com/FateMurphy/CEEMDAN-VMD-GRU) 
- [40]: H. Li et al.: "A new secondary decomposition ensemble learning approach for carbon price forecasting", Knowledge-Based Systems, Vol.214, p.106686 (2021)
- [41]: J. Waring et al.: "Automated machine learning: Review of the state-of-the-art and opportunities for healthcare", Artificial Intelligence in Medicine, Vol. 104, page 101822 (2020)
- [42]: R. Luo et al.: "Neural Architecture Optimization", Advances in Neural Information Processing Systems, Vol. 31, pp. 1–12 (2018)
- [43]: P. Ren et al.: "A comprehensive survey of neural architecture search: Challenges and solutions", ACM Computing Surveys, Vol. 54, No. 4, Article No.76, pp. 1–34 (2021)
- [44]: https://github.com/P-N-Suganthan/CEC2017/blob/master/Comparison%20of%20Results%20in%202019%20on%20CEC%20Competition%20on%20Constrained%20RealParameter%20Optimization-2017.pdf
