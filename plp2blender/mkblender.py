"""@@@TODO: ."""

import enum
import math
import pdb
import pickle
import tempfile
from pathlib import Path

import bpy
from mathutils import Vector

from .plpath_parsing import PLPath


def blend(
    path: PLPath,
    handleType: str = 'NURBS',
    force: int = 8,
    bevelMode: str = 'ROUND',
    bevelDepth: float = 0.09,
    bevelRes: float = 4,
) -> None:
    """@@@TODO: ."""
    _clearBlend()

    for i, seg in enumerate(path.segements):
        curveData = bpy.data.curves.new(f'Segment {i}', type='CURVE')
        curveData.dimensions = '3D'
        curveData.resolution_u = 4
        curveData.bevel_mode = bevelMode
        curveData.bevel_depth = bevelDepth
        curveData.bevel_resolution = bevelRes
        curveData.use_fill_caps = True
        polyline = curveData.splines.new(handleType)

        if seg[-1] == seg[0]:
            seg.pop(-1)
            polyline.use_cyclic_u = True
        else:
            polyline.use_endpoint_u = True

        polyline.points.add(len(seg) - 1)
        polyline.order_u = force
        for j, pnt in enumerate(seg):
            polyline.points[j].co = (pnt.x, pnt.y, pnt.z, 19)

        curveOB = bpy.data.objects.new(f'Segment {i}', curveData)
        bpy.context.scene.collection.objects.link(curveOB)


def _clearBlend():
    """@@@TODO: ."""
    # print all objects
    for obj in bpy.data.objects:
        obj = bpy.data.objects.get('Cube')

        if obj:
            bpy.data.objects.remove(obj, do_unlink=True)

    for cur in bpy.data.curves:
        bpy.data.curves.remove(cur)


def blendBlob():
    """@@@TODO: ."""
    data = []
    with tempfile.NamedTemporaryFile(delete_on_close=False) as f:
        bpy.ops.wm.save_as_mainfile(filepath=f.name)
        with open(f.name, mode='rb') as fr:
            data = fr.read()
    return data


def saveBlendFile(fileName: Path):
    """@@@TODO: ."""
    bpy.ops.wm.save_as_mainfile(filepath=str(fileName))
