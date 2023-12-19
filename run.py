# run.py
from app import create_app
print('running')
app = create_app()

if __name__ == '__main__':
    print("yes")
    app.run(debug=True)
