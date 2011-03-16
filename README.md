Topological sort in Python.

Usage:

    from toposort import toposorted
    for vertex in toposorted(vertices, lambda v: v.parents()):
        do_stuff(vertex)
