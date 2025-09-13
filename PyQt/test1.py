import sys

# 1. Імпорт QApplication та всіх необхідних віджетів
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

# 2. Створення екземпляру QApplication
app = QApplication([])

# 3. Створення графічного інтерфейсу додатку
window = QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(100, 100, 280, 80)
helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
helloMsg.move(60, 15)

# 4. Показати графічний інтерфейс програми
window.show()

# 5. Запуск циклу обробки подій програми
sys.exit(app.exec())

