from flask import Flask
from flask import request

app = Flask(__name__)

def multiplyByThree(number):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        return str(int(number) * 3)
    except ValueError:
        return "Not a number"


@app.route("/")
def index():
    num = request.args.get("number", "")
    if num:
        finalNumber = multiplyByThree(num)
    else:
        finalNumber = ""
    return (
        """<form action="" method="get">
                Initial Number: <input type="text" name="number">
                <input type="submit" value="Multiply by 3">
            </form>"""
        + "final Num: "
        + finalNumber
    )


if __name__ == '__main__':
   app.run(debug = True)