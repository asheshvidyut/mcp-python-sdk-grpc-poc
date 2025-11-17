load("//third_party/bazel_rules/rules_python/python:py_binary.bzl", "py_binary")

package(
    default_applicable_licenses = ["//third_party/py/mcp_grpc:license"],
    # go/thirdparty/documentation#visibility
    default_visibility = ["//third_party/py/mcp_grpc:mcp_users"],
)

py_binary(
    name = "server",
    srcs = ["server.py"],
    deps = [
        "//third_party/py/absl:app",
        "//third_party/py/mcp_grpc",
    ],
)

py_binary(
    name = "client",
    srcs = ["client.py"],
    deps = [
        "//third_party/py/absl:app",
        "//third_party/py/mcp_grpc",
    ],
)
