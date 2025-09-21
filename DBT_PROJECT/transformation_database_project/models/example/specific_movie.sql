-- 從 films 表中挑選 電影標題為 "Dunkirk" 的電影
{% set film_title = "Dunkirk" %}

SELECT *
FROM {{ ref('films')}}
where title = '{{ film_title }}'
