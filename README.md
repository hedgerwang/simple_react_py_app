simple_react_py_app
===================
Build single page web application with React JS and Python

### Prerequisites
> Get `pip` to install other tools that you will need later.

    See instruction from
    http://www.pip-installer.org/en/latest/installing.html#install-or-upgrade-setuptools

> Get `PyExecJS` to enable JS processing in Python

    sudo pip install PyExecJS

> Get `PyReact` to enable React JS processing in python

    sudo pip install PyReact

> Fix PyReact

    # Somehow PyReact does not include the JS files required to process
    # React JS so we need to add these JS files to PyReact manually.

    # Get React JS (see http://facebook.github.io/react)
    # Assume to get version `0.4.1`
    mkdir -p ~/temp_dir
    cd ~/temp_dir
    curl http://facebook.github.io/react/downloads/react-0.4.1.zip > react-0.4.1.zip
    unzip react-0.4.1.zip

    # Move to the directory where 'PyReact' is installed.
    # Assume to move to python2.6's directory.
    sudo mkdir -p /usr/lib/python2.6/site-packages/react/js
    sudo mv react-0.4.1/build/react.js /usr/lib/python2.6/site-packages/react/js/react.js

    # Clean up
    rm -fr ~/temp_dir

> Get NodeJS on your server

    # Please google 'Install NodeJS' on Mac/Linux/Windows and find totorials
    # yourself.


###Install
> Get the source code

    git clone https://github.com/hedgerwang/simple_react_py_app
    cd simple_react_py_app

### Run on the Fly

>  Just hit your browser's refresh button to run an always-up-to-date version
   of your app.

    python lib/py/webserver.py
    open http://127.0.0.1:8080/SimpleClockApp

