from flask import Flask, render_template, request
from babel import numbers, dates
from datetime import date, datetime, time
from flask_babel import Babel, format_date, gettext

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

#@babel.localeselector
#def get_locale():
   # return 'en'
    #request.accept_languages.best_match(['en', 'es', 'de'])

@app.route('/')
def index():
    
    antony = gettext('Antony')
    us_num = numbers.format_decimal(1.2345, locale='en_US')
    se_num = numbers.format_decimal(1.2345, locale='sv_SE')
    de_num = numbers.format_decimal(1.2345, locale='de_DE')

    d = date(2007, 4, 1)
    us_date = dates.format_date(d, locale='en_US')
    de_date = format_date(d)

    dt = datetime(2008, 8, 3, 15, 30)
    us_datetime = dates.format_datetime(dt, locale='en_US')


    result = {'us_num' : us_num, 'se_num': se_num, 'de_num': de_num, 'us_date':us_date, 'de_date':de_date, 'us_datetime': us_datetime}
    return render_template('index.html', result=result, antony=antony)

if __name__ == "__main__":
    app.run(debug=True)