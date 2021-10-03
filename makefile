UI_FILES = main_window edge_param gauss_param threshold_param

main:
	if ls .temp; then rm -r .temp*; else mkdir .temp; fi
	for ui_file in $(UI_FILES); do pyuic5 -x ./UiForm/$${ui_file}.ui -o ./PyUi/$${ui_file}_ui.py; done
	python3 main.py
	rm -r .temp