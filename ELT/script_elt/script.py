import time 
import subprocess

def wait_for_postgres(host,max_retries=10, delay_seconds=5):    
    
    retries = 0
    
    while retries<max_retries:
    
        try:
            result = subprocess.run(
                ['pg_isready','-h',host],
                check=True,
                capture_output=True,
                text=True
            )
            if "accepting connections" in result.stdout:
                print(f'Successfully connected to Postgressql at {host}')
                time.sleep(10)
                return True
            
            retries += 1
        
        except subprocess.CalledProcessError as e:
            print(f'Error connecting to Postgres at {e}')
            retries += 1
            print(f'Retrying in {delay_seconds} seconds...({retries}/{max_retries})')
            time.sleep(delay_seconds)    
    return False
        
if not wait_for_postgres(host='source_postgres'):
    print('Failed to connect to Postgres after maximum retries. Exiting...')
    exit(1)
    
print('Start The ELT Process ...')

source_config = {
    'dbname': 'source_db',
    'user': 'postgres',
    'password':'secret',
    'host': 'source_postgres'
}

destination_config = {
    'dbname': 'destination_db',
    'user': 'postgres',
    'password':'secret',
    'host': 'destination_postgres'
}



# dunmp the source database into a sql files
dump_command = [
    'pg_dump',
    '-h', source_config['host'],
    '-U', source_config['user'],
    '-d', source_config['dbname'],
    '-f', 'data_dump.sql',
    '-w'
]

subprocess_env = dict(PGPASSWORD=source_config['password'])

subprocess.run(dump_command,env=subprocess_env,check=True)


# load thre sql file into the destination database 
load_command = [
    'psql',
    '-h', destination_config['host'],
    '-U', destination_config['user'],
    '-d', destination_config['dbname'],
    '-a','-f', 'data_dump.sql',
]

subprocess_env = dict(PGPASSWORD=destination_config['password'])

subprocess.run(load_command, env=subprocess_env,check=True)

print('Ending ELT Script ...')

