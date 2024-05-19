<h1 align="center">
Multi-Task Offline Reinforcement Learning with Heuristic Conservative Soft Actor-Critic
</h1>
<p align="center">
    Project of AI3601 Reinforcement Learning
    <br />
    <a href="https://github.com/xxyQwQ"><strong>Xiangyuan Xue</strong></a>
    &nbsp;
    <a href="https://github.com/Loping151"><strong>Kailing Wang</strong></a>
    &nbsp;
    <a href="https://github.com/Bujiazi"><strong>Jiazi Bu</strong></a>
    &nbsp;
</p>
<p align="center">
    <a href="https://github.com/"> <img alt="Github Repository" src="https://img.shields.io/badge/Github-Repository-blue?logo=github&logoColor=blue"> </a>
    <a href="assets/slides.pdf"> <img alt="Presentation Slides" src="https://img.shields.io/badge/Presentation-Slides-green?logo=googlenews&logoColor=green"> </a>
    <a href='assets/report.pdf'> <img alt='Project Report' src='https://img.shields.io/badge/Project-Report-red?style=flat&logo=googlescholar&logoColor=red'> </a>
</p>

This project aims to ...

<!-- ![teasor](assets/teasor.png) -->

## 🛠️ Requirements

You can install them following the instructions below.

* Create a new conda environment and activate it:
  
    ```bash
    conda create -n hcsac python=3.10
    conda activate hcsac
    ```

* Install [pytorch](https://pytorch.org/get-started/previous-versions/) with appropriate CUDA version, e.g.
  
    ```bash
    pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113
    ```

* Then install other dependencies:
  
    ```bash
    pip install setuptools==65.5.0 gym==0.21.0 dm_control==1.0.15
    pip install tqdm hydra-core numpy matplotlib
    ```

Latest version is recommended for all the packages, but make sure that your CUDA version is compatible with your `pytorch`.

## 🚀 Experiments

First, you need to download the given offline dataset and extract it to the `dataset` folder. The dataset consists of offline samples from two tasks (i.e. `walker_run` and `walker_walk`), each including two data quality levels (i.e. `medium` and `medium-replay`). They are collected from the replay buffer when training an online TD3 agent. The `package` folder contains necessary environment specifications for the tasks.

...