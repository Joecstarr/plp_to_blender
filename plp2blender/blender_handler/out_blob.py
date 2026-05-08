"""Output blender file data to a blob."""

import tempfile

import bpy


def blendBlob():
    """Output blender file data to a blob.

    Write the blender data to a temporary file. The read that file into a byte array.
    """
    with tempfile.NamedTemporaryFile(delete_on_close=False) as f:
        bpy.ops.wm.save_as_mainfile(filepath=f.name)
        with open(f.name, mode='rb') as fr:
            data = fr.read()
        return data
