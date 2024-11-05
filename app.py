from app import create_app
import logging
from healthcheck import HealthCheck

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
app = create_app()
app.app_context().push()

health = HealthCheck()

def app_working():
    return True, "App is working"

health.add_check(app_working)

app.add_url_rule("/health", "health", view_func=lambda:health.run())

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    
