.PHONY: env all

env:
	conda env create -f environment.yml

all:
	jupyter nbconvert --execute --to notebook --inplace notebooks/*.ipynb
	jupyter nbconvert --to pdf notebooks/*.ipynb --output-dir pdf_builds
