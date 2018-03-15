from jinja2 import Template
from itertools import product


def make_variations(run_maps):
    contexts = []
    for iter, run_map in enumerate(run_maps):

        map_keys = run_map.keys()
        map_ranges = [list(run_map[x]) for x in map_keys]
        for z in product(*map_ranges):
            context = dict({})
            for i, k in enumerate(map_keys):
                context[k] = str(z[i])
            contexts.append(context)
        return contexts


job_template = Template("""
apiVersion: batch/v1
kind: Job
metadata:
  name: jobexample-{{a}}-{{b}}
  labels:
    jobgroup: jobexample
spec:
  template:
    metadata:
      name: jobexample
      labels:
        jobgroup: jobexample
    spec:
      containers:
      - name: c
        image: busybox
        command: ["sh", "-c", "echo HRMC {{b}} {{b}} && sleep 5"]
      restartPolicy: Never
---
""")

var_map = {'a':[1,2],'b':[3,4]} 

variations = make_variations([var_map])
for k in variations:
    rendered_str = job_template.render(k)
    print(rendered_str)
