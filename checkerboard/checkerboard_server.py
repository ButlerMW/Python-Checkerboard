# playground_server


from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('checkerboard_index.html', x=8, y=8)

@app.route('/<int:x>')
def eight_by(x):
    return render_template('checkerboard_index.html', x=x, y=8)
    
@app.route('/<int:x>/<int:y>')
def x_by_y(x,y):
    return render_template('checkerboard_index.html', x=x, y=y)

@app.route('/<int:x>/<int:y>/<color0>/<color1>')
def x_by_y_with_colors(x,y, color0, color1):
    return render_template('checkerboard_index.html', x=x, y=y, color0=color0, color1=color1)

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No Response..."

if __name__ == "__main__":
    app.run(debug=True)