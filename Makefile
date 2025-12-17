ENV_FILE = environment.yml

.PHONY: env html clean

env:
	@echo "Creating/updating conda environment from $(ENV_FILE)..."
	@conda env update -f $(ENV_FILE) || conda env create -f $(ENV_FILE)

html:
	@myst build --html

clean:
	@rm -rf figures
	@echo "Cleaned figures, audio, and _build directories."
