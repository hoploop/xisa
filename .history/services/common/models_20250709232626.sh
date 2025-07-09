

  for proto in ./protos/cmmon/rpc/*.proto; do
  name=$(basename "$proto" .proto)
  datamodel-codegen \
    --input "$proto" \
    --input-file-type proto \
    --output "src/models/${name}_models.py"
    