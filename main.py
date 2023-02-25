from flask import Flask, render_template
import lmproof

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


def proofread(text):
    proofread = lmproof.load('en')
    correction = proofread.proofread(text)
    print('Original: {}'.format(text))
    print('Correction: {}'.format(correction))


# proofread('I would lik to have a coffee with you')

if __name__ == '__main__':
    app.run(debug=True)
