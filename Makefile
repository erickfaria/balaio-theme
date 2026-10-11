PYTHON ?= python3

.PHONY: check locales preview serve

check:
	$(PYTHON) scripts/validate_docs.py
	$(PYTHON) scripts/build_locales.py --check
	$(PYTHON) scripts/validate_theme.py
	$(PYTHON) -m unittest discover -s tests -v
	git diff --check

locales:
	$(PYTHON) scripts/build_locales.py

preview:
	$(PYTHON) scripts/build_preview.py

serve: preview
	$(PYTHON) -m http.server 8765 --bind 127.0.0.1 --directory preview
