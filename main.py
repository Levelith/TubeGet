import sys
from PyQt5.QtWidgets import QApplication
from src.welcome import WelcomeWindow

def main():
    app = QApplication(sys.argv)
    window = WelcomeWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
