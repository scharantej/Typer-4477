## Flask Application Design for Two Text Boxes on a Website

### HTML Files

- **index.html**: The main HTML file that displays the two text boxes and a submit button.
- **results.html**: The HTML file that displays the result of the text boxes' content.

### HTML Content for index.html

```html
<!DOCTYPE html>
<html>
<head>
  <title>Two Text Boxes Website</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>
  <div class="container">
    <h1>Two Text Boxes</h1>
    <form action="/results" method="post">
      <div class="form-group">
        <label for="textbox1">Text Box 1:</label>
        <input type="text" class="form-control" id="textbox1" name="textbox1">
      </div>
      <div class="form-group">
        <label for="textbox2">Text Box 2:</label>
        <input type="text" class="form-control" id="textbox2" name="textbox2">
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</body>
</html>
```

### HTML Content for results.html

```html
<!DOCTYPE html>
<html>
<head>
  <title>Results</title>
</head>
<body>
  <div class="container">
    <h1>Results</h1>
    <p>Text Box 1: {{ textbox1 }}</p>
    <p>Text Box 2: {{ textbox2 }}</p>
  </div>
</body>
</html>
```

### Routes

- **index**: The route that displays the index.html file.
- **results**: The route that handles the form submission and displays the results.html file.

### Python Flask Application

```python
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
  textbox1 = request.form['textbox1']
  textbox2 = request.form['textbox2']
  return render_template('results.html', textbox1=textbox1, textbox2=textbox2)

if __name__ == '__main__':
  app.run()
```