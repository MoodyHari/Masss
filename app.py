from flask import Flask,render_template,request
from notifications import send_email

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/single',methods=['GET','POST'])
def single():
    name = request.form['name']
    email = request.form['email']
    phone_number = request.form['phone_number']
    services = request.form['services']
    training = request.form['training']

    data = [name,email,phone_number,services,training]

    subject = "Enquiry"
    fileToSend = None
    msgg = " Name : "+name+" \n Phone Number : "+phone_number+" \n Email : "+email+" \n Services : "+services+"  \n Training : "+training+"  "

    toaddr = "grshsolutions@gmail.com"
    send_email(msgg,subject,toaddr,fileToSend)

    return render_template('index.html')


@app.route('/about',methods=['GET','POST'])
def about():
    return render_template('about.html')

@app.route('/architectural-Design',methods=['GET','POST'])
def architecturalDesign():
    return render_template('architectural-Design.html')

@app.route('/CAD-Services',methods=['GET','POST'])
def CADServices():
    return render_template('CAD-Services.html')

@app.route('/Civil-CADD',methods=['GET','POST'])
def CivilCADD():
    return render_template('Civil-CADD.html')

@app.route('/construction',methods=['GET','POST'])
def construction():
    return render_template('construction.html')

@app.route('/contact',methods=['GET','POST'])
def contact():
    return render_template('contact.html')

@app.route('/hydroponics',methods=['GET','POST'])
def hydroponics():
    return render_template('Hydroponics.html')

@app.route('/interior-design',methods=['GET','POST'])
def interiordesign():
    return render_template('interior-design.html')

@app.route('/nata',methods=['GET','POST'])
def nata():
    return render_template('nata.html')

@app.route('/rooftoplandscaping',methods=['GET','POST'])
def rooftoplandscaping():
    return render_template('rooftoplandscaping.html')

@app.route('/structural-consultancy',methods=['GET','POST'])
def structuralconsultancy():
    return render_template('structural-consultancy.html')


if __name__ == '__main__':
   app.run(debug=True)
