from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout,
    QHBoxLayout, QPushButton, QLineEdit,
    QMessageBox
)
from PyQt5.QtCore import Qt
from src.validations.validations import is_valid_youtube_playlist

class DownloadPlaylistWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Tube Get - Download Playlist')
        self.setFixedSize(400, 220)

        main_layout = QVBoxLayout()

        top_bar = QHBoxLayout()
        btn_back = QPushButton('⬅️')
        btn_back.setFixedSize(30, 30)
        btn_back.clicked.connect(self.go_back)
        top_bar.addWidget(btn_back)
        top_bar.addStretch()
        main_layout.addLayout(top_bar)

        label = QLabel('Paste your YouTube playlist URL:')
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 14px;")
        main_layout.addWidget(label)

        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText('https://www.youtube.com/playlist?list=...')
        self.url_input.setFixedWidth(300)
        self.url_input.setAlignment(Qt.AlignCenter)
        self.url_input.setStyleSheet("font-size: 14px;")
        main_layout.addWidget(self.url_input, alignment=Qt.AlignCenter)

        self.download_btn = QPushButton('Download')
        self.download_btn.setFixedWidth(120)
        self.download_btn.clicked.connect(self.process_url)
        main_layout.addWidget(self.download_btn, alignment=Qt.AlignCenter)

        self.setLayout(main_layout)

    def process_url(self):
        url = self.url_input.text().strip()
        if not url:
            QMessageBox.warning(self, 'Missing URL', 'Please enter a playlist URL.')
            return

        is_valid, message = is_valid_youtube_playlist(url)
        
        if not is_valid:
            QMessageBox.critical(self, 'Invalid URL', message)
            return
        
        # TODO: Here would be the call for the playlist download manager
        QMessageBox.information(self, 'Valid Playlist', f'Valid Playlist URL:\n{url}')

    def go_back(self):
        from src.welcome import WelcomeWindow
        self.welcome = WelcomeWindow()
        self.welcome.show()
        self.close()