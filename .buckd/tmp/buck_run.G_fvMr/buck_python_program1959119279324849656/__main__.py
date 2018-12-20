from __future__ import absolute_import, print_function
import sys
PY2 = sys.version_info[0] == 2
sys.path.insert(0, "/home/emendoza/CppProjects/Buck/buckaroo-deps/Box2D/.buckd/resources/HEAD-fdbf043")
sys.path.insert(0, "/home/emendoza/CppProjects/Buck/buckaroo-deps/Box2D/.buckd/resources/HEAD-fdbf043/path_to_pywatchman")
if PY2:
    sys.path.insert(0, "/home/emendoza/CppProjects/Buck/buckaroo-deps/Box2D/.buckd/resources/HEAD-fdbf043/path_to_typing")
sys.path.insert(0, "/home/emendoza/CppProjects/Buck/buckaroo-deps/Box2D/.buckd/resources/HEAD-fdbf043")
sys.path.insert(0, "/home/emendoza/CppProjects/Buck/buckaroo-deps/Box2D/.buckd/resources/HEAD-fdbf043/buck_server")
sys.path.insert(0, "/home/emendoza/CppProjects/Buck/buckaroo-deps/Box2D/.buckd/tmp/buck_run.G_fvMr/buck_python_program1959119279324849656")
if __name__ == '__main__':
    try:
        from buck_parser import buck
        buck.main()
    except KeyboardInterrupt:
        print('Killed by User', file=sys.stderr)
