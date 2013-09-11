simple_react_py_app
===================
Build single page web application with React JS and Python

### Prerequisites
> Get pip to install other tools taht you need later.

    See instruction from
    http://www.pip-installer.org/en/latest/installing.html#install-or-upgrade-setuptools

> Get PyExecJS to enable JS processing in Pythin

    # you'd need `pip` to install PyExecJS
    sudo pip install PyExecJS

> Get PyReact to enable React JS processing in python

    sudo pip install PyReact

> Fix PyReact

    # Unfortunately, PyReact does not include the JS files required to process
    # React JS so we need to add them to PyReact manually.

    # Get React JS (see http://facebook.github.io/react/docs/getting-started.html)
    cd ~
    curl http://facebook.github.io/react/downloads/react-0.4.1.zip > react-0.4.1.zip
    unzip react-0.4.1.zip

    # move to the directory where 'PyReact' is installed
    sudo mkdir -p /usr/lib/python2.6/site-packages/react/js
    sudo mv react-0.4.1/build/react.js /usr/lib/python2.6/site-packages/react/js/react.js

    # clean up
    rm -fr react-0.4.1/

> Get NodeJS on your server

    # Install Node.js and NPM on your Amazon EC2 instance
    sudo apt-get install nodejs


###Install
> Get the source code

    git clone https://github.com/hedgerwang/simple_react_py_app
    cd simple_react_py_app

### Run on the Fly

>  Just hit your browser's refresh button to run an always-up-to-date version of your app.

    python lib/py/webserver.py
    open http://127.0.0.1:8080

