CREATE TABLE fund_master (

    amfi_code INTEGER PRIMARY KEY,

    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    plan TEXT,

    launch_date DATE,

    benchmark TEXT,

    expense_ratio_pct REAL,
    exit_load_pct REAL,

    min_sip_amount INTEGER,
    min_lumpsum_amount INTEGER,

    fund_manager TEXT,
    risk_category TEXT,

    sebi_category_code TEXT
);

CREATE TABLE nav_history (

    amfi_code INTEGER,

    date DATE,

    nav REAL,

    FOREIGN KEY (amfi_code)
    REFERENCES fund_master(amfi_code)

);

CREATE TABLE scheme_performance (

    amfi_code INTEGER PRIMARY KEY,

    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    plan TEXT,

    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,

    benchmark_3yr_pct REAL,

    alpha REAL,
    beta REAL,

    sharpe_ratio REAL,
    sortino_ratio REAL,

    std_dev_ann_pct REAL,
    max_drawdown_pct REAL,

    aum_crore REAL,

    expense_ratio_pct REAL,

    morningstar_rating INTEGER,

    risk_grade TEXT,

    FOREIGN KEY (amfi_code)
    REFERENCES fund_master(amfi_code)

);

CREATE TABLE portfolio_holdings (

    amfi_code INTEGER,

    stock_symbol TEXT,
    stock_name TEXT,

    sector TEXT,

    weight_pct REAL,

    market_value_cr REAL,

    current_price_inr REAL,

    portfolio_date DATE,

    FOREIGN KEY (amfi_code)
    REFERENCES fund_master(amfi_code)

);

CREATE TABLE benchmark_indices (

    date DATE,

    index_name TEXT,

    close_value REAL

);