import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, 
                             QVBoxLayout, QLabel, QStackedWidget, QLineEdit)
from PyQt6.QtCore import Qt

from lab1.back_end_lab1 import generateNumbers, runTest

from lab2.back_end_lab2 import padding, MD5, checkForIntegrity





class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('IS labs')
        self.setFixedSize(1200, 800)

        self.stacked_widget = QStackedWidget()

        self.lab1_page = self.create_lab1_page()
        self.lab2_page = self.create_lab2_page()
        self.lab3_page = self.create_lab3_page()
        self.lab4_page = self.create_lab4_page()
        self.lab5_page = self.create_lab5_page()
        self.main_page = self.create_main_page()

        self.stacked_widget.addWidget(self.main_page)
        self.stacked_widget.addWidget(self.lab1_page)
        self.stacked_widget.addWidget(self.lab2_page)
        self.stacked_widget.addWidget(self.lab3_page)
        self.stacked_widget.addWidget(self.lab4_page)
        self.stacked_widget.addWidget(self.lab5_page)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)


    def create_main_page(self):
        page = QWidget()
        
        layout = QVBoxLayout(page)
        layout.setSpacing(20)
        layout.addStretch()

        label = QLabel("Головне меню")
        label.setStyleSheet('''
            font-size: 40px; 
            font-weight: bold; 
            margin-bottom: 120px;        
        
            ''')

        layout.addWidget(label)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        labs = [self.lab1_page, self.lab2_page, self.lab3_page, self.lab4_page, self.lab5_page]

        for i, lab_page in enumerate(labs, 1):
            btn = QPushButton(f"Перейти до Лабораторної №{i}")
            if i < 3:
                btn.clicked.connect(lambda checked, lp=lab_page: self.stacked_widget.setCurrentWidget(lp))
            btn.setFixedHeight(40)
            btn.setFixedWidth(800)
            layout.addWidget(btn, alignment=Qt.AlignmentFlag.AlignCenter)


        layout.addStretch()

        exit_btn = QPushButton("Завершити роботу")
        exit_btn.setObjectName("ExitButton")
        exit_btn.clicked.connect(QApplication.instance().exit)
        layout.addWidget(exit_btn, alignment=Qt.AlignmentFlag.AlignCenter)


        return page


    def create_lab1_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setSpacing(20) 

        label = QLabel("Лабораторна робота №1\nГенератор псевдовипадкових чисел")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        user_input = QLineEdit()
        user_input.setPlaceholderText("Введіть число від 1 до 50...")
        user_input.setFixedWidth(400) 
        user_input.setFixedHeight(40)

        btn_generate = QPushButton("Згенерувати числа")
        btn_generate.setFixedWidth(200)

        result_display = QLabel()
        result_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        result_display.setStyleSheet("font-size: 25px; color: #191102;")
        result_display.setWordWrap(True)
        result_display.setFixedHeight(200)
        result_display.setFixedWidth(800)

        accuracy_display = QLabel()
        accuracy_display.setStyleSheet("font-size: 20px; color: #191102;")
        def on_generate():
            raw_text = user_input.text()
            try:
                count = int(raw_text)
                if count <= 0:
                    result_display.setText("Помилка: Число має бути додатним!")
                    return
                elif count > 50:
                    result_display.setText("Надто велике число значень для генерації, введіть менше значення")
                    return
                
                numbers = generateNumbers(count) 

                accuracy_results = runTest(numbers)
                accuracy_display.setText(f'Приблизне π на основі отриманого результату: {accuracy_results}')
                result_display.setText(f"Результат: {str(numbers)}")
                
            except ValueError:
                result_display.setText("Помилка: Введіть ціле число!")

        btn_generate.clicked.connect(on_generate)

        btn_back = QPushButton("Назад до меню")
        btn_back.setFixedWidth(200)
        btn_back.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))

        layout.addStretch() 
        layout.addWidget(label)
        layout.addWidget(user_input, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(btn_generate, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(result_display, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(accuracy_display, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch()
        layout.addWidget(btn_back, alignment=Qt.AlignmentFlag.AlignCenter)

        return page
    
    def create_lab2_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setSpacing(20) 

        label = QLabel("Лабораторна робота №2\nCтворення програмного засобу для забезпечення цілісності інформації")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        user_input = QLineEdit()
        user_input.setPlaceholderText("Введіть текст для хешування...")
        user_input.setFixedWidth(600) 
        user_input.setFixedHeight(40)

        btn_generate = QPushButton("Хешувати")
        btn_generate.setFixedWidth(200)

        result_display = QLabel()
        result_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        result_display.setStyleSheet("font-size: 25px; color: #191102; margin-top: 50px;")
        result_display.setWordWrap(True)
        result_display.setFixedHeight(100)
        result_display.setFixedWidth(800)

        def on_generate():
            raw_text = user_input.text()
            count = len(raw_text)
            if count > 48:
                result_display.setText("Надто велике значення для генерації, скористуйтесь файловим вводом")
                return
            
            self.hash = MD5(padding(raw_text))
            successLabel.hide()
            fileButton.show()
            result_display.setText(f"Результат: {str(self.hash)}")

        def file_write():
            self.filename = user_input.text()

            if self.filename == '':
                return

            with open(f'lab2/txt/{self.filename}.txt', 'w') as f:
                f.write(self.hash)

            user_input.setPlaceholderText('Введіть текст для хешування...')
            user_input.clear()
            successLabel.setText(f'Готово! Результат записано в {self.filename}')
            successLabel.show()
            btn_generate.show()
            btn_save_file.hide()
            result_display.setText('')

        def get_file_name():
            user_input.clear()
            btn_generate.hide()
            user_input.setPlaceholderText("Введіть ім'я файлу для збереження хешу...")
            fileButton.hide()
            btn_save_file.show()

        btn_save_file = QPushButton('Зберегти у файл')
        btn_save_file.hide()
        btn_save_file.clicked.connect(file_write)

        successLabel = QLabel()
        successLabel.setStyleSheet('color:#263B6A;font-size:20px')
        successLabel.hide()   
        
        fileButton = QPushButton('Записати в файл')
        fileButton.hide()
        fileButton.setFixedHeight(35)

        btn_generate.clicked.connect(on_generate)
        fileButton.clicked.connect(get_file_name)

        btn_back = QPushButton("Назад до меню")
        btn_back.setFixedWidth(200)
        btn_back.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))


        layout.addStretch() 
        layout.addWidget(label)
        layout.addStretch()
        layout.addWidget(user_input, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(successLabel, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(btn_generate, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(btn_save_file, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(result_display, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(fileButton, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch()
        layout.addWidget(btn_back, alignment=Qt.AlignmentFlag.AlignCenter)

        return page

    def create_lab3_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        
        label = QLabel("Лабораторна робота №3")
        btn_back = QPushButton("Назад до меню")
        
        btn_back.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        
        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(btn_back)
        return page
    
    def create_lab4_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        
        label = QLabel("Лабораторна робота №4")
        btn_back = QPushButton("Назад до меню")
        
        btn_back.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        
        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(btn_back)
        return page
    

    def create_lab5_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        
        label = QLabel("Лабораторна робота №5")
        btn_back = QPushButton("Назад до меню")
        
        btn_back.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        
        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(btn_back)
        return page


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    
    window.setStyleSheet('''
        QLabel {
        font-size: 30px; 
        font-weight: bold; 
        font-family: 'Segoe UI', sans-serif;
        color: #2c3e50;
        }

        QWidget {
            background-color: #bbd8b3
        }
        QPushButton {
            background-color: #F3B61F;
            color: white;
            border-radius: 10px; 
            padding: 10px;
            font-size: 16px;
            font-weight: bold;
        }
        QPushButton:hover {
            background-color: #a29f15
        }
        QLineEdit{
            font-size: 16px;
        }
        QPushButton#ExitButton:hover {
            background-color: #510D0A;
        }
        QPushButton#ExitButton {
            background-color: #EB4C4C; 
            width: 400px;
        }
    ''')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()