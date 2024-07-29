from flask import Flask, jsonify
import random

app = Flask(_name_)

# Helper functions
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def generate_fibonacci(n):
    fibonacci = [0, 1]
    while len(fibonacci) < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci[:n]

def generate_even(n):
    return [x for x in range(2, 2*n+1, 2)]

def generate_random(n):
    return [random.randint(1, 100) for _ in range(n)]

@app.route('/numbers/<id_type>/<int:count>', methods=['GET'])
def get_numbers(id_type, count):
    if count <= 0:
        return jsonify({'error': 'Count must be a positive integer'}), 400

    if id_type == 'p':
        num_list = generate_primes(count)
    elif id_type == 'f':
        num_list = generate_fibonacci(count)
    elif id_type == 'e':
        num_list = generate_even(count)
    elif id_type == 'r':
        num_list = generate_random(count)
    else:
        return jsonify({'error': 'Invalid ID type'}), 400

    average = sum(num_list) / len(num_list)
    return jsonify({'average': average, 'numbers': num_list})

if _name_ == '_main_':
    app.run(debug=True)