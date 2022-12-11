CREATE TABLE Currency (
    Date date NOT NULL,
    Currency nvarchar(8) NOT NULL,
    PRIMARY KEY (Date)
);

CREATE TABLE Transaction_cost (
    Date date NOT NULL,
    Cost float NOT NULL,
    PRIMARY KEY (Date),
    CONSTRAINT FK_TCDate FOREIGN KEY (Date) 
    REFERENCES Currency(Date)
);

CREATE TABLE Cost_percentage (
    Date date NOT NULL,
    Percent float NOT NULL,
    PRIMARY KEY (Date),
    CONSTRAINT FK_CPDate FOREIGN KEY (Date) 
    REFERENCES Currency(Date),
    CONSTRAINT CP_Percent CHECK (Percent>=0 AND Percent<=100)
);

CREATE TABLE Hash_rate (
    Date date NOT NULL,
    Hash_Rate float NOT NULL,
    PRIMARY KEY (Date),
    CONSTRAINT FK_HRDate FOREIGN KEY (Date) 
    REFERENCES Currency(Date)
);

CREATE TABLE Market_price (
    Date date NOT NULL,
    Price float NOT NULL,
    PRIMARY KEY (Date),
    CONSTRAINT FK_MPDate FOREIGN KEY (Date) 
    REFERENCES Currency(Date)
);

CREATE TABLE Median_transaction_time (
    Date date NOT NULL,
    Time float NOT NULL,
    PRIMARY KEY (Date),
    CONSTRAINT FK_MTTDate FOREIGN KEY (Date) 
    REFERENCES Currency(Date)
);

CREATE TABLE Miners_revenue (
    Date date NOT NULL,
    Revenue float NOT NULL,
    PRIMARY KEY (Date),
    CONSTRAINT FK_MRDate FOREIGN KEY (Date) 
    REFERENCES Currency(Date)
);

CREATE TABLE Num_transactions (
    Date date NOT NULL,
    Transactions int NOT NULL,
    PRIMARY KEY (Date),
    CONSTRAINT FK_NTDate FOREIGN KEY (Date) 
    REFERENCES Currency(Date)
);

CREATE TABLE Total_coins (
    Date date NOT NULL,
    Num_Coins float NOT NULL,
    PRIMARY KEY (Date),
    CONSTRAINT FK_CDate FOREIGN KEY (Date) 
    REFERENCES Currency(Date)
);

CREATE TABLE Total_fees (
    Date date NOT NULL,
    Fees float NOT NULL,
    PRIMARY KEY (Date),
    CONSTRAINT FK_TFDate FOREIGN KEY (Date) 
    REFERENCES Currency(Date)
);

CREATE TABLE Total_transactions (
    Date date NOT NULL,
    Total_Transactions int NOT NULL,
    PRIMARY KEY (Date),
    CONSTRAINT FK_TTDate FOREIGN KEY (Date) 
    REFERENCES Currency(Date)
);

CREATE TABLE Trade_vol (
    Date date NOT NULL,
    Volume float NOT NULL,
    PRIMARY KEY (Date),
    CONSTRAINT FK_TVDate FOREIGN KEY (Date) 
    REFERENCES Currency(Date)
);

CREATE TABLE Unique_addresses (
    Date date NOT NULL,
    Addresses int NOT NULL,
    PRIMARY KEY (Date),
    CONSTRAINT FK_UADate FOREIGN KEY (Date) 
    REFERENCES Currency(Date)
);

CREATE UNIQUE INDEX Currency_Date
ON Currency (Date);