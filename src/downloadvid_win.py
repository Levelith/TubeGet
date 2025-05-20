import re
from urllib.parse import urlparse, parse_qs
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QHBoxLayout, QPushButton, QLineEdit,
    QMessageBox
)
from PyQt5.QtCore import Qt

class DownloadVideoWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('TubeGet - Download Video')
        self.setFixedSize(400, 220)

        main_layout = QVBoxLayout()

        top_bar = QHBoxLayout()
        btn_back = QPushButton("⬅️")
        btn_back.setFixedSize(30, 30)
        btn_back.clicked.connect(self.go_back)
        top_bar.addWidget(btn_back)
        top_bar.addStretch()
        main_layout.addLayout(top_bar)

        label = QLabel('Enter the URL of the video you want to download:')
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 14px;")
        main_layout.addWidget(label)

        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText('Paste video URL here...')
        self.url_input.setFixedWidth(300)
        self.url_input.setAlignment(Qt.AlignCenter)
        self.url_input.setStyleSheet("font-size: 13px;")
        main_layout.addWidget(self.url_input, alignment=Qt.AlignCenter)

        self.download_btn = QPushButton('Download')
        self.download_btn.setFixedWidth(120)
        self.download_btn.clicked.connect(self.process_url)
        main_layout.addWidget(self.download_btn, alignment=Qt.AlignCenter)

        self.setLayout(main_layout)

    # TODO: It validates the URLs, in this case only the video URLs, by removing different parameters.
    def process_url(self):
        url = self.url_input.text().strip()
        if not url:
            QMessageBox.warning(self, "Missing URL", "Please enter a video URL.")
            return

        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)

        if "list" in query_params:
            QMessageBox.information(self, "Playlist Detected",
                                    "This appears to be a playlist URL.\nPlease use the 'Download Playlist' option instead.")
            return

        is_valid = False

        if "youtube.com" in parsed_url.netloc and parsed_url.path == "/watch":
            if "v" in query_params:
                is_valid = True

        elif "youtu.be" in parsed_url.netloc:
            if parsed_url.path.strip("/"):
                is_valid = True

        if not is_valid:
            QMessageBox.critical(self, "Invalid URL",
                                "Please enter a valid YouTube video URL (youtube.com/watch?v=... or youtu.be/...).")
            return

        # TODO: Here would go the download manager call
        QMessageBox.information(self, "Valid URL", f"Valid YouTube video URL:\n{url}")

    def go_back(self):
        from src.welcome import WelcomeWindow
        self.welcome = WelcomeWindow()
        self.welcome.show()
        self.close()