from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QPushButton, QMessageBox, QHBoxLayout,
    QSpacerItem, QSizePolicy
)
from PyQt5.QtCore import Qt
from src.downloadvid_win import DownloadVideoWindow
from src.downloadpl_win import DownloadPlaylistWindow

class WelcomeWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TubeGet - Welcome")
        self.setFixedSize(400, 200)

        main_layout = QVBoxLayout()

        label = QLabel("Welcome to TubeGet!\nSelect an option to continue:")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 16px; font-weight: bold;")

        btn_video = QPushButton("Download Video")
        btn_playlist = QPushButton("Download Playlist")

        btn_video.clicked.connect(self.download_video)
        btn_playlist.clicked.connect(self.download_playlist)

        main_layout.addWidget(label)
        main_layout.addSpacing(20)
        main_layout.addWidget(btn_video)
        main_layout.addWidget(btn_playlist)

        main_layout.addStretch()

        bottom_layout = QHBoxLayout()
        bottom_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        btn_settings = QPushButton("⚙️")
        btn_settings.clicked.connect(self.open_settings)
        bottom_layout.addWidget(btn_settings)

        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)

    def download_video(self):
        self.video_window = DownloadVideoWindow()
        self.video_window.show()
        self.close()

    def download_playlist(self):
        self.playlist_window = DownloadPlaylistWindow()
        self.playlist_window.show()
        self.close()

    def open_settings(self):
        QMessageBox.information(self, "Settings", "Here would be the configuration window.")