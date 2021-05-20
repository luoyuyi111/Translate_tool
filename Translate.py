import json
from tkinter import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI_Designer.translate import Ui_MainWindow
from PyQt5.QtGui import QIcon


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setWindowIcon(QIcon('translateIcon.ico'))
        self.master = 0
        self.setupUi(self)

    def translateText(self):
        string_text = self.translate_in.toPlainText()
        if string_text != '':
            json_text = json.loads(string_text)
            string_pack = json_text['pack']
            print(string_pack)
            json_pack = json.loads(string_pack)

            target_pack_mac = json_pack['mac']
            print(target_pack_mac)

            target_pack_cols = json_pack['cols']
            target_pack_dat = json_pack['dat']
            print(len(target_pack_cols))
            result = []
            for i in range(len(target_pack_cols)):
                res = str(i+1)+ '.'+ target_pack_cols[i] + ':' + str(target_pack_dat[i])
                result.append(res)
            self.translate_out.setPlainText('\n\n'.join(result))

    def copy_text(self):
        clipboard = QApplication.clipboard()  # 剪切板
        clipboard.setText(self.translate_out.toPlainText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = App()
    MainWindow.show()
    sys.exit(app.exec())