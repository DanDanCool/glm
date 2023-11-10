import jmake

jmake.setupenv()

workspace = jmake.Workspace("glm")
glm = jmake.Project("glm", jmake.Target.HEADER_LIBRARY)
files = jmake.glob('glm', ['**/*.hpp', '**/*.h', '**/*.inl'])
glm.add(jmake.fullpath(files))

glm.export(includes=jmake.fullpath('.'))
workspace.add(glm)
