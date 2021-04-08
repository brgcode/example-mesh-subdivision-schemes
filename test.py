from compas.datastructures import Mesh
from compas.geometry import Box
from compas.geometry import Translation

box = Box.from_diagonal([(0.0, 0.0, 0.0), (1.0, 1.0, 1.0)])
mesh = Mesh.from_shape(box)

tri = mesh.subdivide(k=3, scheme='tri')
quad = mesh.subdivide(k=3, scheme='quad')
corner = mesh.subdivide(k=3, scheme='corner')
ck = mesh.subdivide(k=3, scheme='catmullclark')
doosabin = mesh.subdivide(k=3, scheme='doosabin')

quad.transform(Translation.from_vector([1.2 * 1, 0.0, 0.0]))
corner.transform(Translation.from_vector([1.2 * 2, 0.0, 0.0]))
ck.transform(Translation.from_vector([1.2 * 3, 0.0, 0.0]))
doosabin.transform(Translation.from_vector([1.2 * 4, 0.0, 0.0]))
