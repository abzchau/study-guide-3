from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "blahhhhhhhh"


MESSAGES = {"cheery": "This is awesome.", "dreary": "This is brutal.", "honest": "This is painful."}



@app.route('/')
def show_homepage():
    return render_template('homepage.html')

###############################
#                             #
# 1) Finish the routes below. #
#                             #
###############################


@app.route('/form')
def show_form():
    return render_template('results.html')

@app.route('/results')
def show_results():
    name = request.args.get('person')
    result =request.args.get("mood")
    print(result)
    message = MESSAGES[result]
    print(message)
    return render_template('results.html', result=result, message=message, name=name)

@app.route('/save_name')
def say_hello():
    name = request.args.get('person')
    session['name'] = name
    print(session)
    return render_template('form.html')

@app.route('/clear_session')
def clear_session():
    session.clear()
    return 'Woop, cleared session.'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
