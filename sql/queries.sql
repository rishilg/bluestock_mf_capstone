SELECT COUNT(*) AS total_funds
FROM fund_master;

SELECT
    scheme_name,
    aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

SELECT
    AVG(expense_ratio_pct) AS avg_expense_ratio
FROM fund_master;

SELECT
    scheme_name,
    sharpe_ratio
FROM scheme_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

SELECT
    sector,
    COUNT(*) AS holdings_count
FROM portfolio_holdings
GROUP BY sector
ORDER BY holdings_count DESC;