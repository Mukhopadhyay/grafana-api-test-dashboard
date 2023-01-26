-- Number of APIs per category

SELECT
  category, COUNT(category)
FROM
  api
GROUP BY
  category

-- Average elapsed per category

SELECT
	category, AVG(elapsed)
FROM
	api
INNER JOIN
	response ON response.api_id = api.id
GROUP BY
  category

-- Average elapsed per version

SELECT
	version, AVG(elapsed)
FROM
	api
INNER JOIN
	response ON response.api_id = api.id
GROUP BY
  version

-- Elapsed timeseries

SELECT
  response.created_at,
  response.elapsed as elapsed,
  api.category as metric
FROM
  response
INNER JOIN
  api ON api.id = response.api_id
LIMIT
  50
