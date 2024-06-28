from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

def is_valid_gstin(gstin):
    
    if len(gstin) == 15 :
        state_code = gstin[:2]
        pan_entity_code = gstin[2:12]
        checksum_digit = gstin[14]
    else :
        msg = 'GSTIN must be 15 char.'
        return {'input': gstin, 'GSTIN': False, 'msg' : msg}
    
    if len(gstin) != 15:
        msg = 'GSTIN must be 15 char.'
        return {'input': gstin, 'GSTIN': False, 'msg' : msg}
        
    elif not state_code.isnumeric():
        msg = 'State Code is not a number.'
        return {'input': gstin, 'GSTIN': False, 'msg' : msg}
       
    elif not pan_entity_code.isalnum() or not pan_entity_code.isupper():
        msg = 'Pan no is not valid.'
        return {'input': gstin, 'GSTIN': False, 'msg' : msg}
    
    elif not checksum_digit.isnumeric():
        msg = 'Last digit is not a number.'
        return {'input': gstin, 'GSTIN': False, 'msg' : msg}
   
    elif gstin[13] != 'Z':
        msg = '14th digit is not Z'
        return {'input': gstin, 'GSTIN': False, 'msg' : msg}
       
    else:
        msg = "Valid"
        return {'input': gstin, 'GSTIN': True, 'msg' : msg}

@app.route('/')
def home():
    return render_template('gstin.html')

@app.route('/gstin' , methods = ['GET', 'POST'])
def check():
    if request.method == 'POST':
    # Validate the GSTIN
        gstin = request.form['gstin']
        print(gstin)
        result = is_valid_gstin(gstin)
    
    # Return JSON response
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
