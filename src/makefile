.PHONY: clean

NAME 	   	:= Modelos Bordes Imágenes
VERSION		:= 1.0
DEVELOPERS	:= Reinaldo Barrera Travieso, Ariel Plasencia Díaz
COPYRIGHT  	:= Copyright © 2021: $(DEVELOPERS)
UI_FILES	:= main_window edge_param gauss_param threshold_param about_app about_authors present

compile: ##Compile some files :)
	for ui_file in $(UI_FILES); do pyuic5 -x ./UiForm/$${ui_file}.ui -o ./PyUi/$${ui_file}_ui.py; done
	python3 Utils/remove_character.py

run: ## Open the app desktop ;)
	if ls .temp; then rm -r .temp*; else mkdir .temp; fi
	python3 main.py
	rm -rf .temp

info: ## Display project description
	@echo "$(NAME) v$(VERSION)"
	@echo "$(COPYRIGHT)"

version: ## Show the project version
	@echo "$(NAME) v$(VERSION)"

install: ## Install the project dependencies
	pip3 install PyQt5
	pip3 install skimage

clean: ## Remove temporary files
	rm -rf PyForm/__pycache__/
	rm -rf PyUi/__pycache__/
	rm -rf Utils/__pycache__/
	rm -rf .temp/*

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
