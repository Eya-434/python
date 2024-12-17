from flask import Flask , render_template
app= Flask(__name__)

@app.route('/')
def checherboard8():
    return render_template ('index.html',rows=8, cols=8, color1='black', color2='red')

@app.route('/<int:rows>')
def checherboard4(rows):
    return render_template('index.html',rows= rows,cols=8, color1='black', color2='red' )

@app.route('/<int:rows>/<int:cols>')
def checherboard(eows, cols):
    return render_template('index.html', rows=rows, cols=cols, color1='black', color2='red')

@app.route('/<int:rows>/<int:cols>/<color1>/<color2>')
def checherboard(eows, cols, color1,color2):
    return render_template('index.html', rows=rows, cols=cols, color1=color1, color2=color2)

if __name__ =="__main__": app.run(debug = True)