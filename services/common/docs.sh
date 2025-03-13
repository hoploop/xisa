#go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latestgo install google.golang.org/protobuf/cmd/protoc-gen-go@latest
export GO_PATH=~/go
export PATH=$PATH:/$GO_PATH/bin
mkdir -p doc
cd protos
protoc --doc_out=../doc --doc_opt=html,index.html common/rpc/*.proto