import npyscreen

class CurrencyConverter(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', MainForm, name="Currency Converter")
        self.addForm('ResultsForm', ResultsForm, name="Results")


class MainForm(npyscreen.ActionForm):
    def create(self):
        self.amount_to_convert = self.add(npyscreen.TitleText, name="Amount to convert: ", begin_entry_at=25)
        self.convert_from = self.add(npyscreen.TitleCombo, name="Convert From: ", values=self.getOptions(), begin_entry_at=25)
        self.convert_to = self.add(npyscreen.TitleCombo, name="Convert To: ", values=self.getOptions(), begin_entry_at=25)


    def afterEditing(self):
        self.parentApp.setNextForm('ResultsForm')

    def getOptions(self):
        options = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR',
         'GBP', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'JPY', 'KRW', 'MXN', 'MYR',
          'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']

        return options

    def on_ok(self):
        print(self.amount_to_convert.value)
        print(self.convert_from.value)
        print(self.convert_to.value)

    def on_cancel(self):
        exit()

class ResultsForm(npyscreen.Form):
    def create(self):
        self.add(npyscreen.TitleText, name="Results", value="TEST")

    def afterEditing(self):
        self.setNextForm(None)


if __name__ == '__main__':
    app = CurrencyConverter().run()
