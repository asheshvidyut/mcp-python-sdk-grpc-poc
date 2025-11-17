# Running the MCP Tool Cancellation Example with gRPC Transport

## Start The Server

```
blaze run  //third_party/py/mcp_grpc/examples/grpc/tool_cancellation:server \
  -- --port=50051 --alsologtostderr
```

If the server starts correctly, you should see logs similar to:
```
I1027 08:01:26.329439   35743 grpc.py:342] gRPC server started on 127.0.0.1:50051
```

## Run The Client

In a different terminal, run the following command:

```
blaze run  //third_party/py/mcp_grpc/examples/grpc/tool_cancellation:client \
  -- --server_host=localhost --server_port=50051 --alsologtostderr
```
