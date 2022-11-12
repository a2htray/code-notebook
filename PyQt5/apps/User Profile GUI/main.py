# -*- coding=utf-8 -*-
r"""
"""

import sys
import typing
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QFont, QPixmap


class Experience:
    def __init__(self, position, startDate, endDate=None):
        self.position = position
        self.startDate = startDate
        self.endDate = endDate

    def strDateRange(self) -> str:
        if self.endDate:
            res = f'{self.startDate} - {self.endDate}'
        else:
            res = f'{self.startDate} - Present'
        return res


class UserProfile(QWidget):
    def __init__(self, username, biography,
                 skills: typing.List,
                 experience: typing.Union[Experience, typing.List[Experience]]):
        super().__init__()
        self.username = username
        self.biography = biography
        self.skills = skills
        if isinstance(experience, Experience):
            self.experience = [experience]
        else:
            self.experience = experience

        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 250, 480)
        self.setWindowTitle('User Profile GUI')
        self.displayImages()
        self.displayUserProfile()
        self.show()

    def displayImages(self):
        backgroundImage = './assets/skyblue.png'
        profileImage = './assets/profile_image.png'

        try:
            with open(backgroundImage):
                background = QLabel(self)
                background.setPixmap(QPixmap(backgroundImage))
        except FileNotFoundError:
            print('Image not found')

        try:
            with open(profileImage):
                profile = QLabel(self)
                profile.setPixmap(QPixmap(profileImage))
                profile.move(75, 20)
        except FileNotFoundError:
            print('Image not found')

    def displayUserProfile(self):
        userName = QLabel(self.username, self)
        userName.move(50, 140)
        userName.setFont(QFont('Arial', 20))

        bioTitle = QLabel('Biography', self)
        bioTitle.move(15, 180)
        bioTitle.setFont(QFont('Arial', 17))

        about = QLabel(self.biography, self)
        about.setWordWrap(True)
        about.move(15, 220)

        skillTitle = QLabel('Skills', self)
        skillTitle.move(15, 270)
        skillTitle.setFont(QFont('Arial', 17))
        skill = QLabel(' | '.join(self.skills), self)
        skill.move(15, 310)

        experienceTitle = QLabel('Experience', self)
        experienceTitle.move(15, 330)
        experienceTitle.setFont(QFont('Arial', 17))

        for i, experience in enumerate(self.experience):
            experienceItem = QLabel(experience.position, self)
            experienceItem.move(15, 370 + i * 50)
            experienceDateRange = QLabel(experience.strDateRange(), self)
            experienceDateRange.move(15, 370 + i * 50 + 20)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UserProfile(
        username='a2htray yuen',
        biography="I'm a developer with 9 years experience. And now, I want to use PyQt to create a desktop "
                  "Application for visualization.",
        skills=['Go', 'Python', 'SQL', 'JavaScript', 'PHP'],
        experience=[
            Experience('Python Developer', '2016-05'),
            Experience('Web Developer', '2015-06', '2016-05')
        ]
    )
    sys.exit(app.exec())
