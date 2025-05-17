from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QWindow

class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('TubeGet - Settings')
        self.setFixedSize(300, 200)

        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        layout = QVBoxLayout()

        label = QLabel('TubeGet Settings')
        layout.addWidget(label)

        button_layout = QHBoxLayout()
        btn_save = QPushButton('Save')
        btn_cancel = QPushButton('Cancel')
        btn_save.clicked.connect(self.save_settings)
        btn_cancel.clicked.connect(self.close)

        button_layout.addStretch()
        button_layout.addWidget(btn_save)
        button_layout.addWidget(btn_cancel)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def save_settings(self):
        QMessageBox.information(self, 'Save', 'All configurations have been successfully saved')
        self.accept()