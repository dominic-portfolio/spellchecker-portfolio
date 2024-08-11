# Flask Spellchecker Application

This is a Python-based spellchecker web application built using Flask, HTML, CSS, and JavaScript. The spellchecker uses two main libraries for spelling correction: **TextBlob** and **SymSpell**. Users can choose between different spellchecking methods, including combining both libraries for enhanced accuracy.


## Features

- **TextBlob Correction**: Provides context-aware corrections using the TextBlob library.
- **SymSpell Correction**: Uses a frequency-based approach with the SymSpell library for faster spelling corrections.
- **Combined Correction**: Combines the power of SymSpell for initial corrections and TextBlob for context-aware fine-tuning.
- **Simple Web Interface**: Users can input text, select a correction method, and view corrected output live through an easy-to-use web interface.

## Images
<p align="center">
  <img src="https://github.com/dominic-portfolio/spellchecker-portfolio/blob/master/usage.gif?raw=true" alt="program being used" />
</p>

## Usage

- Install dependencies: pip install -r requirements.txt
- Run the Flask application: python app.py
- Navigate to: http://127.0.0.1:5000/ (default address and port)




## API Endpoints

- `/`: Displays the main web interface.

- `/check`: POST endpoint for spellchecking. Accepts JSON data with the text to be corrected and the chosen method (textblob, SymSpell, or symspell+textblob).

### Example JSON Request:
    {
    "text": "Ths is a spleling errror.",
    "method": "SymSpell"
    }

### Example JSON Response:
    {
    "corrected": "This is a spelling error."
    }

## Acknowledgments

- TextBlob: [TextBlob Documentation](https://textblob.readthedocs.io/en/dev/)
- SymSpell: [SymSpellpy Documentation](https://symspellpy.readthedocs.io/en/latest/)
