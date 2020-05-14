.DEFAULT_GOAL := help
.PHONY: init

help: ## Show this help.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":[^#]*?## "}; {printf "\033[36m%-50s\033[0m %s\n", $$1, $$2}'

init: ## Initialize project
	pip3 install -r requirements.txt
	ln -sf ../../bin/git-pre-commit-hook.sh .git/hooks/pre-commit

# vim: noexpandtab