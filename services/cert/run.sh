#!/bin/bash
echo "Generating server and client certificates for grpc services"
mkdir -p shared
cd shared
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout server.key -out server.crt
cat server.crt server.key > server.pem
openssl x509 -inform PEM -in server.crt > public.pem
openssl genrsa  -out client.key 4096
openssl req -new -key client.key -out client.csr
openssl x509 -req -days 365 -in client.csr -CA server.crt -CAkey server.key -set_serial 01 -out client.crt
openssl pkcs12 -export -clcerts -in client.crt -inkey client.key -out client.p12
openssl x509 -outform der -in client.crt -out ios_client.cer
openssl x509 -outform der -in server.crt -out ios_server.cer
echo "Server and client certificates for grpc services generated and available at cert/shared folder"