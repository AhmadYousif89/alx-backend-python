import os
import importlib.util


def import_module(relative_path):
    # Get the current directory of the script being run.
    current_directory = os.path.dirname(os.path.realpath(__file__))
    # Get the full, absolute file paths for the module.
    module_file_path = os.path.join(current_directory, relative_path + '.py')
    # Derive the module name from the file name.
    module_name = os.path.splitext(os.path.basename(module_file_path))[0]
    # Use the util functions to import the module.
    spec = importlib.util.spec_from_file_location(
        module_name, module_file_path
    )
    if spec is not None:
        module = importlib.util.module_from_spec(spec)
        if spec.loader is not None:
            spec.loader.exec_module(module)
            return module
        else:
            raise ImportError("Error: Module loader is None")
    else:
        raise ImportError("Error: Unable to create module specification")
