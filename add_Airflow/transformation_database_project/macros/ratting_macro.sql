-- 設下定義式專為 macro 中 film_rating.sql 使用
{% generate_rating() %}
        Case 
            when user_rating >= 4.5 then 'Excellent'
            when user_rating >= 4 then 'Good'
            when user_rating >= 3 then 'Average'
            else 'Poor'
        end as rating_category
{% endmacro %}
