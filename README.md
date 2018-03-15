	docker-compose build makeexpansionjob | docker-compose run makeexpansionjob | kubectl create -f -	

	
        cd worker-queue-2
        kubectl create -f worker-queue-2/redis-pod.yaml
	kubectl create -f worker-queue-2/redis-service.yaml
        cd ..
        docker-compose build makeworkerjob | docker-compose run makeworkerjob
        kubectl create -f job.yaml
        kubectl get pods -a -o wide
        kubectl logs -l job-name=job-wq-2
