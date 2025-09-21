{{ config(materialized='table') }}
select * from {{ source('destination_db', 'actors') }}

