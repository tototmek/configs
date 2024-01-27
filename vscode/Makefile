.PHONY: install pull

install:
	mkdir -p ~/.config/Code/User
	cp settings.json ~/.config/Code/User/settings.json
	cp keybindings.json ~/.config/Code/User/keybindings.json 
	@code $(foreach extension, $(shell cat extensions), --install-extension $(extension))


pull:
	cp ~/.config/Code/User/settings.json settings.json
	cp ~/.config/Code/User/keybindings.json keybindings.json
	code --list-extensions --show-versions > extensions