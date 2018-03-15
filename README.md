# K8sTest

## Expansion Parallelism from map

Given a map, create set of sweep values and Kubernetes jobs to process each job.  When finished processing, the jobs will exit.:

		docker-compose build makeexpansionjob | docker-compose run makeexpansionjob | kubectl create -f -
		kubectl logs -l job-name=job-wq-2

Monitor progress:

		kubectl get pods -a -o wide
		kubectl logs -l job-name=job-wq-2


##  Worker Parallelism from map

Create work queue (redis) and setup set of workerjobs that pull parameters from the queue, process and then repeat until queue is empty.
Then populate queue with the sweep value sets based on the map.

Setup redis service:

        kubectl create -f worker-queue-2/redis-pod.yaml
		kubectl create -f worker-queue-2redis-service.yaml

Populate queue with sweep parameters:

        docker-compose build makeworkerjob | docker-compose run makeworkerjob

Create worker to start processing:

        kubectl create -f job.yaml

Monitor progress:

        kubectl get pods -a -o wide
        kubectl logs -l job-name=job-wq-2
