from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def func():
    return render_template('class.html')
@app.route('/About',methods=['GET','POST'])
def abc():
    if (request.method=='POST'):
        x=request.form['a']
        y=request.form['b']
        z=request.form['gender']
        p=request.form['profession']
        c=request.form['course']
        print(x,y,z,p,c)
        return render_template('class.html')
if __name__ == "__main__":
    app.run()
