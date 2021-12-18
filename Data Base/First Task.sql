/*
First Task
*/

SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'singleSales';

/*
N 1
*/

SELECT TOP(10)
    *
FROM
    distributor.singleSales
WHERE
    branchName = 'Москва'
    AND dateId BETWEEN '2011-01-01' AND '2011-01-31'

/*
N 2
*/

SELECT TOP(10)
    fullname,
    salesRub,
    sales,
    itemId
FROM
    distributor.singleSales

/*
N 3
*/

SELECT
    min(salesRub) AS min,
    max(salesRub) AS max
FROM
    distributor.singleSales

/*
N 4
*/

SELECT
    fullname,
    salesRub,
    month(dateId)
FROM
    distributor.singleSales
WHERE
    sales = (
        SELECT
            MAX(sales)
        FROM
            distributor.singleSales
        WHERE
            month(dateId) = 2
    )

/*
N 5
*/

SELECT
    COUNT(DISTINCT checkId) AS checks
FROM
    distributor.sales

/*
N 6
*/

SELECT
    COUNT(DISTINCT checkId) AS checks
FROM
    distributor.sales
WHERE
    salesRub >= 10000

/*
N 8
*/

SELECT
    *
FROM
    [distributor].[singleSales]
WHERE
    branchName = 'Москва'
    AND dateId BETWEEN '2011-01-01' AND '2011-01-31'
    AND fullname IS NOT NULL
    AND companyName IS NOT NULL
ORDER BY
    salesRub DESC

/*
N 9-11
*/


SELECT
    *
FROM
    [distributor].[singleSales]
WHERE
    branchName = 'Москва' 
    AND dateId BETWEEN '2011-06-01' AND '2011-06-30'
    AND companyName IS NOT NULL
    AND category = 'Сантехника'
ORDER BY
    sales DESC


SELECT
    *
FROM
    [distributor].[singleSales]
WHERE
    dateId BETWEEN '2011-02-01' AND '2011-08-01'
    AND companyName IS NOT NULL
    AND fullname IS NOT NULL
    AND brand = 'Roca'
ORDER BY
    fullname

SELECT
    *
FROM
    [distributor].[singleSales]
WHERE
    dateId BETWEEN '2011-02-01' AND '2011-09-30'
    AND fullname IS NOT NULL
    AND category LIKE '%Обои%'
    AND sales BETWEEN 5 AND 10
ORDER BY
    fullname ASC,
    salesRub DESC

SELECT TOP(1)
    *
FROM
    [distributor].[singleSales]
WHERE
    branchName = 'Самара'
    AND fullname IS NOT NULL
    AND companyName IS NOT NULL
ORDER BY
    salesRub DESC

/*
**N 12**
*/

SELECT TOP(10)
    *
FROM
    distributor.singleSales
WHERE
    region='Самарская область'
    AND salesRub = (
        SELECT
            MAX(salesRub)
        FROM
            distributor.singleSales
        WHERE
            region = 'Самарская область'
    )

/*
**N 13**
*/

SELECT
    [checkId] AS [Номер чека],
    [itemId] AS [Инд. номер товара],
    [branchName] AS [Город],
    [region] AS [Регион],
    sizeBranch AS [Размер склада],
    fullname AS [Менеджер],
    companyName AS [Компания],
    itemName AS [Наименование товара],
    brand AS [Брэнд],
    category AS [Категория],
    dateId AS [Дата],
    sales AS [Количество продаж],
    salesRub AS [Сумма продаж]
FROM
    [distributor].[singleSales]
WHERE
    category = 'Напольные покрытия'
    AND sales > 5
    AND fullname IS NOT NULL
    AND brand = 'Praktik'

/*
**N 14**
*/

SELECT
    COUNT(DISTINCT fullname) AS [quantity]
FROM
    [distributor].[singleSales]
WHERE
    fullname LIKE '%ва%'
    OR fullname LIKE '%ов%'
    AND sales BETWEEN 5 AND 10
    AND branchName = 'Новосибирск'

-- Или по таблице менеджеров (при условии окончания фамилии на -ов, -ва):

SELECT
    COUNT(DISTINCT surname) [quantity]
FROM
    [distributor].[salesManager]
WHERE
    surname LIKE '%ва'
    OR surname LIKE '%ов'

/*
**N 15**
*/

SELECT
    COUNT(DISTINCT companyName) AS [quantity]
FROM
    [distributor].[singleSales]
WHERE
    sales > 10
    AND companyName LIKE 'ООО%'
    AND region = 'Самарская область'
    AND dateId > '2011-09-01'

/*
**N 16**
*/

SELECT
    fullname,
    COUNT(DISTINCT companyName) AS [Количество_клиентов]
FROM
    [distributor].[singleSales]
WHERE
    sales > 10
    AND branchName = 'Москва'
    AND fullname IS NOT NULL
    AND companyName IS NOT NULL
GROUP BY
    fullname
ORDER BY
    Количество_клиентов DESC

/*
**N 17**
*/

SELECT
    branchName,
    COUNT(DISTINCT companyName) / 
    COUNT(DISTINCT fullname) AS [Среднее_количество_клиентов_на менеджера_филиала]
FROM
    [distributor].[singleSales]
WHERE
    fullname IS NOT NULL
GROUP BY
    branchName

/*
**N 18**
*/

with temp(fullname, numberOfCompanies) as (
    SELECT
        fullname,
        count(distinct companyName)
    FROM
        distributor.singleSales
    WHERE
        branchName = 'Москва'
        and fullname IS NOT NULL
    GROUP BY
        fullname
)
SELECT
    avg(numberOfCompanies)
FROM
    temp

SELECT
    avg()
    companyName,
    COUNT(DISTINCT companyName)
FROM
    distributor.singleSales
WHERE
    fullname IS NOT NULL
    branchName = 'Москва'
GROUP BY
    fullname

/*markdown
**N 19**
*/

SELECT
    COUNT(sales.checkId),
    branch.branchName
FROM
    distributor.sales
INNER JOIN
    distributor.branch
    ON (sales.branchId = branch.branchId)
GROUP BY
    sales.branchId, branch.branchName

/*
**N 20.1**
*/

WITH temp(managerId, checksSold) AS (
    SELECT
        salesManagerId, COUNT(sales.checkId)
    FROM
        distributor.sales
    WHERE
        salesManagerId IS NOT NULL
    GROUP BY
        salesManagerId
)
SELECT
    managerId,
    surname,
    [names],
    checksSold
FROM
    temp
INNER JOIN
    distributor.salesManager
    ON (salesManager.salesManagerId = temp.managerId)
WHERE
    checksSold = (
        SELECT
            max(checksSold)
        FROM
            temp
    )

/*
**N 20.2**
*/

WITH temp(branch, fullname, checks) AS (
    SELECT
        branchName
        fullname,
        COUNT(checkId)
    FROM
        distributor.singleSales
    WHERE
        fullname IS NOT NULL
    GROUP BY
        branchName,
        fullname
)
SELECT
    branch,
    fullname,
    checks
FROM
    temp
WHERE
    checks = (
        SELECT
            max(checks)
        FROM
            temp
        GROUP BY
            branch
    )

