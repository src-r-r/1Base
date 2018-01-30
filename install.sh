#!/bin/bash

PYTHON=$(which python)

cd onebase_common
$PYTHON setup.py develop
cd ../onebase_api
$PYTHON setup.py develop
