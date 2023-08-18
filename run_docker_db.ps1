# Run PostgreSQL container
docker run -p 5432:5432 -e POSTGRES_USER=kolev-pg -e POSTGRES_PASSWORD=password -d -v my-postgres-data:/var/lib/postgresql/data --name pg-container postgres:latest

# Run pgAdmin container
docker run -p 5050:80 -e PGADMIN_DEFAULT_EMAIL=some_gamil@gmail.com -e PGADMIN_DEFAULT_PASSWORD=password -v my-data:/var/lib/pgadmin --name pg-admin -d dpage/pgadmin4

# Uncomment the python command as well if you want to load the datadump and fill the Tags fields automatically. Otherwise just fill them manually in the admin page. 
# Lunch, Desserts, Main Dish, Breakfast, Dinner, Snacks show be filled as independent Tags in the admin page otherwise some pages will not work properly


# python manage.py loaddata data.json