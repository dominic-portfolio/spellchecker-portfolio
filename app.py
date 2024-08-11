import pkg_resources
import re
from flask import Flask, request, jsonify, render_template
from textblob import TextBlob
from symspellpy import SymSpell, Verbosity

app = Flask(__name__)

sym_spell = SymSpell(max_dictionary_edit_distance=3, prefix_length=7)
dictionary_path = pkg_resources.resource_filename(
    "symspellpy", "frequency_dictionary_en_82_765.txt"
)

sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)

def correct_word(input_term):
    # Lookup suggestions for the input term
    suggestions = sym_spell.lookup(input_term, Verbosity.CLOSEST, max_edit_distance=3, transfer_casing=True)
    
    # Return the best suggestion or the original term if no suggestions found
    if suggestions:
        return suggestions[0].term # suggestions returned as list
    else:
        return input_term

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    data = request.json
    text = data['text']
    method = data.get('method', 'textblob')
    
    if method == 'textblob':
        blob = TextBlob(text)
        corrected_text = str(blob.correct())
        
    elif method == 'SymSpell':
        tokens = re.findall(r'\w+|[^\w\s]', text, re.UNICODE)
        #corrected_tokens = [preserve_case(token, correct_word(token)) if token.isalpha() else token
        #for token in tokens]
        corrected_tokens = [correct_word(token) if token.isalpha() else token for token in tokens]
        corrected_text = ''.join(
        [token if token in '.,!?;:' else ' ' + token for token in corrected_tokens]).strip()
        #corrected_text = ' '.join([correct_word(word) for word in text.split()])
        
    elif method == 'symspell+textblob':
        tokens = re.findall(r'\w+|[^\w\s]', text, re.UNICODE)
        first_correction_tokens = [correct_word(token) if token.isalpha() else token
    for token in tokens]
        first_correction_text = ''.join([token if token in '.,!?;:' else ' ' + token for token in first_correction_tokens]).strip()
        #first_correction = ' '.join([correct_word(word) for word in text.split()])
        
        # Use TextBlob for context-aware correction on the initial corrected text
        blob = TextBlob(first_correction_text)
        corrected_text = str(blob.correct())
    else:
        corrected_text = text # no model used
    return jsonify({'corrected': corrected_text})

if __name__ == '__main__':
    app.run(debug=True)
    #host='192.168.1.64', port='50001', 
    
    

'''def preserve_case(token, corrected_token):
    if token.islower():
        return corrected_token.lower()
    elif token.isupper():
        return corrected_token.upper()
    elif token.istitle():
        return corrected_token.title() # all words uppercase in word
    else:
        return corrected_token'''