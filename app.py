import streamlit as st
import yfinance as yf
import datetime 

st.header('Stock Analysis')
ticker_symbol=st.text_input('Enter the Stock Name','AAPL')

start_date=st.date_input("Start Date", value=datetime.date(2019, 7, 6))
end_date=st.date_input("End Date", value=datetime.date(2019, 7, 30))

data=yf.download(ticker_symbol,start=start_date,end=end_date)


st.subheader(f'Data for {ticker_symbol} from {start_date} to {end_date}')
st.write(data)

st.subheader('Line Chart for Close Attribute')
st.line_chart(data['Close'])
st.subheader('Bar Chart for Volume Attribute')
st.bar_chart(data['Volume'])