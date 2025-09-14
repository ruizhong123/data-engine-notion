-- 根據 電影資料中的評分來轉換評級 並且製作出一個表格出來
with films_with_ratting as (
    SELECT 
        film_id,
        title,
        release_year,
        price,
        rating,
        user_rating,
        CASE 
            when user_rating >= 4.5  then 'Excellent'
            when user_rating >= 4.0  then 'Good'
            when user_rating >= 3.0  then 'Average'
            else 'Poor'
        end as rating_category        
    FROM{{ ref('films') }}
    ),

film_with_actor as (
    SELECT
        f.film_id,
        f.title,
        STRING_AGG(a.actor_name, ', ') as actors
    FROM {{ref('films')}} f
    LEFT JOIN {{ref('film_actors')}} fa ON f.film_id = fa.film_id
    LEFT JOIN {{ref('actors')}} a ON fa.actor_id = a.actor_id
    GROUP BY f.film_id, f.title
)


SELECT
    fwf.*,
    fwa.actors
FROM films_with_ratting fwf
LEFT JOIN film_with_actor fwa ON fwf.film_id = fwa.film_id







