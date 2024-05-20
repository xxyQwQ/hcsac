#!/bin/bash

agents=("rsp" "csac" "mtcsac" "hcsac")
agents=("rsp")
tasks=("walk" "run")
datasets=("medium" "medium-replay")
seeds=(0 1 2 3 4)

for agent in ${agents[*]}; do
    if [ $agent == "rsp" ] || [ $agent == "csac" ]; then
        for task in ${tasks[*]}; do
            for dataset in ${datasets[*]}; do
                for seed in {0..4}; do
                    python $agent.py seed=$seed setting.task_name=$task setting.dataset_name=$dataset
                done
            done
        done
    else
        for dataset in ${datasets[*]}; do
            for seed in {0..4}; do
                python $agent.py seed=$seed setting.dataset_name=$dataset
            done
        done
    fi
done