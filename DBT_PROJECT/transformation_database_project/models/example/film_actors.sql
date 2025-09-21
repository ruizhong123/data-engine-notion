{{ config(materialized='table') }}

select * from {{ source('destination_db', 'film_actors') }}
