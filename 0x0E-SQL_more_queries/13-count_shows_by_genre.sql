-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT genres.genre AS `genre`, COUNT(*) AS `number_of_shows`
FROM `tv_show_genres`
JOIN genres ON tv_show_genres.`genre_id` = genres.`id`
GROUP BY genres.`genre`
ORDER BY `number_of_shows` DESC;
