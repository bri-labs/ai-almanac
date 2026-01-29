from flask import Flask

app=Flask(__name__)

# Define endpoint
@app.route("/")
def home():
    return "Hello world from Dockerized Flask app 3"

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=5000)
    # Flask watches for chagnes, and reflects change on save
    app.run(host="0.0.0.0", port=5000, debug=True)

