# Test 1 - mountain peaks

Prerequisite : docker compose shall be installed.

To deploy the project, download the repository.
Run the following commands from the top level directory of the project (should be your_path/peaks/):
	docker-compose build
	docker-compose up
	
Before you can test the api you have to perform the migrations to build the database using informations in the django project. To do so, open another terminal in the top level directory and run:
	docker ps
	
This will display the list of containers. Locate the 'peaks_web' image and copy its container ID.
Then run:
	docker exec -t -i paste_container_ID bash
	
This will launch a prompt where you can run:
	python manage.py migrate
	
You're now ready to enjoy the application. In your browser go to http://localhost:8000.

You'll have to add a few peaks in the database, following the link on the home page (http://localhost:8000/index/detail/).