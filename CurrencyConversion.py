import sys
from decimal import *
from forex_python.converter import (CurrencyRates, CurrencyCodes)
from PySide6.QtWidgets import (QWidget, QApplication, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QComboBox, QLineEdit)
from __feature__ import snake_case, true_property

my_app = QApplication([])
r = CurrencyRates(force_decimal = True)
c = CurrencyCodes()

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.my_list = ['Pick a currency', 'Euro ' + c.get_symbol('EUR'), 'yen ' + c.get_symbol('JPY'), 
        'lev лв', 'koruna ' + c.get_symbol('CZK'), 'Danish krone ' + c.get_symbol('DKK'),
        'pound ' + c.get_symbol('GBP'), 'forint ' + c.get_symbol('HUF'), 'zloty ' + c.get_symbol('PLN'), 
        'leu ' + c.get_symbol('RON'), 'Swedish krona ' + c.get_symbol('SEK'), 'franc ' + c.get_symbol('CHF'), 
        'Icelandic króna ' + c.get_symbol('ISK'), 'Norweigian krone ' + c.get_symbol('NOK'), 'lira ' + c.get_symbol('TRY'), 
        'Australian dollar ' + c.get_symbol('AUD'), 'real ' + c.get_symbol('BRL'), 'Canadian dollar ' + c.get_symbol('CAD'), 
        'yuan ' + c.get_symbol('CNY'), 'Hong Kong dollar ' + c.get_symbol('HKD'), 'rupiah ' + c.get_symbol('IDR'), 
        'rupee ' + c.get_symbol('INR'), 'won ' + c.get_symbol('KRW'), 'Mexican peso ' + c.get_symbol('MXN'), 
        'ringgit ' + c.get_symbol('MYR'), 'New Zealand dollar ' + c.get_symbol('NZD'), 'Philippine peso ' + c.get_symbol('PHP'), 
        'Singapore dollar ' + c.get_symbol('SGD'), 'baht ' + c.get_symbol('THB'), 'rand ' + c.get_symbol('ZAR')]

        self.my_combo_box = QComboBox()
        self.my_combo_box.add_items(self.my_list)
        self.my_line_edit = QLineEdit('Enter a dollar amount')
        self.my_line_edit.select_all()
        self.my_line_edit.minimum_width = 150

        self.label = QLabel('')
        self.Label2 = QLabel(c.get_symbol('USD'))

        hbox = QHBoxLayout()
        hbox.add_widget(self.Label2)
        hbox.add_widget(self.my_line_edit)
        hbox.add_widget(self.my_combo_box)

        vbox = QVBoxLayout()
        vbox.add_layout(hbox)
        vbox.add_widget(self.label)
        self.set_layout(vbox)

        self.my_combo_box.currentIndexChanged.connect(self.update_ui)
        self.my_line_edit.textChanged.connect(self.update_ui)


    def update_ui(self):
        if self.my_combo_box.current_index > 0:
            amount = self.my_line_edit.text
            currency = self.currency_code(self.my_combo_box.current_index)
            self.label.text = "%.2f" % r.convert('USD', currency, Decimal(amount)) + " " + c.get_symbol(self.currency_code(self.my_combo_box.current_index))

    def currency_code(self, index):
        code_list = ['EUR', 'JPY', 'BGN', 'CZK', 'DKK', 'GBP', 'HUF', 'PLN', 'RON', 'SEK', 'CHF', 'ISK', 'NOK',
        'TRY', 'AUD', 'BRL', 'CAD', 'CNY', 'HKD', 'IDR', 'INR', 'KRW', 'MXN', 'MYR', 'NZD', 'PHP', 'SGD', 'THB', 'ZAR']

        for el in code_list:
            if index == (code_list.index(el) + 1):
                return el


my_win = Window()
my_win.show()
sys.exit(my_app.exec())