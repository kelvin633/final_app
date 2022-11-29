
# Import packages
import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns

st.set_page_config(layout='wide')


# Read Data 
df = pd.read_csv("international_matches.csv")
st.markdown("<h1 style='text-align: center; color: maroon;'>International Soccer Matches Data Explorer ⚽️🏆</h2>", unsafe_allow_html=True)

# Plot and Visualization
st.markdown("<h2 style='text-align: center; color: maroon;'>Data Visualization </h2>", unsafe_allow_html=True)

# Correlation # Seaborn Plot
if st.checkbox("Correlation Plot between Home / Away FIFA Rank and their scores "):
		st.write(sns.heatmap(df.corr(),annot=True))
		st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)

# Pie Chart
#if st.checkbox("Pie Plot"):
#		all_columns_names = df.columns.tolist()
#		if st.button("Generate Pie Plot"):
#			st.success("Generating A Pie Plot")
#			st.write(df.iloc[:,-1].value_counts().plot.pie(autopct="%1.1f%%"))
#			st.pyplot()

# Count Plot
if st.checkbox("Lets plot the value counts of your data"):
		st.text("Value Counts By Target")
		all_columns_names = df.columns.tolist()
		primary_col = st.selectbox("Primary Columm to Group By",all_columns_names)
		selected_columns_names = st.multiselect("Select Columns",all_columns_names)
		if st.button("Plot"):
			st.text("Generate Plot")
			if selected_columns_names:
				vc_plot = df.groupby(primary_col)[selected_columns_names].count()
			else:
				vc_plot = df.iloc[:,-1].value_counts()
			st.write(vc_plot.plot(kind="bar"))
			st.pyplot()

# Customizable Plot

st.markdown("<h2 style='text-align: center; color: maroon;'>Customize your Plot </h2>", unsafe_allow_html=True)
all_columns_names = df.columns.tolist()
type_of_plot = st.selectbox("Select Type of Plot : 1) Area Chart    2) Bar Chart    3) Line Chart   4) Histogram    5) Box Plot  6) KDE ",["area","bar","line","hist","box","kde"])
selected_columns_names = st.multiselect("  Select Columns To Plot :",all_columns_names)

if st.button("Generate Plot"):
		st.success("Generating Customizable Plot of {} for {}".format(type_of_plot,selected_columns_names))

		# Plot By Streamlit
		if type_of_plot == 'area':
			cust_data = df[selected_columns_names]
			st.area_chart(cust_data)

		elif type_of_plot == 'bar':
			cust_data = df[selected_columns_names]
			st.bar_chart(cust_data)

		elif type_of_plot == 'line':
			cust_data = df[selected_columns_names]
			st.line_chart(cust_data)

		# Custom Plot 
	#	elif type_of_plot:
	#		cust_plot= df[selected_columns_names].plot(kind=type_of_plot)
	#		st.write(cust_plot)
	#		st.pyplot()


# Sidebar 1 
st.sidebar.markdown("<h3 style='text-align: center; color: navy;'>About this Application </h2>", unsafe_allow_html=True)
st.sidebar.write('This application explores and analyze all international soccer matches played since the 90s. On top of that, the strength of each team is provided by incorporating actual FIFA rankings along with the places where each match was played and the final results.')
st.sidebar.write('Click here to display dataset')
if st.sidebar.checkbox("Show all Dataset"):
                  number = st.number_input("Number of Rows to View",5,15)
                  st.dataframe(df.head(number))

# Sidebar 2
st.sidebar.markdown("<h3 style='text-align: center; color: navy;'>My Dataset</h2>", unsafe_allow_html=True)

# Select Columns
if st.sidebar.checkbox("   Display by individual columns "):
		all_columns = df.columns.tolist()
		selected_columns = st.multiselect("Select",all_columns)
		new_df = df[selected_columns]
		st.dataframe(new_df)

# Show summary   
#if st.sidebar.checkbox("My Summary"):
#		st.write(df.describe().T)

# Sidebar 3
st.sidebar.markdown("<h3 style='text-align: center; color: navy;'>Column Names Description </h3>", unsafe_allow_html=True)
df2 = pd.read_csv("description.csv")
if st.sidebar.button("Show Column Names description"):
		st.write(df2)

# Sidebar 4
st.sidebar.markdown("<h3 style='text-align: center; color: navy;'>Dataset Datatypes </h2>", unsafe_allow_html=True)
st.sidebar.write('Click here to display our dataset datatypes')

# Show Datatypes
if st.sidebar.button("Data Types"):
		st.write(df.dtypes)


# SHOW DATASET  
 
 #side_1, side_2 = st.sidebar.columns(2)

 #with side_1:
  #  st.write('Show Dataset')


 #with side_2:
  #  st.write('column 2')

            #html_temp = """
        #<div style="background-color:LightSteelBlue;"><p>Click under Show Dataset to start</p></div>
        #"""
        #st.markdown(html_temp,unsafe_allow_html=True) 

