import sys
import time

from PySide6.QtCore import QObject, Signal, QThread
from PySide6.QtWidgets import QApplication, QWidget
from ui_workerui import Ui_myWidget


class Worker1(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def doWork(self):
        value = '0'
        self.started.emit(value)
        time.sleep(1)

        for i in range(5):
            value = str(i+1)
            self.progressed.emit(value)
            time.sleep(1)

        value = str(int(value)+1)
        self.finished.emit(value)


class MyWidge(QWidget, Ui_myWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.button1.clicked.connect(self.hardWork1)
        self.button2.clicked.connect(self.hardWork2)

    def hardWork1(self):
        self._worker = Worker1()
        self._thread = QThread()

        # Daria para substituir tudo pelo acima,
        # assim não precisaria do abaixo
        worker = self._worker
        thread = self._thread

        # Mover o worker para a thread
        worker.moveToThread(thread)

        # Conectar no doWork
        thread.started.connect(worker.doWork)
        worker.finished.connect(thread.quit)

        # Garante que elimina da memória
        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)

        # Depois de tudo isso acima pode-se utilizar
        worker.started.connect(self.worker1Started)
        worker.progressed.connect(self.worker1Progressed)
        worker.finished.connect(self.worker1Finished)

        thread.start()

    def worker1Started(self, value):
        self.button1.setDisabled(True)
        self.label1.setText(value)
        print('worker iniciado')

    def worker1Progressed(self, value):
        self.label1.setText(value)
        print('em progresso')

    def worker1Finished(self, value):
        self.button1.setDisabled(False)
        self.label1.setText(value)
        print('worker finalizado')

    def hardWork2(self):
        self._worker2 = Worker1()
        self._thread2 = QThread()

        # Daria para substituir tudo pelo acima,
        # assim não precisaria do abaixo
        worker = self._worker2
        thread = self._thread2

        # Mover o worker para a thread
        worker.moveToThread(thread)

        # Conectar no doWork
        thread.started.connect(worker.doWork)
        worker.finished.connect(thread.quit)

        # Garante que elimina da memória
        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)

        # Depois de tudo isso acima pode-se utilizar
        worker.started.connect(self.worker2Started)
        worker.progressed.connect(self.worker2Progressed)
        worker.finished.connect(self.worker2Finished)

        thread.start()

    def worker2Started(self, value):
        self.button2.setDisabled(True)
        self.label2.setText(value)
        print('worker 2 iniciado')

    def worker2Progressed(self, value):
        self.label2.setText(value)
        print('2 em progresso')

    def worker2Finished(self, value):
        self.button2.setDisabled(False)
        self.label2.setText(value)
        print('worker 2 finalizado')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidge = MyWidge()
    myWidge.show()
    app.exec()
