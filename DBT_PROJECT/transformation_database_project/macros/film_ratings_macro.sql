-- 使用處理巨量資料
{% macro generate_film_ratings() %}

with films_with_rattings as (
    select 
        film_id,
        title,
        release_date,
        price,
        rating,
        user_rating,
        {% generate_rating() %}
    from {{ ref('films') }}
),

films_with_actor as (
    select
        f.film_id,
        f.title,
        STRING_AGG(a.actor_name, ', ') as actors
    FROM {{ ref('films') }} f
    LEFT JOIN {{ ref('film_actors') }} fa ON f.film_id = fa.film_id
    LEFT JOIN {{ ref('actors') }} a ON fa.actor_id = a.actor_id
    GROUP BY f.film_id, f.title
)

select 
    fwf.*,
    fwa.actors
from films_with_rattings fwf
left join films_with_actor fwa on fwf.film_id = fwa.film_id


{% endmacro %}
