protoc \
  -I ./protos \
  --include_imports \
  --descriptor_set_out=descriptors.pb \
  ./protos/common/rpc/*.proto

  protoc -Iprotos --jsonschema_out=schemas protos/*.proto


datamodel-codegen --input descriptor.pb --input-file-type proto