from app import create_app

#Creates Flask Instance
app = create_app()

#only executes if main.py is called
if __name__ == '__main__':
    #Starts the server and activates the debug mode
    app.run(debug=True)