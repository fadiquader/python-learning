### Create python virtual env 
```shell
 python3 -m venv venv
 source venv/bin/activate
 
```

dump installed packages into `requirements.txt`
```shell
 # install any package you want 
pip install pytest 
pip freeze > requirements.txt
# install for deps file
pip install -r requirements.txt
