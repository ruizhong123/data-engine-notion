FROM python:3.12-slim

# Install PostgreSQL command-line tools
RUN apt-get update 
RUN apt-get install -y postgresql-client-17 cron

COPY start.sh /opt/airflow/start.sh

# Copy the ELT script 
COPY ELT_SCRIPT/ /opt/airflow/ELT_SCRIPT/

# design 3am to implement the excutable file
RUN echo "0 3 * * * python /opt/airflow/ELT_SCRIPT/elt_script.py" | crontab - 

# Set the default command to run the ELT script
CMD ["python", "/opt/airflow/ELT_SCRIPT/elt_script.py"]
