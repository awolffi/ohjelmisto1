from flask import Flask

app = Flask(__name__)
@app.route('/alkuluku/<int:num>')
def check_if_prime(num):
    
    if num > 1:
        for x in range(2, (num//2)+1):
            if num % x == 0:
                is_prime = False
                break
        else:
            is_prime = True
    else:
        is_prime = False

    response = {
        "number" : num,
        "isPrime" : is_prime
    }

    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
