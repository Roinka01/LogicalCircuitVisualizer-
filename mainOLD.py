import os, sys, inspect
from qtpy.QtWidgets import QApplication
from node_file_parsing import filePrsing

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "", ".."))

from utils import loadStylesheet
from node_editor_window import NodeEditorWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = NodeEditorWindow()
    wnd.nodeeditor.addNodes()
    module_path = os.path.dirname( inspect.getfile(wnd.__class__) )
    loadStylesheet( os.path.join( module_path, 'qss/nodestyle.qss') )
    sys.exit(app.exec_())
