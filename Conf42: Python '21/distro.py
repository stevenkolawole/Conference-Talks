import streamlit as st
import numpy as np 

st.title('Distribution Tester')
st.write('Pick a distribution from the list and we shall draw \
	the line chart from a random sample from the distribution')

keys = ['Normal','Uniform']
dist_key = st.selectbox('Which distribution do you want to plot?', keys)
if dist_key == 'Normal':
	nums = np.random.randn(1000)
elif dist_key == 'Uniform':
	nums = np.array([np.random.randint(100) for i in range(1000)])

# Display user
st.line_chart(nums)