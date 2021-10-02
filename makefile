UI_FILES = main_window

main:
	mkdir .temp 
	for ui_file in $(UI_FILES); do pyuic5 -x ./UiForm/$${ui_file}.ui -o ./PyUi/$${ui_file}_ui.py; done
	python3 main.py
	rm -r .temp