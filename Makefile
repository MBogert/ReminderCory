# Courtesy of https://gist.github.com/hynek/5e85706cee589a204251b33359585392 #

update-deps:
    pip-compile --upgrade --generate-hashes
    pip-compile --upgrade --generate-hashes --output-file dev-requirements.txt dev-requirements.in
    pip install --upgrade -r requirements.txt  -r dev-requirements.txt

install
    pip install --editable .

init:
    pip install pip-tools
    rm -rf .tox

update: init update-deps install

.PHONY: update-deps init update install

# End Quote #

define activate_env
# 	TODO Implementation
endef