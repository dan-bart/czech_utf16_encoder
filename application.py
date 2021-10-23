from flask import Flask,render_template, request
from czech_utf16_encoder.encoder import Czech_Hex_Encoder
from czech_utf16_encoder.forms import InputForm,OutputForm,RetrieveDBInfo
from czech_utf16_encoder.models import Data
from czech_utf16_encoder import db
from czech_utf16_encoder import app as application

# application = Flask(__name__)
# application.debug=True
# # change this to your own value
# application.secret_key = '1234'   

@application.route('/', methods=['POST', 'GET'])
def index():
    input_form = InputForm(request.form)
    output_form = OutputForm()
    if request.method == 'POST':
        input_text = input_form.input_field.data
        encoder = Czech_Hex_Encoder()
        processed_text = encoder.hex_encode(input_text)
        output_form.output_field.data = processed_text
        data_entry = Data(entry = input_text, output = processed_text)
        if input_text != "":
            try:     
                db.session.add(data_entry)
                db.session.commit()        
                db.session.close()
            except:
                db.session.rollback()
        return render_template('index.html',input_form = input_form,output_form = output_form)
    else:
        output_form.output_field.data = ""
        return render_template('index.html',input_form = input_form,output_form = output_form)


@application.route("/log",methods = ["POST","GET"])
def log():
    form_log = RetrieveDBInfo(request.form) 
    print(form_log.validate())
    print(form_log.validate_on_submit())
    if request.method == 'POST' and form_log.validate_on_submit():
        try:   
            num_return = int(form_log.numRetrieve.data)
            query_db = Data.query.order_by(Data.id.desc()).limit(num_return)

            db.session.close()
        except:
            db.session.rollback()
        return render_template('db_results.html', form = form_log, results=query_db, num_return=num_return)                
    
    return render_template('logs.html', form=form_log)

if __name__ == "__main__":
    application.run(debug=True)
