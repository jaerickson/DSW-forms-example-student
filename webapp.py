from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/", methods=['GET'])
def render_main():
    return render_template('home.html')
@app.route("/response", methods=['POST'])
def render_response():
    color = request.form['color']
    #The request object stores information about the request sent to the server. 
    #args is a MultiDict (like a dictionary bu tcan have multiple values for the same key)
    #The information in args is visible in the url for the page being requested (ex. .../response?color=blue
    if color == 'purple' :
        reply = "That's my favorite color,too!"
    else:
        reply = "My favorite color is purple."
    return render_template('response.html', response = reply)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
