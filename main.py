from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired
from bill import Bill, Flatmate
from flask.views import MethodView
from flask import Flask, render_template, request
from wtforms import Form, StringField

app = Flask(__name__)

class Homepage(MethodView):

    def get(self):
        return render_template('index.html')

class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template('bills_form.html', bill_form=bill_form)

class ResultPage(MethodView):

    def post(self):
        bill_form = BillForm(request.form)
        amount = float(bill_form.amount.data)
        period = bill_form.period.data

        the_bill = Bill(amount, period)

        flatmate_1 = Flatmate(bill_form.name1, int(bill_form.days_in_house_1.data))
        flatmate_2 = Flatmate(bill_form.name2, int(bill_form.days_in_house_2.data))

        return render_template('result.html',
                               name1=flatmate_1.name,
                               name2=flatmate_2.name,
                               amount1 = flatmate_1.pays(the_bill, flatmate_2),
                               amount2 = flatmate_2.pays(the_bill, flatmate_1))


class BillForm(Form):
    amount = StringField('Amount: ', validators=[DataRequired()], default= '1000')
    period = StringField('Period: ', validators=[DataRequired()], default= 'January 2024' )

    name1 = StringField('Name: ', validators=[DataRequired()], default= 'Mary')
    name2 = StringField('Name: ', validators=[DataRequired()], default= 'John')

    days_in_house_1 = IntegerField('Days in house: ', validators=[DataRequired()], default= 15)
    days_in_house_2 = IntegerField('Days in house: ', validators=[DataRequired()], default= 15)

    button = SubmitField('Calculate')



app.add_url_rule('/', view_func=Homepage.as_view('homepage'))
app.add_url_rule('/bills_form', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/result', view_func=ResultPage.as_view('result_page'))

app.run()

