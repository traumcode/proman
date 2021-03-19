from flask import Flask, render_template, url_for, jsonify, request, redirect, flash, session


app = Flask(__name__)
app.secret_key = "secret"


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()