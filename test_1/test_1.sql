SELECT name_client AS "Продавец", name_good AS "Товар", sum(kol) AS "Количество", 
(SELECT name_client FROM test_exercise.client WHERE client.id = goods.id_client_pok) AS "Покупатель"
FROM test_exercise.client
JOIN test_exercise.goods ON client.id = goods.id_client_pr GROUP BY client.name_client;