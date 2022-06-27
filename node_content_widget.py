# -*- coding: utf-8 -*-
"""A module containing the base class for the Node's content graphical representation. It also contains an example of
an overridden Text Widget, which can pass a notification to it's parent about being modified."""
from collections import OrderedDict
from turtle import color

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor, QPolygon, QPen, QBrush
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

from node_serializable import Serializable
from qtpy.QtWidgets import QWidget, QLabel, QVBoxLayout, QTextEdit, QHBoxLayout


class QDMNodeContentWidget(QWidget, Serializable):
    """Base class for representation of the Node's graphics content. This class also provides layout
    for other widgets inside of a :py:class:`~nodeeditor.node_node.Node`"""
    def __init__(self, node:'Node', parent:QWidget=None):
        """
        :param node: reference to the :py:class:`~nodeeditor.node_node.Node`
        :type node: :py:class:`~nodeeditor.node_node.Node`
        :param parent: parent widget
        :type parent: QWidget

        :Instance Attributes:
            - **node** - reference to the :class:`~nodeeditor.node_node.Node`
            - **layout** - ``QLayout`` container
        """
        self.node = node
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        """Sets up layouts and widgets to be rendered in :py:class:`~nodeeditor.node_graphics_node.QDMGraphicsNode` class.
        """
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)
        # self.wdg_label = QLabel("Inputs & Outputs:")
        self.wdg_label = QLabel(self.node.socketStrList)
        self.layout.addWidget(self.wdg_label)
        self.layout.addWidget(QDMShape(self.node))

        # self.layout.addWidget(QDMTextEdit("Inputs:\n" + self.node.socketStrList))


    def setEditingFlag(self, value:bool):
        """
        .. note::

            If you are handling keyPress events by default Qt Window's shortcuts and ``QActions``, you will not
             need to use this method.

        Helper function which sets editingFlag inside :py:class:`~nodeeditor.node_graphics_view.QDMGraphicsView` class.

        This is a helper function to handle keys inside nodes with ``QLineEdits`` or ``QTextEdits`` (you can
        use overridden :py:class:`QDMTextEdit` class) and with QGraphicsView class method ``keyPressEvent``.

        :param value: new value for editing flag
        """
        self.node.scene.getView().editingFlag = value

    def serialize(self) -> OrderedDict:
        return OrderedDict([
        ])

    def deserialize(self, data:dict, hashmap:dict={}, restore_id:bool=True) -> bool:
        return True



class QDMTextEdit(QTextEdit):
    """
        .. note::

            This class is an example of a ``QTextEdit`` modification that handles the `Delete` key event with an overridden
            Qt's ``keyPressEvent`` (when not using ``QActions`` in menu or toolbar)

        Overridden ``QTextEdit`` which sends a notification about being edited to its parent's container :py:class:`QDMNodeContentWidget`
    """
    def focusInEvent(self, event:'QFocusEvent'):
        """Example of an overridden focusInEvent to mark the start of editing

        :param event: Qt's focus event
        :type event: QFocusEvent
        """
        self.parentWidget().setEditingFlag(True)
        super().focusInEvent(event)

    def focusOutEvent(self, event:'QFocusEvent'):
        """Example of an overridden focusOutEvent to mark the end of editing

        :param event: Qt's focus event
        :type event: QFocusEvent
        """
        self.parentWidget().setEditingFlag(False)
        super().focusOutEvent(event)

class QDMShape(QWidget):
    def __init__(self, node:'Node'):
        super().__init__()
        self.node=node
        self.initUI()

    def initUI(self):
        # self.setGeometry(300, 300, 350, 100)
        # self.setWindowTitle('Colours')
        self.show()

    def paintEvent(self, e):
        print("im in paint event")
        print()
        qp = QPainter()
        qp.begin(self)
        self.drawShape(qp)
        qp.end()

    def drawShape(self, qp):
        qp.setPen(QPen(QColor(self.palette().color(QtGui.QPalette.Background))))
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        # qp.setPen(col)

        # if (self.node.gate.getGateType().lower()=='not'):
        #     qp.setBrush(QColor(200, 0, 0))
        xStart=25
        xEnd=65
        xMid=47
        yStart=0
        yEnd=40
        yMid=20
        if (self.node.gate.getGateType().lower()=='input'):
            qp.setBrush(QColor(255, 80, 0, 160))
            qp.drawEllipse(QPoint(xMid, yMid), 20, 20);
        elif (self.node.gate.getGateType().lower()=='not'):
            qp.setBrush(QColor(200, 0, 0))
            ptList=[QPoint(xStart,yStart),QPoint(xStart,yEnd),QPoint(xEnd,yMid),QPoint(xStart,yStart)]
            qp.drawPolygon(QPolygon(ptList))
            qp.drawEllipse(QPoint(xEnd+8,yMid),10,10)
        elif (self.node.gate.getGateType().lower() == 'and'):
            qp.setBrush(QBrush(Qt.green))
            qp.setPen(QPen(Qt.green))
            qp.drawEllipse(QPoint(45, 20), 18, 20)
            qp.drawRect(xStart-4, yStart, 25, 40)
        elif (self.node.gate.getGateType().lower() == 'or'):
            qp.setBrush(QBrush(Qt.darkYellow))
            qp.setPen(QPen(Qt.darkYellow))
            qp.drawEllipse(QPoint(45, 20), 18, 20)
            qp.drawRect(xStart - 4, yStart, 25, 40)
            qp.setBrush(QBrush(QColor(self.palette().color(QtGui.QPalette.Background))))
            qp.setPen(QPen(QColor(self.palette().color(QtGui.QPalette.Background))))
            qp.drawEllipse(QPoint(xStart-20, 20),30,20)
        else:
            qp.setBrush(QColor(200, 0, 0))
            qp.drawRect(xStart, yStart, 40, 40)
        # qp.drawRect(10, 15, 90, 60)


        qp.setBrush(QColor(255, 80, 0, 160))
        qp.drawRect(130, 15, 90, 60)

        qp.setBrush(QColor(25, 0, 90, 200))
        qp.drawRect(250, 15, 90, 60)