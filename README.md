# Repository to preprint: Inference Scaling 𝙵Laws: The Limits of LLM Resampling with Imperfect Verifiers

This repository contains the accompanying code to the preprint with the title **[Inference Scaling 𝙵Laws: The Limits of LLM Resampling with Imperfect Verifiers](https://arxiv.org/abs/2411.17501)**.

The experiments run for this work build on the following publications and their accompanying code repositories.

**EvalPlus ---**
[Is Your Code Generated by ChatGPT Really Correct? Rigorous Evaluation of Large Language Models for Code Generation](https://proceedings.neurips.cc/paper_files/paper/2023/hash/43e9d647ccd3e4b7b5baab53f0368686-Abstract-Conference.html) ([GitHub](https://github.com/evalplus/evalplus)) ([license](https://github.com/evalplus/evalplus/edit/master/LICENSE))

**RACE ---**
[Beyond Correctness: Benchmarking Multi-dimensional Code Generation for Large Language Models](https://arxiv.org/abs/2407.11470) ([GitHub](https://github.com/jszheng21/RACE)) ([license](https://github.com/jszheng21/RACE?tab=Apache-2.0-1-ov-file))

## General notes

### Contents

- Section 3: The sanitized code samples for HumanEval+ and MBPP+ can be found [here](https://www.dropbox.com/scl/fi/je3d9lrmu36g5x3alugsa/humaneval_evalplus.zip?rlkey=del4cd36kfyyseaw7r9zs8gn0&st=6ixn93qb&dl=0) and [here](https://www.dropbox.com/scl/fi/ks8ml79rapst8ebgce6wz/mbpp_evalplus.zip?rlkey=tm1uk56l7onv1wsyb2a9x9ist&st=szk5toba&dl=0). Simply unzip the directories into `evalplus/`.  Code for running the analysis and plotting figures is in `evalplus/visualizations.ipynb`.
- Section 4: Inference scaling curves are in `evalplus/scaling_curves.ipynb`
- Section 5: Parsed code samples for our experiments on code quality can be found [here](https://www.dropbox.com/scl/fi/wwevjlo1u30jxt5bdyra7/humaneval_race.zip?rlkey=4j3hmhwuq87ndfnh4apxeil9n&st=l23miy3q&dl=0). Unzip the directory into `race/`. Analysis and visualizations are in `race/visualizations.ipynb`

### Sample collection

To collect existing samples from the EvalPlus repository and generate new samples for additional models, we used their implementation provided [here](https://github.com/evalplus/evalplus/tree/937c46858cf8e687b31b5a728b7083d6e5a84971). For generating samples for our code quality experiments, we used the original implementation of the RACE benchmark provided [here](https://github.com/jszheng21/RACE/tree/3b8ee591abd5febd8ae8ec17c7b9907949c5e1d5).

## Additional questions and details

You can refer to the paper and its associated appendices for more details on our setup. You can contact us at stroebl@princeton.edu
