datamodel-codegen \
  --input ./protos/common/rpc/*.proto \
  --input-file-type proto \
  --output src/models/user_base.py \
  --class-name UserModel \
  --base-class pydantic.BaseModel