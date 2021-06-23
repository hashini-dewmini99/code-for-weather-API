from flask import Flask, render_template,request
import requests

app=Flask(_name_)

@app.route('/teperature',methods=['POST'])
 def temperature():
   zipcode=request.form['zip']
   
   r=request.get('https://openweathermap.org/current='+zipcode+'1a7bf5bf8b7d3b76a2524813b8c9cc10api')
   json_object=r.json
   temp_k=float(json_object['main']['temp'])
   temp_f=(temp_k-273.15)*1.8+32
  
  return render_template('temperature.html',temp=temp_f)
@app.route('/')
def index():
   return render_template('index.html')

if_name_ =='_main_':
 app.run(debug=True)