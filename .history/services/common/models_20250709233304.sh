datamodel-codegen \
  --input protos/*.proto \
  --input-file-type proto \
  --output models/all_models.py \
  --base-class your_project.db.BaseBeanieModel