#!/usr/bin/env python
# coding: utf-8

# In[20]:


#import libraries 
import yfinance as yf
import pandas as pd
import numpy as np 


# In[21]:


stocks = ["AMZN", "MSFT", "GOOGL"]
stocks_data = yf.download(stocks, start="2010-01-01", end="2020-12-31") #download stock data from yahoo finance
close_price = stocks_data["Close"] #show "Close" price of the stock data 
display(close_price)


# In[22]:


stocks_daily_returns = close_price.pct_change() #calculate daily returns of each stock 
stocks_daily_returns = stocks_daily_returns.dropna() #drop all "NaN" values from the data 
display(stocks_daily_returns)


# In[23]:


#create #(50% Amazon, 50% Microsoft), (50% Amazon, 50% Google), (50% Microsoft, 50% Google) [portfolio]
stocks_portfolio = pd.DataFrame({
    "Amazon-Microsoft": 0.5 * stocks_daily_returns["AMZN"] + 0.5 * stocks_daily_returns["MSFT"],
    "Amazon-Google": 0.5 * stocks_daily_returns["AMZN"] + 0.5 * stocks_daily_returns["GOOGL"],
    "Microsoft-Google": 0.5 * stocks_daily_returns["MSFT"] + 0.5 * stocks_daily_returns["GOOGL"]
})

display(stocks_portfolio) 


# In[24]:


#CV || (std/mean)% for each portfolio 
amazon_microsoft_cv = stocks_portfolio["Amazon-Microsoft"].std() / stocks_portfolio["Amazon-Microsoft"].mean()
amazon_google_cv = stocks_portfolio["Amazon-Google"].std() / stocks_portfolio["Amazon-Google"].mean()
microsoft_google_cv = stocks_portfolio["Microsoft-Google"].std() / stocks_portfolio["Microsoft-Google"].mean()

#create list of CV values and varibale names
cv_values = [amazon_microsoft_cv, amazon_google_cv, microsoft_google_cv]
portfolio_names = ["Amazon-Microsoft", "Amazon-Google", "Microsoft-Google"]

#find the minimum CV value and its variable name
min_cv_value = min(cv_values)
min_cv_index = cv_values.index(min_cv_value)
min_cv = portfolio_names[min_cv_index]

print(f"Coefficient Variation of Amazon-Microsoft Portfolio: {amazon_microsoft_cv:.2f}")
print(f"Coefficient Variation of Amazon-Google Portfolio: {amazon_google_cv:.2f}")
print(f"Coefficient Variation of Microsoft-Google Portfolio: {microsoft_google_cv:.2f}")
print(f"The most effective CV portfolio is '{min_cv}' with a value of {min_cv_value:.2f}") 

#you can use precision for round off  instead of an f string .2f


# In[25]:


#Sharpe Ratio || (Rx – Rf) / StdDev Rx for each portfolio 

risk_free_rate = 0.01 / 360 #assuming the risk-free returns is 1% per year (360 days)

amazon_microsoft_sharpe = (stocks_portfolio["Amazon-Microsoft"].mean() - risk_free_rate) / stocks_portfolio["Amazon-Microsoft"].std()
amazon_google_sharpe = (stocks_portfolio["Amazon-Google"].mean() - risk_free_rate) / stocks_portfolio["Amazon-Google"].std()
microsoft_google_sharpe = (stocks_portfolio["Microsoft-Google"].mean() - risk_free_rate) / stocks_portfolio["Microsoft-Google"].std()

#create a list of sharpe values and varibale names
sharpe_values = [amazon_microsoft_sharpe, amazon_google_sharpe, microsoft_google_sharpe]
portfolio_names_sharpe = ["Amazon-Microsoft", "Amazon-Google", "Microsoft-Google"]

#find the maximum sharpe value and its variable name
max_sharpe_value = max(sharpe_values)
max_sharpe_index = sharpe_values.index(max_sharpe_value)
max_sharpe = portfolio_names_sharpe[max_sharpe_index]

print(f"Sharpe Ratio of Amazon-Microsoft Portfolio: {amazon_microsoft_sharpe:.2f}")
print(f"Sharpe Ratio of Amazon-Google Portfolio: {amazon_google_sharpe:.2f}")
print(f"Sharpe Ratio of Microsoft-Google Portfolio: {microsoft_google_sharpe:.2f}")
print(f"The best portfolio based on Sharpe Ratio is '{max_sharpe}' with a value of {max_sharpe_value:.2f}") 


# In[ ]:




