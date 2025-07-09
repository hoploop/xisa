protoc \
  -I ./protos \
  --include_imports \
  --descriptor_set_out=descriptors.pb \
  ./protos/common/rpc/*.proto

protoc -Iprotos -I ./protos/common/rpc --jsonschema_out=schemas ./protos/common/rpc/*.proto


datamodel-codegen --input descriptor.pb --input-file-type proto