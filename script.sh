python csac.py setting.task_name=walk setting.dataset_name=medium # csac-walk-medium
python csac.py setting.task_name=walk setting.dataset_name=medium-replay # csac-walk-medium-replay
python csac.py setting.task_name=run setting.dataset_name=medium # csac-run-medium
python csac.py setting.task_name=run setting.dataset_name=medium-replay # csac-run-medium-replay

python mtcsac.py setting.dataset_name=medium # mtcsac-medium
python mtcsac.py setting.dataset_name=medium-replay # mtcsac-medium-replay

python hcsac.py setting.dataset_name=medium # hcsac-medium
python hcsac.py setting.dataset_name=medium-replay # hcsac-medium-replay
