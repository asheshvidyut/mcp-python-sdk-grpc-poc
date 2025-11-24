import os
from hatchling.builders.hooks.plugin.interface import BuildHookInterface

class CustomBuildHook(BuildHookInterface):
    def initialize(self, version, build_data):
        print("Patching gRPC generated files...")
        proto_dir = os.path.join(self.root, "src", "mcp", "proto")
        grpc_file = os.path.join(proto_dir, "mcp_pb2_grpc.py")

        if os.path.exists(grpc_file):
            print(f"Patching {grpc_file}")
            with open(grpc_file, "r") as f:
                content = f.read()

            original_import = "import mcp_pb2 as mcp__pb2"
            patched_import = "from . import mcp_pb2 as mcp__pb2"

            if original_import in content:
                content = content.replace(original_import, patched_import)
                with open(grpc_file, "w") as f:
                    f.write(content)
                print(f"Successfully patched {grpc_file}")
            else:
                print(f"Import statement not found in {grpc_file}, skipping patch.")
        else:
            print(f"WARNING: {grpc_file} not found, cannot patch.")

    def finalize(self, version, build_data, artifact_path):
        pass
