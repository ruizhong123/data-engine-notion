FROM python:3.12-slim


# Install PostgreSQL command-line tools
RUN apt-get update 
RUN apt-get uninstall -y postgresql-client-15 && apt-get install -y postgresql-client-17 cron

COPY start.sh app/start.sh

# Copy the ELT script 
COPY elt_script.py .

WORKDIR /app

# design 3am to implement the excutable file
RUN echo "0 3 * * * python /app/elt_script.py" | crontab - 

# Set the default command to run the ELT script
CMD ["python", "elt_script.py"]
