"""Output blender data to a file."""

from pathlib import Path

import bpy


def saveBlendFile(fileName: Path):
    """Output blender data to a file."""
    bpy.ops.wm.save_as_mainfile(filepath=str(fileName), check_existing=False)
