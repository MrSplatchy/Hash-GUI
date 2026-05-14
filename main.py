import hashlib
import sys

from PyQt6.QtWidgets import QApplication, QFileDialog, QMainWindow, QPushButton


def get_hash(f_path):
    h = hashlib.sha256()
    B_SIZE = 65536
    with open(f_path, "rb") as file:
        data = file.read(B_SIZE)
    h.update(data)
    digest = h.hexdigest()
    return digest


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 150, 200, 150)
        self.setWindowTitle("Test")

        button = QPushButton("Open with", self)
        button.clicked.connect(self.dialog)
        button.resize(100, 32)
        button.move(50, 50)

        self.show()

    def dialog(self):
        file, check = QFileDialog.getOpenFileName(
            None,
            "QFileDialog.getOpenFileName()",
            "",
            self.tr("All Files (*);;Python Files (*.py);;Text Files (*.txt)"),
        )

        if check:
            print(get_hash(file))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWin()
    sys.exit(app.exec())
