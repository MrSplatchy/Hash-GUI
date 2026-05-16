import hashlib
import os
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


def get_hash(file_path):
    CHUNK_SIZE = 65536
    file_path = os.path.abspath(file_path)

    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(CHUNK_SIZE):
            sha256.update(chunk)

    return sha256.hexdigest()


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 200)
        self.setWindowTitle("Hash-GUI")

        # Central widget and main layout
        central = QWidget(self)
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(12)

        # Create widgets
        self.uploadButton = QPushButton("Open file", self)
        self.fileName = QTextEdit(self)
        self.fileName.setReadOnly(True)
        self.fileName.setFixedHeight(32)

        self.hashingButton = QPushButton("Hash file", self)
        self.hashingButton.setFixedHeight(48)
        self.hashName = QTextEdit(self)
        self.hashName.setReadOnly(True)
        self.hashName.setFixedHeight(32)

        # Create layout for file row
        file_row = QHBoxLayout()
        file_row.setSpacing(8)
        file_row.addWidget(self.uploadButton, stretch=0)
        file_row.addWidget(self.fileName, stretch=1)

        # Add widgets and layouts to main layout
        main_layout.addLayout(file_row)
        main_layout.addWidget(self.hashingButton)
        main_layout.addWidget(self.hashName)
        main_layout.addStretch()

        # Connect signals
        self.uploadButton.clicked.connect(self.dialog)
        self.hashingButton.clicked.connect(self.hash)

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
            self.setWindowTitle("Hashing...")  # Yes the title change is necessary.
            file_checked = get_hash(self.file)
            self.setWindowTitle("Hash-GUI")
            # Shows the hashed text
            self.hashName.setText(file_checked)
        except AttributeError:
            self.hashName.setText("Please choose a file")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWin()
    sys.exit(app.exec())
