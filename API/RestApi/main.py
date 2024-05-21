from flask import Flask, jsonify, request

app = Flask(__name__)

def is_valid_gstin(gstin):
    state_code = gstin[:2]
    pan_entity_code = gstin[2:12]
    checksum_digit = gstin[14]
    
    if len(gstin) != 15:
        return {'input': gstin, 'GSTIN': False}
        
    elif not state_code.isalpha() or not state_code.isupper():
        return {'input': gstin, 'GSTIN': False}
       
    elif not pan_entity_code.isalnum() or not pan_entity_code.isupper():
        return {'input': gstin, 'GSTIN': False}
   
    elif not checksum_digit.isdigit():
        return {'input': gstin, 'GSTIN': False}
       
    else:
        return {'input': gstin, 'GSTIN': True}

@app.route('/')
def home():
    return 'HOME PAGE'

@app.route('/validate_gstin/<string:gstin>')
def check(gstin):
    # Validate the GSTIN
    result = is_valid_gstin(gstin)
    
    # Return JSON response
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
