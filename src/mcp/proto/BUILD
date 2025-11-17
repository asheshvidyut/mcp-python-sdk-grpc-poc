load("//net/grpc:cc_grpc_library.bzl", "cc_grpc_library")
load("//net/grpc/python:py_grpc_library.bzl", "py_grpc_library")
load("//third_party/bazel_rules/rules_python/python:proto.bzl", "py_proto_library")
load("//third_party/protobuf/bazel:cc_proto_library.bzl", "cc_proto_library")
load("//third_party/protobuf/bazel:proto_library.bzl", "proto_library")

package(
    default_applicable_licenses = ["//third_party/py/mcp:license"],
    default_visibility = [
        "//third_party/mcp_cpp:__subpackages__",
        "//third_party/py/mcp:__subpackages__",
    ],
)

proto_library(
    name = "mcp_proto",
    srcs = ["mcp.proto"],
    has_services = 1,
    deps = [
        "//google/protobuf:duration",
        "//google/protobuf:struct",
    ],
)

py_proto_library(
    name = "mcp_py_pb2",
    has_services = 1,
    deps = [":mcp_proto"],
)

py_grpc_library(
    name = "mcp_py_pb2_grpc",
    srcs = [":mcp_proto"],
    deps = [":mcp_py_pb2"],
)

cc_proto_library(
    name = "mcp_cc_proto",
    deps = [":mcp_proto"],
)

cc_grpc_library(
    name = "mcp_cc_grpc",
    srcs = [":mcp_proto"],
    generate_mocks = True,
    deps = [":mcp_cc_proto"],
)
