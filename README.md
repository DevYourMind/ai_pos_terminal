Порядок запуска ноутбуков:

1. data_processing/damaged_terminals_augmentations.ipynb - создание аугментированных картинок с поврежденными терминалами
2. data_processing/anticlass_augmentations.ipynb - создание аугментированных картинок с "антиклассами" под задачи обнаружения терминала/чека
3. data_processing/isnt_visible_augmentations.ipynb - создание аугментированных картинок с
4. data_processing/markup_creation.ipynb - создание файла с разметкой для датасета
5. data_processing/duplicates_drop.ipynb - удаление дубликатов фотографий
6. data_processing/sorted_data_eda.ipynb - файл с EDA по размеченным данным

Папки с задачами:

1. [X] terminal_receipt_classification - определение наличия терминала/чека на фото
    ---- DONE ----
2. [ ] terminal_quality_classification - определение наличия/отсутствия визуального дефекта терминала на фото
    ---- IN PROCESS ----
3. [ ] damage_isnot_visible_classification - определение качества фотографии терминала (возможность судить об отсутствии дефекта)
    ---- IN PROCESS ----
4. [ ] prediction_pipeline - pipeline обработки фотографий из СБС и формирования прогнозов
    ---- IN PROCESS----
