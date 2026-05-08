"""Plot a PL path into a blender instance."""

import bpy

from ..path_parsing.plpath import PLPath


def _clearBlend():
    """Clear default data (cube) from blender data."""
    if obj := bpy.data.objects.get('Cube'):
        bpy.data.objects.remove(obj, do_unlink=True)

    for cur in bpy.data.curves:
        bpy.data.curves.remove(cur)


def blend(
    path: PLPath,
    handleType: str = 'NURBS',
    force: int = 8,
    bevelMode: str = 'ROUND',
    bevelDepth: float = 0.09,
    bevelRes: float = 32,
) -> None:
    """Plot a PL path as a NURBS path into a blender scene.

    Args:
        path: The PL path to plot
        handleType: The type of curve to plot ([NURBS](https://en.wikipedia.org/wiki/Non-uniform_rational_B-spline), Bezier, etc.).
        force: The weight for each control point.
        bevelMode: Bevel type for the "tube" surrounding the curve.
        bevelDepth: The distance from the bevel face ([blender docs](https://docs.blender.org/manual/en/latest/modeling/modifiers/generate/bevel.html)).
        bevelRes: The "roundness" of the "tube" surrounding the curve.
    """
    _clearBlend()

    scene = bpy.context.scene
    for i, seg in enumerate(path.segments):
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
        if scene:
            scene.collection.objects.link(curveOB)
