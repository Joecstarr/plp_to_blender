"""@@@TODO: ."""

import math
import pdb

import bpy
from mathutils import Vector

from .plpath_parsing import PLPath


def blend(path: PLPath):
    """@@@TODO: ."""
    for i, segment in enumerate(path.segements):
        curveData = bpy.data.curves.new(f'myCurve {i}', type='CURVE')
        curveData.dimensions = '3D'
        curveData.resolution_u = 2
        polyline = curveData.splines.new('POLY')
        polyline.points.add(len(segment))
        for point in segment:
            polyline.points[i].co = (point.x, point.y, point.z, 1)

        # create Object
        curveOB = bpy.data.objects.new('myCurve', curveData)
        curveData.bevel_depth = 0.01

        # attach to scene and validate context
        scn = bpy.context.scene
        scn.objects.link(curveOB)
        scn.objects.active = curveOB
