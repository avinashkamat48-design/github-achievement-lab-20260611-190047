PYTHON ?= python

.PHONY: test report help

help:
	@echo "Available targets:"
	@echo "  test    run the pytest suite"
	@echo "  report  generate a sample quality report"

test:
	$(PYTHON) -m pytest -q

report:
	$(PYTHON) -m achievement_lab.cli examples/quality-plan.json --report reports/quality-report.md
