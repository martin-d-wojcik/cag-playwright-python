# Playwright And Docker
This repository contains my project using Python Playwright 🎭 and Docker🐋

The project uses Page Object Model(POM) design pattern to implement the tests of [CAG Contactor Website](https://careers.contactor.cag.se/)



## Running the tests locally without docker
Clone the code and create a virtal environment. Install the ``requirements.txt`` and activate the virtual env, after that you can fire the below command

``pytest -v tests``

## Running the tests on docker

``docker build . -t playwright-python-end-2-end:v3``

### all tests without parallesism
``docker run -it playwright-python-end-2-end:v3 pytest -v``
