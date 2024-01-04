#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pip', 'install yfinance')


# In[19]:


import yfinance as yf


# In[33]:


import pandas as pd
import matplotlib.pyplot as plt


# In[44]:


indx_fund = '^RUT'
strt_date = '2023-01-01'
end_date = '2023-12-31'
indx_data = yf.download(indx_fund, start=strt_date, end=end_date)
indx_data = indx_data[['Open', 'High', 'Low', 'Close']]

indx_returns = indx_data['Close'].pct_change()
indx_returns = indx_returns.dropna()

#csv_file_path = r'C:\Users\deshw\Downloads\stocks\indx_data.csv'
#indx_data.to_csv(csv_file_path)


# In[30]:


# Replace 'AAPL' with the desired stock symbol
S1 = 'AAPL'
S2 = 'MSFT'
S3 = 'TCS.NS'
S4 = 'BA'
S5 = 'BABA'
S6 = 'BSX'
S7 = 'ABNB'
S8 = 'ADES'
S9 = 'F'
S10 = 'TM'
S11 = 'JNJ'
S12 = 'JPM'
S13 = 'AEP'
S14 = 'ABAT'
S15 = 'RCL'
S16 = 'CVNA'
S17 = 'CAR'
S18 = 'ZM'
S19 = 'DOW'
S20 = 'DO'
# Define the time period for which you want to get the data
start_date = '2023-01-01'
end_date = '2023-12-31'

# Download historical data
S1_data = yf.download(S1, start=start_date, end=end_date)
S1_data = S1_data[['Open', 'High', 'Low', 'Close']]
S2_data = yf.download(S2, start=start_date, end=end_date)
S2_data = S2_data[['Open', 'High', 'Low', 'Close']]
S3_data = yf.download(S3, start=start_date, end=end_date)
S3_data = S3_data[['Open', 'High', 'Low', 'Close']]
S4_data = yf.download(S4, start=start_date, end=end_date)
S4_data = S4_data[['Open', 'High', 'Low', 'Close']]
S5_data = yf.download(S5, start=start_date, end=end_date)
S5_data = S5_data[['Open', 'High', 'Low', 'Close']]
S6_data = yf.download(S6, start=start_date, end=end_date)
S6_data = S6_data[['Open', 'High', 'Low', 'Close']]
S7_data = yf.download(S7, start=start_date, end=end_date)
S7_data = S7_data[['Open', 'High', 'Low', 'Close']]
S8_data = yf.download(S8, start=start_date, end=end_date)
S8_data = S8_data[['Open', 'High', 'Low', 'Close']]
S9_data = yf.download(S9, start=start_date, end=end_date)
S9_data = S9_data[['Open', 'High', 'Low', 'Close']]
S10_data = yf.download(S10, start=start_date, end=end_date)
S10_data = S10_data[['Open', 'High', 'Low', 'Close']]
S11_data = yf.download(S11, start=start_date, end=end_date)
S11_data = S11_data[['Open', 'High', 'Low', 'Close']]
S12_data = yf.download(S12, start=start_date, end=end_date)
S12_data = S12_data[['Open', 'High', 'Low', 'Close']]
S13_data = yf.download(S13, start=start_date, end=end_date)
S13_data = S13_data[['Open', 'High', 'Low', 'Close']]
S14_data = yf.download(S14, start=start_date, end=end_date)
S14_data = S14_data[['Open', 'High', 'Low', 'Close']]
S15_data = yf.download(S15, start=start_date, end=end_date)
S15_data = S15_data[['Open', 'High', 'Low', 'Close']]
S16_data = yf.download(S16, start=start_date, end=end_date)
S16_data = S16_data[['Open', 'High', 'Low', 'Close']]
S17_data = yf.download(S17, start=start_date, end=end_date)
S17_data = S17_data[['Open', 'High', 'Low', 'Close']]
S18_data = yf.download(S18, start=start_date, end=end_date)
S18_data = S18_data[['Open', 'High', 'Low', 'Close']]
S19_data = yf.download(S19, start=start_date, end=end_date)
S19_data = S19_data[['Open', 'High', 'Low', 'Close']]
S20_data = yf.download(S20, start=start_date, end=end_date)
S20_data = S20_data[['Open', 'High', 'Low', 'Close']]

# Print the first few rows of the data
#print(stock_data.head())


# In[35]:


stock_returns = S1_data['Close'].pct_change()

# Plot the returns
plt.figure(figsize=(10, 6))
plt.plot(stock_returns, label=f'{S1} Returns')
plt.plot(indx_returns, label=f'{indx_fund} Returns')
plt.legend()
plt.title('Stock vs Index Fund Performance')
plt.xlabel('Date')
plt.ylabel('Daily Returns')
plt.show()


# In[36]:


stock_returns = S1_data['Close'].pct_change()

# Plot the returns
plt.figure(figsize=(10, 6))
plt.plot(stock_returns, label=f'{S2} Returns')
plt.plot(indx_returns, label=f'{indx_fund} Returns')
plt.legend()
plt.title('Stock vs Index Fund Performance')
plt.xlabel('Date')
plt.ylabel('Daily Returns')
plt.show()


# In[37]:


stock_returns = S1_data['Close'].pct_change()

# Plot the returns
plt.figure(figsize=(10, 6))
plt.plot(stock_returns, label=f'{S10} Returns')
plt.plot(indx_returns, label=f'{indx_fund} Returns')
plt.legend()
plt.title('Stock vs Index Fund Performance')
plt.xlabel('Date')
plt.ylabel('Daily Returns')
plt.show()


# In[39]:


stock_avg_return = stock_returns.mean()
index_avg_return = indx_returns.mean()

stock_volatility = stock_returns.std()
index_volatility = indx_returns.std()

# Calculate Sharpe ratio (risk-adjusted return)
stock_sharpe_ratio = stock_avg_return / stock_volatility
index_sharpe_ratio = index_avg_return / index_volatility

print(f'{S10} Average Return: {stock_avg_return:.2%}')
print(f'{indx_fund} Average Return: {index_avg_return:.2%}')
print(f'{S10} Volatility: {stock_volatility:.2%}')
print(f'{indx_fund} Volatility: {index_volatility:.2%}')
print(f'{S10} Sharpe Ratio: {stock_sharpe_ratio:.4f}')
print(f'{indx_fund} Sharpe Ratio: {index_sharpe_ratio:.4f}')


# In[38]:


Income_statement1 = yf.Ticker(S1).financials
Income_statement2 = yf.Ticker(S2).financials
Income_statement3 = yf.Ticker(S3).financials
Income_statement4 = yf.Ticker(S4).financials
Income_statement5 = yf.Ticker(S5).financials
Income_statement6 = yf.Ticker(S6).financials
Income_statement7 = yf.Ticker(S7).financials
Income_statement8 = yf.Ticker(S8).financials
Income_statement9 = yf.Ticker(S9).financials
Income_statement10 = yf.Ticker(S10).financials
Income_statement11 = yf.Ticker(S11).financials
Income_statement12 = yf.Ticker(S12).financials
Income_statement13 = yf.Ticker(S13).financials
Income_statement14 = yf.Ticker(S14).financials
Income_statement15 = yf.Ticker(S15).financials
Income_statement16 = yf.Ticker(S16).financials
Income_statement17 = yf.Ticker(S17).financials
Income_statement18 = yf.Ticker(S18).financials
Income_statement19 = yf.Ticker(S19).financials
Income_statement20 = yf.Ticker(S20).financials


# In[27]:


Balance_sheet1 = yf.Ticker(S1).balance_sheet
Balance_sheet2 = yf.Ticker(S2).balance_sheet
Balance_sheet3 = yf.Ticker(S3).balance_sheet
Balance_sheet4 = yf.Ticker(S4).balance_sheet
Balance_sheet5 = yf.Ticker(S5).balance_sheet
Balance_sheet6 = yf.Ticker(S6).balance_sheet
Balance_sheet7 = yf.Ticker(S7).balance_sheet
Balance_sheet8 = yf.Ticker(S8).balance_sheet
Balance_sheet9 = yf.Ticker(S9).balance_sheet
Balance_sheet10 = yf.Ticker(S10).balance_sheet
Balance_sheet11 = yf.Ticker(S11).balance_sheet
Balance_sheet12 = yf.Ticker(S12).balance_sheet
Balance_sheet13 = yf.Ticker(S13).balance_sheet
Balance_sheet14 = yf.Ticker(S14).balance_sheet
Balance_sheet15 = yf.Ticker(S15).balance_sheet
Balance_sheet16 = yf.Ticker(S16).balance_sheet
Balance_sheet17 = yf.Ticker(S17).balance_sheet
Balance_sheet18 = yf.Ticker(S18).balance_sheet
Balance_sheet19 = yf.Ticker(S19).balance_sheet
Balance_sheet20 = yf.Ticker(S20).balance_sheet


# In[ ]:


chashflow1 = yf.Ticker(S1).cashflow
chashflow2 = yf.Ticker(S2).cashflow
chashflow3 = yf.Ticker(S3).cashflow
chashflow4 = yf.Ticker(S4).cashflow
chashflow5 = yf.Ticker(S5).cashflow
chashflow6 = yf.Ticker(S6).cashflow
chashflow7 = yf.Ticker(S7).cashflow
chashflow8 = yf.Ticker(S8).cashflow
chashflow9 = yf.Ticker(S9).cashflow
chashflow10 = yf.Ticker(S10).cashflow
chashflow11 = yf.Ticker(S11).cashflow
chashflow12 = yf.Ticker(S12).cashflow
chashflow13 = yf.Ticker(S13).cashflow
chashflow14 = yf.Ticker(S14).cashflow
chashflow15 = yf.Ticker(S15).cashflow
chashflow16 = yf.Ticker(S16).cashflow
chashflow17 = yf.Ticker(S17).cashflow
chashflow18 = yf.Ticker(S18).cashflow
chashflow19 = yf.Ticker(S19).cashflow
chashflow20 = yf.Ticker(S20).cashflow


# In[32]:


# Calculate daily percentage change
S1_data['Daily_Price_Change'] = S1_data['Close'].pct_change() * 100

# Drop the NaN value in the first row (resulting from the percentage change calculation)
S1_data = S1_data.dropna()

S2_data['Daily_Price_Change'] = S2_data['Close'].pct_change() * 100
S2_data = S2_data.dropna()
S3_data['Daily_Price_Change'] = S3_data['Close'].pct_change() * 100
S3_data = S3_data.dropna()
S4_data['Daily_Price_Change'] = S4_data['Close'].pct_change() * 100
S4_data = S4_data.dropna()
S5_data['Daily_Price_Change'] = S5_data['Close'].pct_change() * 100
S5_data = S5_data.dropna()
S6_data['Daily_Price_Change'] = S6_data['Close'].pct_change() * 100
S6_data = S6_data.dropna()
S7_data['Daily_Price_Change'] = S7_data['Close'].pct_change() * 100
S7_data = S7_data.dropna()
S8_data['Daily_Price_Change'] = S8_data['Close'].pct_change() * 100
S8_data = S8_data.dropna()
S9_data['Daily_Price_Change'] = S9_data['Close'].pct_change() * 100
S9_data = S9_data.dropna()
S10_data['Daily_Price_Change'] = S10_data['Close'].pct_change() * 100
S10_data = S10_data.dropna()
S11_data['Daily_Price_Change'] = S11_data['Close'].pct_change() * 100
S11_data = S11_data.dropna()
S12_data['Daily_Price_Change'] = S12_data['Close'].pct_change() * 100
S12_data = S12_data.dropna()
S13_data['Daily_Price_Change'] = S13_data['Close'].pct_change() * 100
S13_data = S13_data.dropna()
S14_data['Daily_Price_Change'] = S14_data['Close'].pct_change() * 100
S14_data = S14_data.dropna()
S15_data['Daily_Price_Change'] = S15_data['Close'].pct_change() * 100
S15_data = S15_data.dropna()
S16_data['Daily_Price_Change'] = S16_data['Close'].pct_change() * 100
S16_data = S16_data.dropna()
S17_data['Daily_Price_Change'] = S17_data['Close'].pct_change() * 100
S17_data = S17_data.dropna()
S18_data['Daily_Price_Change'] = S18_data['Close'].pct_change() * 100
S18_data = S18_data.dropna()
S19_data['Daily_Price_Change'] = S19_data['Close'].pct_change() * 100
S19_data = S19_data.dropna()
S20_data['Daily_Price_Change'] = S20_data['Close'].pct_change() * 100
S20_data = S20_data.dropna()


# In[ ]:




