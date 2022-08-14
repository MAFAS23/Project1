
import streamlit as st
import requests
import json


st.markdown('<iframe src="https://embed.lottiefiles.com/animation/89118"></iframe>',
            unsafe_allow_html=True)

# membuat kolom

kol1, kol2, kol3 = st.columns(3)

with kol1:
    currency1 = ['EUR', 'USD', 'GBP', 'AUD', 'IDR', 'CAD', 'CNY', 'COP', 'XCP', 'EGP', 'HKD', 'INR',
                 'IRR', 'JPY', 'KRW', 'MYR', 'NZD', 'PKR', 'PHP', 'SAR', 'CHF', 'TWD', 'TRY', 'AED', 'VND']
    curr1 = st.selectbox('Currency 1', currency1)

with kol2:
    if curr1 == 'EUR':
        st.markdown(
            '<iframe src="https://embed.lottiefiles.com/animation/43343"></iframe>', unsafe_allow_html=True)
    elif curr1 == 'USD':
        st.markdown(
            '<iframe src="https://embed.lottiefiles.com/animation/43342"></iframe>', unsafe_allow_html=True)
    else:
        st.markdown(
            '<iframe src="https://embed.lottiefiles.com/animation/80143"></iframe>', unsafe_allow_html=True)
with kol3:
    currency2 = ['USD', 'EUR', 'GBP', 'AUD', 'IDR', 'CAD', 'CNY', 'COP', 'XCP', 'EGP', 'HKD', 'INR',
                 'IRR', 'JPY', 'KRW', 'MYR', 'NZD', 'PKR', 'PHP', 'SAR', 'CHF', 'TWD', 'TRY', 'AED', 'VND']
    curr2 = st.selectbox('Currency 2', currency2)


# API


url = f'https://free.currconv.com/api/v7/convert?q={curr1}_{curr2},{curr2}_{curr1}&compact=ultra&apiKey=998fd01dfa204fecebe2'

re = requests.get(url)
re = re.json()


one_two = re[f'{curr1}_{curr2}']
two_one = re[f'{curr2}_{curr1}']


kol1, kol2 = st.columns(2)

with kol1:
    st.write(f'1{curr1} to {curr2}')
    st.success(one_two)
with kol2:
    st.write(f'1{curr2} to {curr1}')
    formatted = "{:,.6f}".format(two_one)
    st.success(formatted)


kol1, kol2 = st.columns(2)

with kol1:
    amount1 = st.number_input(f'{curr1} to {curr2}', key='1')

with kol2:
    amount2 = st.number_input(f'{curr2} to {curr1}', key='2')

kol1, kol2 = st.columns(2)

with kol1:
    st.text("Converted Amount")
    st.success(amount1*one_two)
with kol2:
    st.text("Converted Amount")
    st.success(amount2/one_two)
st.markdown('<style> body{text-align:center;} </style>',
            unsafe_allow_html=True)
