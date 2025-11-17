# Running the MCP Server with gRPC Transport

## Start the Server

```
blaze run  //third_party/py/mcp_grpc/examples/grpc/internal:server \
  -- --port=50051 --alsologtostderr
```

If the server starts correctly, you should see the following logs:

```
I1027 08:01:26.326934   35743 grpc.py:289] gRPC reflection enabled
I1027 08:01:26.329439   35743 grpc.py:342] gRPC server started on 127.0.0.1:50051
```

## Run the Client

In a different terminal, run the following command:

```
blaze run  //third_party/py/mcp_grpc/examples/grpc/internal:server \
  -- --server_host=localhost --server_port=50051 --alsologtostderr
```
