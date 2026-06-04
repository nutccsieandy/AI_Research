import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
    QHBoxLayout, QLineEdit, QListWidget, QListWidgetItem,
    QFrame, QMessageBox
)
from PyQt6.QtCore import Qt


class TaskApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Andy TaskFlow｜任務管理")
        self.resize(900, 560)
        self.set_ui()

    def set_ui(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #0f172a;
                color: #ffffff;
                font-family: "Microsoft JhengHei", "PingFang TC";
                font-size: 16px;
            }

            QLabel#title {
                font-size: 34px;
                font-weight: bold;
                color: #ffffff;
            }

            QLabel#subtitle {
                font-size: 15px;
                color: #94a3b8;
            }

            QFrame#card {
                background-color: #1e293b;
                border-radius: 22px;
                padding: 24px;
            }

            QLineEdit {
                background-color: #334155;
                border: 2px solid #475569;
                border-radius: 14px;
                padding: 13px;
                color: white;
                font-size: 16px;
            }

            QLineEdit:focus {
                border: 2px solid #38bdf8;
            }

            QPushButton {
                background-color: #0ea5e9;
                color: white;
                border: none;
                border-radius: 14px;
                padding: 13px 22px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #38bdf8;
            }

            QPushButton#deleteBtn {
                background-color: #ef4444;
            }

            QPushButton#deleteBtn:hover {
                background-color: #f87171;
            }

            QListWidget {
                background-color: #0f172a;
                border: none;
                border-radius: 14px;
                padding: 10px;
            }

            QListWidget::item {
                background-color: #334155;
                margin: 7px;
                padding: 14px;
                border-radius: 12px;
            }

            QListWidget::item:selected {
                background-color: #0ea5e9;
            }
        """)

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(35, 35, 35, 35)
        main_layout.setSpacing(25)

        sidebar = QFrame()
        sidebar.setObjectName("card")
        sidebar.setFixedWidth(250)

        sidebar_layout = QVBoxLayout()
        title = QLabel("TaskFlow")
        title.setObjectName("title")

        subtitle = QLabel("漂亮的 PyQt6\n桌面任務管理工具")
        subtitle.setObjectName("subtitle")

        info = QLabel("功能：\n\n✓ 新增任務\n✓ 刪除任務\n✓ 清空任務\n✓ 現代化 UI")
        info.setStyleSheet("color:#cbd5e1; line-height: 1.5;")

        sidebar_layout.addWidget(title)
        sidebar_layout.addWidget(subtitle)
        sidebar_layout.addSpacing(35)
        sidebar_layout.addWidget(info)
        sidebar_layout.addStretch()
        sidebar.setLayout(sidebar_layout)

        content = QFrame()
        content.setObjectName("card")

        content_layout = QVBoxLayout()
        header = QLabel("我的任務清單")
        header.setObjectName("title")

        desc = QLabel("輸入任務後按下新增，快速管理今天要完成的事情。")
        desc.setObjectName("subtitle")

        input_layout = QHBoxLayout()
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("請輸入任務，例如：完成 PyQt 專案")

        add_btn = QPushButton("新增任務")
        add_btn.clicked.connect(self.add_task)

        input_layout.addWidget(self.task_input)
        input_layout.addWidget(add_btn)

        self.task_list = QListWidget()

        btn_layout = QHBoxLayout()
        delete_btn = QPushButton("刪除選取")
        delete_btn.setObjectName("deleteBtn")
        delete_btn.clicked.connect(self.delete_task)

        clear_btn = QPushButton("清空全部")
        clear_btn.clicked.connect(self.clear_tasks)

        btn_layout.addWidget(delete_btn)
        btn_layout.addWidget(clear_btn)

        content_layout.addWidget(header)
        content_layout.addWidget(desc)
        content_layout.addSpacing(15)
        content_layout.addLayout(input_layout)
        content_layout.addSpacing(15)
        content_layout.addWidget(self.task_list)
        content_layout.addLayout(btn_layout)

        content.setLayout(content_layout)

        main_layout.addWidget(sidebar)
        main_layout.addWidget(content)

        self.setLayout(main_layout)

    def add_task(self):
        text = self.task_input.text().strip()
        if not text:
            QMessageBox.warning(self, "提醒", "請先輸入任務內容。")
            return

        item = QListWidgetItem("  " + text)
        self.task_list.addItem(item)
        self.task_input.clear()

    def delete_task(self):
        selected = self.task_list.currentRow()
        if selected >= 0:
            self.task_list.takeItem(selected)
        else:
            QMessageBox.information(self, "提醒", "請先選擇要刪除的任務。")

    def clear_tasks(self):
        self.task_list.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaskApp()
    window.show()
    sys.exit(app.exec())
