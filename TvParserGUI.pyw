#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import datetime

import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui

from FirstTvProgramParser import FirstTvProgramParser


class Form(QtGui.QDialog):
    def __init__(self, parent=None):

        """
        Create GUI
        """
        #super(Form, self).__init__(parent) # pycharm issue with old/new style class
        QtGui.QDialog.__init__(self,parent)
        dt = datetime.datetime.now()
        self.lineedit = QtGui.QLineEdit(dt.strftime('%d.%m.%Y'))
        self.lineedit.selectAll()
        self.browser = QtGui.QTextBrowser()
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.lineedit)
        layout.addWidget(self.browser)
        self.setLayout(layout)
        self.resize(400,500)
        self.setStyleSheet('font-size: 10pt; font-family: Tahoma;')
        self.lineedit.setFocus()
        self.connect(self.lineedit, QtCore.SIGNAL("returnPressed()"),
                                                        self.updateUi)
        self.setWindowTitle(u"Программа передач Первого канала")

    def updateUi(self):
        """
        Print out TV program to the browser element
        """
        FirstTvParser = FirstTvProgramParser()
        text = unicode(self.lineedit.text())
        FirstTvParser.day = text
        self.browser.clear()
        try:
            FirstTvParser.first_tv_parse()
        except ValueError:
            self.browser.append(u"<font color=red>Ошибка в строке: <br> <b>%s</b></font><background-color = red>" % text)
        else:
            for index, prog_time in enumerate(FirstTvParser.program[0]):
                self.browser.append("<b>%s</b> : %s" %(prog_time,                          #time for current program
                                                FirstTvParser.program[1][index]) )  #name of current program



app = QtGui.QApplication(sys.argv)
form = Form()
form.show()
app.exec_()

