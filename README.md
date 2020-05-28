# FormationSimplon20200525NannyScrappy

# FormationSimplon20200525

## Note to set up docker
#### to build an image
```docker build -t <image name> .```

#### to run a container
```docker container run -it --name <container name> -p 8001:5000 -v "$(PWD):/workspace" -d <image name>```
e.g.: docker container run (--rm) -it --name "azure-ml" -p 8001:5000 -v "$(PWD):/workspace" (-d) jupyter-python
explaination:  	       containers name /  hostPC port: service port in container / $(PWD) = projects directory

#### to execute the container in bash
```docker exec -it <container name> bash```

#### start jupyter notebook in the containter
```jupyter notebook --port=5000 --NotebookApp.password='' --NotebookApp.token='' --no-browser --ip=0.0.0.0 --allow-root```

#### launch jupyter notebook in navigator
localhost:8001

## Consignes
Use Scrapy to scrap a site