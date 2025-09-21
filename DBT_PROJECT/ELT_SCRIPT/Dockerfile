FROM python:3.12-slim

# Install PostgreSQL command-line tools
RUN apt-get update 
RUN apt-get uninstall -y postgresql-client-15 && apt-get install -y postgresql-client-17

# Copy the ELT script 
COPY elt_script.py .

# Set the default command to run the ELT script
CMD ["python", "elt_script.py"]
