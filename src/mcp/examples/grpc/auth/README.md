# Running the MCP Server with gRPC Transport and TLS

## Start the server

```
blaze run //third_party/py/mcp_grpc/examples/grpc/auth:server -- --alsologtostderr
```

## Run the client

```
blaze run //third_party/py/mcp_grpc/examples/grpc/auth:client -- --alsologtostderr
```
