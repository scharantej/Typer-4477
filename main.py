
# Updated Python Flask Application for Two Text Boxes Website

# Importing necessary modules
from flask import Flask, request, render_template

# Creating a Flask application
app = Flask(__name__)

# Defining the route for the main page
@app.route('/', methods=['GET'])
def index():
    """Main page of the application"""
    return render_template('index.html')  # Rendering the index.html file

# Defining the route to handle the form submission
@app.route('/results', methods=['POST'])
def results():
    """Processes the form data and displays the results"""
    # Extracting the data from the form
    textbox1 = request.form['textbox1']
    textbox2 = request.form['textbox2']
    
    # Sample data objects (replace with your own data as needed)
    sample_data = {
        'label1': 'Text Box 1:',
        'textbox1': textbox1,
        'label2': 'Text Box 2:',
        'textbox2': textbox2
    }
    
    # Rendering the results.html file with the data
    return render_template('results.html', sample_data=sample_data)

# Running the application
if __name__ == '__main__':
    app.run(debug=True)  # Running the application in debug mode for easier debugging
