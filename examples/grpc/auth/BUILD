load("//third_party/bazel_rules/rules_python/python:py_binary.bzl", "py_binary")
load("//third_party/bazel_rules/rules_python/python:py_library.bzl", "py_library")

package(
    default_applicable_licenses = ["//third_party/py/mcp_grpc:license"],
    default_visibility = ["//third_party/py/mcp_grpc:mcp_users"],
)

py_library(
    name = "_credentials",
    srcs = ["_credentials.py"],
    data = [
        "localhost.crt",
        "localhost.key",
        "root.crt",
    ],
    deps = [
        "//pyglib:resources",
    ],
)

py_binary(
    name = "server",
    srcs = ["server.py"],
    data = [
        "localhost.crt",
        "localhost.key",
        "root.crt",
    ],
    main = "server.py",
    deps = [
        ":_credentials",
        "//third_party/py/absl:app",
        "//third_party/py/absl/flags",
        "//third_party/py/absl/logging",
        "//third_party/py/mcp_grpc",
    ],
)

py_binary(
    name = "client",
    srcs = ["client.py"],
    data = [
        "root.crt",
    ],
    main = "client.py",
    deps = [
        ":_credentials",
        "//third_party/py/absl:app",
        "//third_party/py/absl/flags",
        "//third_party/py/mcp_grpc",
    ],
)
