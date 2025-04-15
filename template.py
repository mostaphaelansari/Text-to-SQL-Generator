import pathlib

folders = [
    'text_to_sql_generator/data',
    'text_to_sql_generator/data/raw',
    'text_to_sql_generator/data/processed',
    'text_to_sql_generator/data/databases',
    'text_to_sql_generator/models',
    'text_to_sql_generator/models/checkpoints',
    'text_to_sql_generator/models/config',
    'text_to_sql_generator/src',
    'text_to_sql_generator/src/data',
    'text_to_sql_generator/src/models',
    'text_to_sql_generator/evaluation',
    'text_to_sql_generator/utils',
    'text_to_sql_generator/notebooks',
    'text_to_sql_generator/app',
    'text_to_sql_generator/scripts',
    'dataset'
]

for folder in folders:
    pathlib.Path(folder).mkdir(parents=True, exist_ok=True)
    
files = [
    'text_to_sql_generator/src/data/preprocess.py',
    'text_to_sql_generator/src/data/dataloader.py',
    'text_to_sql_generator/src/data/augmentation.py',
    'text_to_sql_generator/src/models/models.py',
    'text_to_sql_generator/src/models/decoder.py',
    'text_to_sql_generator/src/models/training.py',
    'text_to_sql_generator/evaluation/metrics.py',
    'text_to_sql_generator/evaluation/sql_excutor.py',
    'text_to_sql_generator/evaluation/evaluator.py',
    'text_to_sql_generator/utils/sql_formatter.py',
    'text_to_sql_generator/utils/logging.py',
    'text_to_sql_generator/utils/visualization.py',
    'text_to_sql_generator/notebooks/data_exploration.ipynb',
    'text_to_sql_generator/notebooks/model_training.ipynb',
    'text_to_sql_generator/notebooks/result_analysis.ipynb',
    'text_to_sql_generator/app/app.py',
    'text_to_sql_generator/scripts/download_data.sh',
    'dataset/train.py',
    'dataset/evaluate.py',
    'requirements.txt',
    'config.yaml',
    'docker-compose.yaml',
    'README.md'
]

for file in files:
    pathlib.Path(file).touch()

print("Project structure created successfully!")
