from app import app
from flask import request,jsonify,render_template,request,json






@app.route('/')
def main():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculateNum():
     firstnum=int(request.form['input1'])
     secondnum=int(request.form['input2'])
     operations=int(request.form['operations'])  
     if operations==1:
        return jsonify({'input1':result})
     elif operations==2:
        result=firstnum-secondnum
        return jsonify({'input1':result})
     elif operations==3:
        result=firstnum/secondnum
        return jsonify({'input1':result})
     elif operations==4:
        result=firstnum*secondnum
        return jsonify({'input1':result})
        
   #Basically passes in the data from the form and according to the operations , it will add/subtract/multiply/divide then puts it in a jsonify back to done function
      
         
    
    
  
    