from datetime import datetime
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from qasync import asyncSlot
class Tab1(QWidget):
    def __init__(self):
        super().__init__()

        self.setLayout(QVBoxLayout())
        self.lbl_status = QLabel("Idle", self)
        self.layout().addWidget(self.lbl_status)
        self.btn = QPushButton("Push Me")
        self.btn.clicked.connect(self.push_me)
        self.layout().addWidget(self.btn)
    
    @asyncSlot()
    async def push_me(self):
        print(f"Clicked {datetime.now()}")