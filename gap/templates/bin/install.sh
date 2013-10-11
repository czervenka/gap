#!/bin/sh
set -e
cd $(dirname $0)/..

type pip > /dev/null || (easy_install pip)
pip install gap
bin/gip install -r requirements.gip
