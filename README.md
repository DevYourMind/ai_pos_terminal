Порядок запуска ноутбуков:

1. data_processing/anticlass_augmentations.ipynb - создание аугментированных картинок с "антиклассами" под задачи обнаружения терминала/чека
2. data_processing/markup_creation.ipynb - создание файла с разметкой для датасета
3. data_processing/duplicates_drop.ipynb - удаление дубликатов фотографий
4. data_processing/sorted_data_eda.ipynb - файл с EDA по размеченным данным

Папки с задачами:
1. terminal_receipt_classification - определение наличия терминала/чека на фото ---- DONE
2. terminal_quality_classification - определение наличия/отсутствия визуального дефекта терминала на фото ---- IN PROCESS