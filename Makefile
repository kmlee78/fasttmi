run-server:
	/bin/bash scripts/start-dev.sh
dev-up:
	docker-compose -f docker-compose.yml up
dev-down:
	docker-compose -f docker-compose.yml down $(args)
dev-shell:
	docker-compose -f docker-compose.yml run --rm app /bin/bash