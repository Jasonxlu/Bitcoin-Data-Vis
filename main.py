import pymssql
import sys
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Project 04

servername = '*******.database.windows.net'
login = '*******'
pwd = '********'
dbname = 'Blockchain'

print('**Trying to connect to ' + dbname + ' in Microsoft Azure cloud...')
print()

try:
    dbConn = pymssql.connect(server=servername,
                             user=login,
                             password=pwd,
                             database=dbname)
    print("**Connected, Welcome to the " + dbname + " database!")
except Exception as err:
    print("Error:", err)
    print("failed to connect :-(")
    sys.exit()
finally:
    print()


# Project 05
# Visualizations

plt.style.use('_mpl-gallery')

cmd = input("Please enter a command ('1' for two statistic comparison, '2' for stacked comparison, '3' for time range selection, 'list' for tables, 'x' to exit): ")
dbCursor = dbConn.cursor()

while cmd != 'x':
    # Side by Side Time Series
    if cmd == "1":
        statistics = {"Hash_rate": "Hash_Rate", "Cost_percentage": "Percentage", "Transaction_cost": "Cost", "Market_price": "Price", "Median_transaction_time": "Time", "Miners_revenue": "Revenue",
                      "Num_transactions": "Transactions", "Total_coins": "Num_Coins", "Total_fees": "Fees", "Total_transactions": "Total_Transactions", "Trade_vol": "Volume", "Unique_addresses": "Addresses"}

        data1 = input("Please enter 1st table name: ")
        data2 = input("Please enter 2nd table name: ")

        try:
            # First Table
            datesql = "Select Date from " + data1 + ";"
            sql = "Select " + statistics[data1] + " from " + data1 + ";"
            dbCursor.execute(datesql)
            dates = dbCursor.fetchall()
            dbCursor.execute(sql)
            row = dbCursor.fetchall()

            x1 = []
            y1 = []

            for i in dates:
                x1.append(i[0])
            for i in row:
                y1.append(i[0])

            # Second Table
            datesql = "Select Date from " + data2 + ";"
            sql = "Select " + statistics[data2] + " from " + data2 + ";"
            dbCursor.execute(datesql)
            dates = dbCursor.fetchall()
            dbCursor.execute(sql)
            row = dbCursor.fetchall()

            x2 = []
            y2 = []

            for i in dates:
                x2.append(i[0])
            for i in row:
                y2.append(i[0])

            plt.rcParams['figure.figsize'] = [10, 7]

            figure, axis = plt.subplots(1, 2)

            figure.subplots_adjust(hspace=0, left=0.14,
                                   right=0.90, bottom=0.15, top=0.90)

            # For Data Table
            axis[0].plot_date(x1, y1, 'b')
            axis[0].set_title(data1)
            axis[0].set(xlabel="Date", ylabel=statistics[data1])
            axis[0].tick_params(axis='x', labelrotation=45)

            # For Data Table 2
            axis[1].plot_date(x2, y2, 'r')
            axis[1].set_title(data2)
            plt.ylabel(statistics[data2])
            plt.xlabel("Date")
            plt.xticks(rotation=70)

            plt.yticks()
            plt.show()
        except:
            print("Invalid table name, try again...")

    # Stacked Time Series
    elif cmd == "2":

        sql = """Select Market_price.Date, Transaction_cost.Cost, Median_transaction_time.Time, Miners_revenue.Revenue, Num_transactions.Transactions, Total_coins.Num_Coins, Total_fees.Fees, Trade_vol.Volume, Unique_addresses.Addresses, Cost_percentage.[Percent]
        from Market_price inner join Hash_rate on Market_price.Date = Hash_rate.Date 
        inner join Transaction_cost on Market_price.Date = Transaction_cost.Date
        inner join Cost_percentage on Market_price.Date = Cost_percentage.Date
        inner join Median_transaction_time on Market_price.Date = Median_transaction_time.Date
        inner join Miners_revenue on Market_price.Date = Miners_revenue.Date
        inner join Num_transactions on Market_price.Date = Num_transactions.Date
        inner join Total_coins on Market_price.Date = Total_coins.Date
        inner join Total_fees on Market_price.Date = Total_fees.Date
        inner join Trade_vol on Market_price.Date = Trade_vol.Date
        inner join Unique_addresses on Market_price.Date = Unique_addresses.Date;"""
        dbCursor.execute(sql)
        row = dbCursor.fetchall()

        # make data
        dates = []
        costs = []
        times = []
        revenues = []
        transactions = []
        num_coins = []
        fees = []
        # total_transactions = []
        volumes = []
        addresses = []
        percentages = []

        for i in row:
            dates.append(i[0])
            costs.append(i[1])
            times.append(i[2])
            revenues.append(i[3])
            transactions.append(i[4])
            num_coins.append(i[5])
            fees.append(i[6])
            # total_transactions.append(i[7])
            volumes.append(i[7])
            addresses.append(i[8])
            percentages.append(i[9])

        y = np.vstack([costs, times, revenues, transactions, num_coins,
                      fees, volumes, addresses, percentages])

        plt.rcParams['figure.figsize'] = [10, 7]

        fig, ax = plt.subplots()
        color_map = ["#9b59b6", "#e74c3c", "#34495e", "#2ecc71",
                     "red", "blue", "orange", "purple"]
        sp = ax.stackplot(dates, y, colors=color_map)

        vol = ["Transaction Cost", "Median Transaction Time", "Miners Revenue", "Num Transactions", "Total Coins",
               "Total Fees", "Trade Volume", "Unique Addresses", "Cost Percentage"]

        ax.legend(sp, vol, loc='upper left')

        plt.subplots_adjust(hspace=0, left=0.14,
                            right=0.90, bottom=0.15, top=0.90)
        plt.ylabel('Values')
        plt.xlabel('Dates')
        plt.xticks(rotation=70)
        plt.yticks()
        plt.title("Stacked Time Series")
        plt.show()

    # Market Price Time Range
    elif cmd == "3":

        start = input("Please enter start date (Earliest 1/2/2009): ")
        end = input("Please enter end date (Latest 11/28/2022): ")

        sql = "Select Date, Price from Market_price where Date >= " + \
            "'" + start + "'" + " and Date <= " + "'" + end + "'" + ";"
        dbCursor.execute(sql)
        row = dbCursor.fetchall()

        x = []
        y = []
        for i in row:
            x.append(i[0])
            y.append(i[1])

        plt.rcParams['figure.figsize'] = [10, 7]

        fig, ax = plt.subplots()

        sp = ax.stackplot(x, y, colors="yellow")
        plt.subplots_adjust(hspace=0, left=0.14,
                            right=0.90, bottom=0.15, top=0.90)
        plt.ylabel('Market Price')
        plt.xlabel('Dates')
        plt.xticks(rotation=70)
        plt.yticks()
        plt.title("Market Price")
        plt.show()

    # List Tables
    elif cmd == "list":
        sql = """SELECT name FROM sys.tables;"""
        dbCursor.execute(sql)
        row = dbCursor.fetchall()
        for i in row:
            print(i[0])

    else:
        print("**Error, unknown command, try again...")

    print()
    cmd = input("Please enter a command (1-6, x to exit): ")


print()
print('**Done')
dbConn.close()
