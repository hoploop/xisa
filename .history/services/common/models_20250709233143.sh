protoc \
  -I ./protos \
  --include_imports \
  --descriptor_set_out=descriptors.pb \
  ./protos/common/rpc/*.proto
protoc \
  -I ./protos \
  --jsonschema_out=schemas \
  ./protos/common/rpc/*.proto