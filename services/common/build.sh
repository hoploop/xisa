#python3 -m pip install grpcio-tools
echo "Building Python protos definitions"
python3 -m grpc_tools.protoc -I ./protos --python_out=./src/  --pyi_out=./src/ --grpc_python_out=./src/ ./protos/common/rpc/*.proto
echo "Python protos definitions built in common service"