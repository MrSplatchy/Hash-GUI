import hashlib
import sys

from PyQt6.QtWidgets import (
    QApplication,
    QFileDialog,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


def get_hash(f_path):
    h = hashlib.sha256()
    B_SIZE = 65536
    with open(f_path, "rb") as file:
        while data := file.read(B_SIZE):
            h.update(data)
    return h.hexdigest()


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 200)
        self.setWindowTitle("Hash-GUI")

        central = QWidget(self)
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(12)

        file_row = QHBoxLayout()
        file_row.setSpacing(8)

        # Actual widgets
        uploadButton = QPushButton("Open file", self)
        self.fileName = QTextEdit(self)
        self.fileName.setReadOnly(True)
        self.fileName.setFixedHeight(32)

        hashingButton = QPushButton("Hash file", self)
        hashingButton.setFixedHeight(48)
        self.hashName = QTextEdit(self)
        self.hashName.setReadOnly(True)
        self.hashName.setFixedHeight(32)

        # Layouts

        file_row.addWidget(uploadButton, stretch=0)
        file_row.addWidget(self.fileName, stretch=1)

        main_layout.addLayout(file_row)
        main_layout.addWidget(hashingButton)
        main_layout.addWidget(self.hashName)
        main_layout.addStretch()

        # Connect widgets to funcs
        uploadButton.clicked.connect(self.dialog)
        hashingButton.clicked.connect(self.hash)
        self.show()

    def dialog(self):
        self.file, check = QFileDialog.getOpenFileName(
            None,
            "QFileDialog.getOpenFileName()",
            "",
            self.tr("All Files (*)"),
        )

        if check:
            self.fileName.setText(self.file)

    def hash(self):
        try:
            file_checked = get_hash(self.file)
            self.hashName.setText(file_checked)
        except AttributeError:
            self.hashName.setText("please choose a file goddammit")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWin()
    sys.exit(app.exec())
