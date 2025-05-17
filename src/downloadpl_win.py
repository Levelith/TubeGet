from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout,
    QHBoxLayout, QPushButton
)
from PyQt5.QtCore import Qt

class DownloadPlaylistWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Tube Get - Download Playlist')
        self.setFixedSize(400, 200)

        main_layout = QVBoxLayout()

        top_bar = QHBoxLayout()
        btn_back = QPushButton("⬅️")
        btn_back.setFixedSize(30, 30)
        btn_back.clicked.connect(self.go_back)

        top_bar.addWidget(btn_back)
        top_bar.addStretch()

        main_layout.addLayout(top_bar)

        label = QLabel('Interface to download playlist')
        label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(label)

        self.setLayout(main_layout)

    def go_back(self):
        from src.welcome import WelcomeWindow
        self.welcome = WelcomeWindow()
        self.welcome.show()
        self.close()