# ARS and MEP stock performance
This project aims to show the performance of stock bought at argentinian brokers with argentinian pesos **AR$**. Currently, it is only working with cedears (stock and etf).

The program will get the **MEP** (USD) value at the date you bought the stock, the current **MEP** value and the current stock value. With those elements, it will compare the value of the stock when you bought it, with the current value of it, both in **MEP**, so we can get rid of the inflation problem.

## How to run it

To run it, you only need to complete the   `my_current_stock.xlsx` file with your cedears. The only 3 necessarty things to complete are the ticker, the unit price (in **AR$**) and the date when you bought them. You can complete the other columns but they are not going to be used.

Then, just run the performance.py file (be sure to close the `my_current_stock.xlsx` file before running). A file called `my_performance.xlsx` will be created and there you will be able to see your performance in **AR$** and **MEP** for any of your stock.