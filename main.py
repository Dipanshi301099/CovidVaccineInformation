from flask import Flask, request,render_template, url_for ,redirect
import businesslayer 
#UPLAD_FLODER ='static/uploads'

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('test.html')

@app.route('/test',methods=['GET', 'POST'])
def test():
    return render_template('test.html')

@app.route('/showvac')
def show_vac():
    return render_template('getDetails.html', data=[], status=0)

@app.route('/vaccine_details', methods = ['GET', 'POST'])
def displayDetails():
    vaccine_name = request.form['vac_name']
    data,status = businesslayer.show_details(vaccine_name)
    return render_template('getDetails.html', data=data,status=status)

# @app.route('/vaccine_details', methods = ['GET', 'POST'])
# def displayDetails():
#     vaccine_name = request.form['vac_name']
#     status = businesslayer.show_details(vaccine_name)
#     return render_template('getDetails.html',status=status)




@app.route('/first1',methods=['GET','POST'])
def first1():
    return render_template('first1.html')

def display_on_console(vaccine_name,city_name,ava_date,vacc_qty,expiry_date):
    print("Vaccine Name :\t",vaccine_name)
    print("Available In :\t",city_name)
    print("Date :\t",ava_date)
    print("Vaccine Qty :\t",vacc_qty)
    print("Expiry Date :\t",expiry_date)

@app.route('/first2',methods=['GET','POST'])
def first2():
    print("Inside first2")
    _vac_name = request.form['fname']
    ava_detail = request.form['dname']
    ava_manufacture_loc = request.form['lname']
    manufacture_date = request.form['mname']
    ex_date = request.form['ename']
    print(_vac_name, ava_detail, ava_manufacture_loc, manufacture_date, ex_date)
    businesslayer.input_table1(_vac_name, ava_detail, ava_manufacture_loc, manufacture_date, ex_date)
    # display_on_console(_vac_name,ava_city,ava_date,qt_vacc,ex_date)
    print("Calling HTML Page in app route first 2")
    return render_template('first1.html')    

@app.route('/second2',methods=['GET', 'POST'])
def second2():
    print('inside second 2 main.py')
    return render_template('second2.html')



@app.route('/second1',methods=['GET','POST'])
def second1():
    print('inside main.py 1')
    _vac_name = request.form['vname']
    av_city = request.form['aname']
    av_date = request.form['avname']
    exp_date = request.form['nname']
    qtn_vacc = request.form['qname']
    print('inside main.py 2')
    print(_vac_name, av_city, av_date, exp_date, qtn_vacc)
    businesslayer.input_table2(_vac_name, av_city, av_date, exp_date, qtn_vacc)
    return render_template('second2.html')

@app.route('/third',methods=['GET','POST'])
def third():
    # // list of list
    # // data = [[name,manu,3,4],[name,manu,3,4]]
    
    return render_template('third.html')

def third3():
    return render_template('third.html')

if __name__ == '__main__':    
    # This is used when running locally. Gunicorn is used to run the
    #app.run(host='0.0.0.0', port=8080, debug=True, processes=4, threaded=True)
    app.run(threaded=True,debug=True)
    #app.run(host='127.0.0.1', port=8080, debug=True)
## [END app]

