#Dimitriy Leksanov
#HW04 -- Can I flask you a question?
#2017-09-23

from flask import Flask
my_app = Flask(__Name__)

@my_app.route('/')
def root():
    return "What kind"

@my_app.route('/next')
def next():
    return "of sorcery"

@my_app.route('/next/otherNext')
def otherNext():
    return "is this"

@my_app.route('/next/otherNext/otherOtherNext')
def otherOtherNext():
    return "?"

if __name__ == '__main__':
    my_app.run()
