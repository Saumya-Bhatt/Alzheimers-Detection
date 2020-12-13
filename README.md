# Alzheimers-Detection

## Running the webapp

1. Clone or download the files of this repository in your local machine.
2. In the root folder, run the following commands - 
```
  pip install pipenv
  pipenv shell
  pipenv install -r requirements.txt
```
 3. If any error arises, while downloading the required libraries, manually try to install them using `pip install <library name>`. This list of required libraries are mentioned in requirements.txt file and the pipfile.
 4. After all the libraries have been successfully installed, run the given below command to start the webapp
 ```
  streamlit run app.py
```

## Contributing

**Note :**
Do not change the requirement.txt file or the contents of the Procfile and setup.sh as it might clash with the heroku configurations. Do not add any Pipenv/Piplock files also.


