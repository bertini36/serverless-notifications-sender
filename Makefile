include .env
$(eval export $(shell sed -ne 's/ *#.*$//; /./ s/=.*$$// p' .env))

deploy: ## 🚀 Deploy app in AWS
	@echo "🚀 Let's deploy!!!"
	@docker-compose run --rm --entrypoint sh serverless -c "cd /code/ && serverless deploy"

clean:	## 🧹 Delete containers and their volumes
	@echo "🧹 Cleaning"
	@docker-compose down -v --remove-orphans
