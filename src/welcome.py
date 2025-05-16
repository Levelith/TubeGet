from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
)
from PyQt5.QtCore import Qt

class WelcomeWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TubeGet - Welcome")
        self.setFixedSize(400, 200)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        label = QLabel("Welcome to TubeGet!\nSelect an option to continue:")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 16px; font-weight: bold;")

        btn_video = QPushButton("Download Video")
        btn_playlist = QPushButton("Download Playlist")

        btn_video.clicked.connect(self.download_video)
        btn_playlist.clicked.connect(self.download_playlist)

        layout.addWidget(label)
        layout.addSpacing(20)
        layout.addWidget(btn_video)
        layout.addWidget(btn_playlist)

        self.setLayout(layout)

    def download_video(self):
        QMessageBox.information(self, "Video", "Aquí iría la lógica para descargar un video.")

    def download_playlist(self):
        QMessageBox.information(self, "Playlist", "Aquí iría la lógica para descargar una playlist.")
