### Project Name:
**StayFinder: Your Ultimate Hotel Search Companion**

### Description:
StayFinder, a cutting-edge hotel search engine, redefines your booking experience. Leveraging Elasticsearch, this Python project enables seamless hotel discovery based on age, stars, name, city, and availability. With Builder and Filter Design Patterns, StayFinder provides a flexible, extensible structure for a personalized and efficient search.

### Features:
- **Smart Search:** Effortlessly discover nearby hotels using age, stars, name, city, and availability criteria.
- **Geo-Location Enabled:** Precise location-based results with city center coordinates (latitude and longitude).
- **Flexible Structure:** Builder Design Pattern ensures fine control over complex hotel object creation.
- **Filtering Options:** Filter Design Pattern allows users to refine search results for a tailored experience.

### Technologies Used:
- **Python:** Core language for development.
- **Elasticsearch:** Backend powerhouse for efficient result searching.
- **Nginx and Flask:** Dynamic duo for web server configuration and microservices API development.

## Setup

1. Modify Elasticsearch connection in **parameters.yml**.

2. Run Docker Compose for the environment: 
   ```bash
   docker-compose up -d
   ```

3. Access the site at http://localhost:56733/test.

### Data Population

- Fill Elasticsearch with test data using:
  ```bash
  docker exec -it python_app python src/command/fill_elasticsearch.py
  ```

### Maintenance Commands

- Stop and remove containers:
  ```bash
  docker-compose stop
  ```

- Check logs:
  ```bash
  docker logs python_app -f
  tail -f /var/log/uwsgi.log (inside container)
  ```

- Refresh code:
  ```bash
  docker exec -it python_app touch uwsgi.ini
  ```

- Check coding standards:
  ```bash
  docker exec -it python_app flake8
  ```

- Run tests:
  ```bash
  docker exec -it python_app pytest -s
  ```

### How to Search

1. Using Swagger UI: http://localhost:56733/swagger-ui/
2. Manually through direct URL:
   http://localhost:56733/hotels/search?size=10&n=star&lat=52.21&page=1&lng=21.01&age=5&c=warsaw&fpn=true

### Additional Information

For more details on coding standards (Flake8), testing (Pytest), and documentation (Mock), refer to the following:
- [Pytest Documentation](https://docs.pytest.org/)
- [Mock Documentation](https://mock.readthedocs.io/)

**Usage:**
   - Explore the intuitive web interface to search for hotels based on your preferences.
   - Customize your search using the provided filters for a tailored experience.

Enhance your hotel search journey with StayFinder - where efficiency meets elegance! 🌟