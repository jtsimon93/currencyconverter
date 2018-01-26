import npyscreen
from currencyconverter import CurrencyConverter

class CurrencyConverterApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', MainForm, name="Currency Converter")


class MainForm(npyscreen.ActionForm):
    def create(self):
        self.amount_to_convert = self.add(npyscreen.TitleText, name="Amount to convert: ", begin_entry_at=25)
        self.convert_from = self.add(npyscreen.TitleCombo, name="Convert From: ", values=self.getOptions(), begin_entry_at=25)
        self.convert_to = self.add(npyscreen.TitleCombo, name="Convert To: ", values=self.getOptions(), begin_entry_at=25)


    def afterEditing(self):
        self.parentApp.setNextForm('MAIN')

    def getOptions(self):
        options = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR',
         'GBP', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'JPY', 'KRW', 'MXN', 'MYR',
          'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']

        return options

    def on_ok(self):
        # call to show Results
        self.show_results()

    def on_cancel(self):
        exit()

    def show_results(self):

        #npyscreen.notify_confirm(str(self.getOptions()[self.convert_to.value]), title='ERROR')

        # Check to see if user is trying to convert to the same currency, alert if so
        if self.convert_from.value == self.convert_to.value:
            # display error
            npyscreen.notify_confirm('Cannot convert to same currency', title='ERROR')
        else:
            # For readability, type casting and assigning to var
            to_convert = float(self.amount_to_convert.value)
            to_convert_from = str(self.getOptions()[self.convert_from.value])
            to_convert_to = str(self.getOptions()[self.convert_to.value])
            result = CurrencyConverter.convert(to_convert, to_convert_from, to_convert_to)

            message = str(to_convert) + ' ' + to_convert_from + ' = ' + str(result) + ' ' + to_convert_to
            npyscreen.notify_confirm(message, title='Results')



if __name__ == '__main__':
    app = CurrencyConverterApp().run()
