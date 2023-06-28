QUESTAO_1 = """WITH 
ntr_transactions AS (
-- Note: 0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday, 5 = Saturday, 6 = Sunday.
SELECT DISTINCT SentDate, MONTH(SentDate) as _month,  DAY(SentDate) AS month_day, WEEKDAY(SentDate) week_day, 
       AddressOrigin AS address_origin, 1 as n_t 
FROM raw_transactions_table rtt 
WHERE status in ('Confirmed')
),

ntr_agg_transactions AS (
SELECT _month, month_day, week_day, address_origin, sum(n_t) as n_transactions
FROM ntr_transactions 
WHERE _month = 1
group by 1,2,3,4
)

-- CARTEIRA COM MAIOR TRANSACACOES
SELECT address_origin, SUM(n_transactions) as sum_n_transactions
FROM ntr_agg_transactions GROUP BY 1 ORDER BY 2 DESC LIMIT 1"""

QUESTAO_2 = """WITH 
ntr_transactions AS (
-- Note: 0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday, 5 = Saturday, 6 = Sunday.
SELECT DISTINCT SentDate, MONTH(SentDate) as _month,  DAY(SentDate) AS month_day, WEEKDAY(SentDate) week_day, 
       AddressOrigin AS address_origin, 1 as n_t 
FROM raw_transactions_table rtt 
WHERE status in ('Confirmed')
),

ntr_agg_transactions AS (
SELECT _month, month_day, week_day, address_origin, sum(n_t) as n_transactions
FROM ntr_transactions 
WHERE _month = 1
group by 1,2,3,4
)

-- DIA COM MAIOR TRANSACOES
SELECT month_day, SUM(n_transactions) as sum_n_transactions
FROM ntr_agg_transactions GROUP BY 1 ORDER BY 2 DESC LIMIT 1
"""

QUESTAO_3 = """WITH 
ntr_transactions AS (
-- Note: 0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday, 5 = Saturday, 6 = Sunday.
SELECT DISTINCT SentDate, MONTH(SentDate) as _month,  DAY(SentDate) AS month_day, WEEKDAY(SentDate) week_day, 
       AddressOrigin AS address_origin, 1 as n_t 
FROM raw_transactions_table rtt 
WHERE status in ('Confirmed')
),

ntr_agg_transactions AS (
SELECT _month, month_day, week_day, address_origin, sum(n_t) as n_transactions
FROM ntr_transactions 
WHERE _month = 1
group by 1,2,3,4
),
-- DIA SEMANA AVG TRANS REALIZADA
ntr_agg AS (
SELECT month_day, week_day, SUM(n_transactions) as nn_transactions
FROM ntr_agg_transactions
GROUP BY 1,2 ORDER BY 1) 

SELECT week_day, AVG(nn_transactions)
FROM ntr_agg 
GROUP BY 1 ORDER BY 2 DESC LIMIT 1
"""

QUESTAO_4 = """SELECT month(SentDate) AS _month, status, count(1)
FROM raw_transactions_table rtt 
GROUP BY 1,2
"""

QUESTAO_5 = """WITH 
ntr_rtt_clean AS(
	SELECT DISTINCT IdTransaction as id, AddressOrigin as origin, AddressDestination AS destination, 
	TotalSent, MONTH(SentDate) as _month,
	-- Correção do campo TotalSent retiro da , e cast
	CAST(REPLACE(TotalSent,',','') AS FLOAT) as amount,
	SentDate 
	FROM raw_transactions_table rtt 
	WHERE Status = 'Confirmed'
	ORDER BY id
),
ntr_amount_origin AS (
	SELECT origin, SUM(amount) AS amount
	FROM ntr_rtt_clean
	GROUP BY 1
),

ntr_amount_destination AS (
	SELECT destination, SUM(amount) AS amount
	FROM ntr_rtt_clean
	GROUP BY 1
),

ntr_amount_balance AS (
	SELECT nao.origin as wallet, (nad.amount - nao.amount) as balance
	FROM ntr_amount_origin nao 
	LEFT JOIN ntr_amount_destination nad
	ON nao.origin = nad.destination
)
	
SELECT wallet, balance FROM ntr_amount_balance ORDER BY balance DESC LIMIT 1
"""

QUESTAO_6 = """
WITH 
ntr_rtt_clean AS(
	SELECT DISTINCT IdTransaction as id, AddressOrigin as address, 
	TotalSent, MONTH(SentDate) as _month,
	-- Correção do campo TotalSent retiro da , e cast
	CAST(REPLACE(TotalSent,',','') AS FLOAT) as amount,
	SentDate 
	FROM raw_transactions_table rtt 
	WHERE Status = 'Confirmed'
	ORDER BY id
),

ntr_amount_fee AS (
 SELECT ntc.id, ntc.address, ntc.amount, rtf.`fee-percentage`, 
 		ntc.amount * (rtf.`fee-percentage`/100) as tax_amount, ntc._month, 
 	    CONCAT(ntc.id, ntc._month) as id_month
 FROM ntr_rtt_clean ntc 
 LEFT JOIN raw_transactions_fee rtf 
 ON ntc.amount >= rtf.`range-start`  
 AND ntc.amount <= rtf.`range-end` 
 ORDER BY id
) 


-- 4
SELECT 'q4' as questao, 
       'media' as v1, 
       TRUNCATE(AVG(tax_amount),2) as v2
FROM ntr_amount_fee

UNION ALL

-- 3
(SELECT 'q3' as questao,
	id as v1, 
	tax_amount as v2
FROM ntr_amount_fee
ORDER BY tax_amount DESC LIMIT 1)

UNION ALL

-- 2
(
SELECT 'q2' as questao, 
	address as v1, 
	TRUNCATE(SUM(tax_amount),2) as v2
FROM ntr_amount_fee
WHERE _month = 2
GROUP BY 1 ORDER BY 2 DESC LIMIT 1 
)

UNION ALL
-- 1
(
SELECT 'q1' as questao,
	address as v1, 
	TRUNCATE(SUM(tax_amount),2) as v2
FROM ntr_amount_fee
WHERE _month = 1
GROUP BY 1 ORDER BY 2 DESC LIMIT 1
)
"""