
```shell
pip install grpcio grpcio-tools

# write proto file
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto

python server.py
python client.py

```
