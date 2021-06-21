import sys
from typing import List


from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5 import QtChart as qtch
from PyQt5.QtChart import QChart, QLineSeries, QSplineSeries
from PyQt5.QtCore import QPointF, QRect, QRectF, QSizeF, Qt
from PyQt5.QtGui import QColor, QFont, QFontMetrics, QMouseEvent, QPainter, QPainterPath, QResizeEvent
from PyQt5.QtWidgets import QApplication, QGraphicsItem, QGraphicsScene, QGraphicsSceneMouseEvent, \
    QGraphicsSimpleTextItem, QGraphicsView, QStyleOptionGraphicsItem, QWidget


class Callout(QGraphicsItem):

    def __init__(self, parent: QChart):
        super().__init__()
        self.m_chart: QChart = parent
        self.m_text: str = ''
        self.m_anchor: QPointF = QPointF()
        self.m_font: QFont = QFont()
        self.m_textRect: QRectF = QRectF()
        self.m_rect: QRectF = QRectF()

    def setText(self, text: str):
        self.m_text = text
        metrics = QFontMetrics(self.m_font)
        self.m_textRect = QRectF(metrics.boundingRect(QRect(0, 0, 150, 150), Qt.AlignLeft, self.m_text))
        self.m_textRect.translate(5, 5)
        self.prepareGeometryChange()
        self.m_rect = QRectF(self.m_textRect.adjusted(-5, -5, 5, 5))
        self.updateGeometry()

    def updateGeometry(self):
        self.prepareGeometryChange()
        self.setPos(self.m_chart.mapToPosition(self.m_anchor) + QPointF(10, -50))

    def boundingRect(self) -> QRectF:
        from_parent = self.mapFromParent(self.m_chart.mapToPosition(self.m_anchor))
        anchor = QPointF(from_parent)
        rect = QRectF()
        rect.setLeft(min(self.m_rect.left(), anchor.x()))
        rect.setRight(max(self.m_rect.right(), anchor.x()))
        rect.setTop(min(self.m_rect.top(), anchor.y()))
        rect.setBottom(max(self.m_rect.bottom(), anchor.y()))
        return rect

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget):
        path = QPainterPath()
        mr = self.m_rect
        path.addRoundedRect(mr, 5, 5)

        anchor = QPointF(self.mapFromParent(self.m_chart.mapToPosition(self.m_anchor)))
        if not mr.contains(anchor):
            point1 = QPointF()
            point2 = QPointF()

            # establish the position of the anchor point in relation to self.m_rect
            above = anchor.y() <= mr.top()
            above_center = mr.top() < anchor.y() <= mr.center().y()
            below_center = mr.center().y() < anchor.y() <= mr.bottom()
            below = anchor.y() > mr.bottom()

            on_left = anchor.x() <= mr.left()
            left_of_center = mr.left() < anchor.x() <= mr.center().x()
            right_of_center = mr.center().x() < anchor.x() <= mr.right()
            on_right = anchor.x() > mr.right()

            # get the nearest self.m_rect corner.
            x = (on_right + right_of_center) * mr.width()
            y = (below + below_center) * mr.height()
            corner_case = (above and on_left) or (above and on_right) or (below and on_left) or (below and on_right)
            vertical = abs(anchor.x() - x) > abs(anchor.y() - y)
            horizontal = bool(not vertical)

            x1 = x + left_of_center * 10 - right_of_center * 20 + corner_case * horizontal * (
                    on_left * 10 - on_right * 20)
            y1 = y + above_center * 10 - below_center * 20 + corner_case * vertical * (above * 10 - below * 20)
            point1.setX(x1)
            point1.setY(y1)

            x2 = x + left_of_center * 20 - right_of_center * 10 + corner_case * horizontal * (
                    on_left * 20 - on_right * 10)
            y2 = y + above_center * 20 - below_center * 10 + corner_case * vertical * (above * 20 - below * 10)
            point2.setX(x2)
            point2.setY(y2)

            path.moveTo(point1)
            path.lineTo(anchor)
            path.lineTo(point2)
            path = path.simplified()

        painter.setPen(QColor(30, 30, 30))
        painter.setBrush(QColor(255, 255, 255))
        painter.drawPath(path)
        painter.drawText(self.m_textRect, self.m_text)

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent):
        event.setAccepted(True)

    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent):
        if event.buttons() & Qt.LeftButton:
            self.setPos(self.mapToParent(event.pos() - event.buttonDownPos(Qt.LeftButton)))
            event.setAccepted(True)
        else:
            event.setAccepted(False)


class View(QGraphicsView):

    max = 10

    def __init__(self, parent=None, name = '', log = False):
        super().__init__(parent)
        self.m_callouts: List[Callout] = []
        self.setDragMode(QGraphicsView.NoDrag)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.log = log
        # chart
        self.m_chart = QChart(parent)
        self.m_chart.setMinimumSize(640, 480)
        self.m_chart.setTitle(name)
        self.m_chart.legend().hide()
        self.series = QLineSeries()
        self.m_chart.addSeries(self.series)
        self.m_chart.createDefaultAxes()
        self.m_chart.setAcceptHoverEvents(True)
        self.m_chart.setTheme(qtch.QChart.ChartThemeDark)
        self.xdata = []
        self.ydata = []
        self.setRenderHint(QPainter.Antialiasing)

        self.setScene(QGraphicsScene())
        self.scene().addItem(self.m_chart)

        self.m_coordX = QGraphicsSimpleTextItem(self.m_chart)
        self.m_coordX.setPos(self.m_chart.size().width() / 2 - 50, self.m_chart.size().height() - 20)
        self.m_coordX.setText("X: ")
        self.m_coordY = QGraphicsSimpleTextItem(self.m_chart)
        self.m_coordY.setPos(self.m_chart.size().width() / 2 + 50, self.m_chart.size().height() - 20)
        self.m_coordY.setText("Y: ")

        x_axis = qtch.QValueAxis()
        x_axis.setRange(0, 10)

        if self.log:
            self.y_axis = qtch.QLogValueAxis()
            self.y_axis.setBase(10)
            self.y_axis.setRange(1,self.max)
        else:
            self.y_axis = qtch.QValueAxis()
            self.y_axis.setRange(0,self.max)

        self.m_chart.setAxisX(x_axis,self.series)
        self.m_chart.setAxisY(self.y_axis,self.series)

        self.m_tooltip = Callout(self.m_chart)
        self.scene().addItem(self.m_tooltip)
        self.m_tooltip.hide()
        self.series.hovered.connect(self.tooltip)


        self.setMouseTracking(True)

    def resizeEvent(self, event: QResizeEvent):
        if scene := self.scene():
            scene.setSceneRect(QRectF(QPointF(0, 0), QSizeF(event.size())))
            self.m_chart.resize(QSizeF(event.size()))
            self.m_coordX.setPos(self.m_chart.size().width() / 2 - 50, self.m_chart.size().height() - 20)
            self.m_coordY.setPos(self.m_chart.size().width() / 2 + 50, self.m_chart.size().height() - 20)

            for callout in self.m_callouts:
                callout.updateGeometry()

        super().resizeEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent):
        from_chart = self.m_chart.mapToValue(event.pos())
        self.m_coordX.setText(f"X: {from_chart.x():.3f}")
        self.m_coordY.setText(f"Y: {from_chart.y():.3f}")
        super().mouseMoveEvent(event)

    def tooltip(self, point: QPointF, state: bool):
        if not self.m_tooltip:
            self.m_tooltip = Callout(self.m_chart)

        if state:
            pos = zip(self.xdata, self.ydata)
            min = min(pos, key = lambda point: abs((point[0] - point.x())**2 + (point[1] - point.y())**2))
            i = self.xdata.index(minx)
            self.m_tooltip.setText(f"X: {self.xdata[i]} \nY: {self.ydata[i]} ")
            self.m_tooltip.m_anchor = QPointF(self.xdata[i],self.ydata[i])
            self.m_tooltip.setZValue(11)
            self.m_tooltip.updateGeometry()
            self.m_tooltip.show()
        else:
            self.m_tooltip.hide()

    def keep_callout(self):
        self.m_callouts.append(self.m_tooltip)
        self.m_tooltip = Callout(self.m_chart)
        self.scene().addItem(self.m_tooltip)

    def refresh_stats(self,xdata,ydata):

        self.xdata.append(xdata)
        self.ydata.append(ydata)
        #autoscaling
        if ydata > 0.9*self.max:
            self.max = 1.2*ydata

            if self.log:
                y_axis.setRange(1,self.max)
            else:
                y_axis.setRange(0,self.max)

            self.m_chart.setAxisY(y_axis,self.series)

        #to add data follow this procedure
        new_data = [
        qtc.QPointF(x,self.ydata[index])
        for index, x in enumerate(self.xdata)]
        self.series.replace(new_data)

    def set_xlim(self,min,max):
        x_axis = qtch.QValueAxis()
        x_axis.setRange(min, max)
        self.m_chart.setAxisX(x_axis,self.series)

    def cla(self):

        self.ydata = []
        self.xdata = []
        self.max = 10
        if self.log:
            self.y_axis.setRange(1,self.max)
        else:
            self.y_axis.setRange(0,self.max)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = View()
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())
