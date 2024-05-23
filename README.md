<h1 align="center">
Multi-Task Offline Reinforcement Learning with Heuristic Conservative Soft Actor-Critic
</h1>
<p align="center">
    Project of AI3601 Reinforcement Learning, 2024 Spring, SJTU
    <br />
    <a href="https://github.com/xxyQwQ"><strong>Xiangyuan Xue</strong></a>
    &nbsp;
    <a href="https://github.com/Loping151"><strong>Kailing Wang</strong></a>
    &nbsp;
    <a href="https://github.com/Bujiazi"><strong>Jiazi Bu</strong></a>
    &nbsp;
</p>
<p align="center">
    <a href="https://github.com/xxyQwQ/hcsac"> <img alt="Github Repository" src="https://img.shields.io/badge/Github-Repository-blue?logo=github&logoColor=blue"> </a>
    <a href="assets/slides.pdf"> <img alt="Presentation Slides" src="https://img.shields.io/badge/Presentation-Slides-green?logo=googlenews&logoColor=green"> </a>
    <a href='assets/report.pdf'> <img alt='Project Report' src='https://img.shields.io/badge/Project-Report-red?style=flat&logo=googlescholar&logoColor=red'> </a>
</p>

This project aims to explore the offline multi-task reinforcement learning paradigm. We propose a novel method named heuristic conservative soft actor-critic (HCSAC) based on conservative Q-learning (CQL) and soft actor-critic (SAC) to solve the offline multi-task reinforcement learning problem. We employ task embedding to allow the agent to learn shared representations across multiple tasks. We also follow conservative data sharing (CDS) to utilize heuristic relabeling to augment the offline dataset, so that the agent can benefit from the shared transitions while avoiding performance degradation.

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
    pip install tqdm hydra-core numpy pandas seaborn matplotlib 
    ```

Ensure that your CUDA version is compatible with your `pytorch`. Refer to this [link](https://stackoverflow.com/questions/76129688/why-is-pip-install-gym-failing-with-python-setup-py-egg-info-did-not-run-succ) if you encounter errors when installing `gym`.

## 🚀 Experiments

First, you need to download the given offline dataset and extract it to the `dataset` folder. The dataset consists of offline samples from two tasks (i.e. `walker_run` and `walker_walk`), each including two data quality levels (i.e. `medium` and `medium-replay`). They are collected from the replay buffer when training an online TD3 agent. The `package` folder contains necessary environment specifications for the tasks.

Then you can train the agents with default parameters by running the following commands:

```bash
python bc.py # behavioral cloning
python csac.py # conservative soft actor-critic
python mtcsac.py # multi-task conservative soft actor-critic
python hcsac.py # heuristic conservative soft actor-critic
```

You can specify the task and dataset by modifying the corresponding parameters. For example, to train the HCSAC agent on the `medium-replay` dataset with a batch size of `1024`, you can run the following command:

```bash
python hcsac.py setting.dataset_name=medium-replay strategy.batch_size=1024
```

You can refer to the `config` folder for more configurations and hyperparameters. We write all the experiment commands in the `script` folder. You can reproduce the results in the report by running the following command:

```bash
bash script/run.sh
```

The results and models will be saved in the `checkpoint` folder. You can visualize the training curves and compare the performance of different agents using the provided jupyter notebook `plot.ipynb` in the `script` folder.

## 🎬 Samples

Here are the training curves of the agents in the $4$ settings, including `walk-medium`, `walk-medium-replay`, `run-medium`, and `run-medium-replay`:

![walk-medium](assets/walk_medium.png)
![walk-medium-replay](assets/walk_medium_replay.png)
![run-medium](assets/run_medium.png)
![run-medium-replay](assets/run_medium_replay.png)

Here are the performance comparisons of the agents in terms of the average return in online evaluation:

| Task               | BC             | CSAC           | MTCSAC         | HCSAC          |
|:------------------:|:--------------:|:--------------:|:--------------:|:--------------:|
| walk-medium        | 113.96 ± 34.86 | 163.10 ± 21.00 | 170.22 ± 19.61 | 173.41 ± 11.72 |
| run-medium         | 54.71 ± 7.88   | 77.23 ± 7.11   | 72.46 ± 6.25   | 76.06 ± 5.61   |
| walk-medium-replay | 136.78 ± 20.96 | 131.73 ± 39.88 | 184.32 ± 20.23 | 158.17 ± 25.72 |
| run-medium-replay  | 54.91 ± 3.39   | 76.65 ± 4.36   | 66.62 ± 11.22  | 69.44 ± 9.14   |

See the project report for more experiment details and explanations.
