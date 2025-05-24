import sys
from pathlib import Path
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from src.welcome import WelcomeWindow

def main():
    icon_path = Path(__file__).parent / "assets" / "icon.ico"
    
    if not icon_path.exists():
        print(f"Error: The icon was not found in: {icon_path}", file=sys.stderr)
        sys.exit(1)
    
    app = QApplication(sys.argv)
    
    try:
        app.setWindowIcon(QIcon(str(icon_path)))
    except Exception as e:
        print(f"Error al cargar el icono: {e}", file=sys.stderr)
    
    window = WelcomeWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()