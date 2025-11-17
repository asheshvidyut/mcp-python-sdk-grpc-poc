load("//third_party/bazel_rules/rules_python/python:py_binary.bzl", "py_binary")

package(
    default_applicable_licenses = ["//third_party/py/mcp_grpc:license"],
    default_visibility = ["//third_party/py/mcp_grpc:mcp_users"],
)

py_binary(
    name = "server",
    srcs = ["server.py"],
    deps = [
        "//third_party/py/absl:app",
        "//third_party/py/absl/flags",
        "//third_party/py/absl/logging",
        "//third_party/py/mcp_grpc",
        "//third_party/py/pydantic:pydantic_v2",
    ],
)

py_binary(
    name = "client",
    srcs = ["client.py"],
    deps = [
        "//third_party/py/absl:app",
        "//third_party/py/absl/flags",
        "//third_party/py/absl/logging",
        "//third_party/py/mcp_grpc",
    ],
)
