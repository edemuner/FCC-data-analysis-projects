import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = [1 if i > 25 else 0 for i in df['weight'] / ((df['height'] / 100) ** 2)]

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = [1 if i > 1 else 0 for i in df['cholesterol']]
df['gluc'] = [1 if i > 1 else 0 for i in df['gluc']]

# limpando os valores em que a pressão diastólica é maior que a pressão sistólica
df = df.loc[df['ap_lo'] <= df['ap_hi']]

# limpando os valores em que o quantil de altura é abaixo de 0.025
df = df.loc[df['height'] >= df['height'].quantile(0.025)]

# limpando os valores em que o quantil de altura é acima de 0.975
df = df.loc[df['height'] <= df['height'].quantile(0.975)]

# os mesmos ajustes no peso
df = df.loc[df['weight'] >= df['weight'].quantile(0.025)]

df = df.loc[df['weight'] >= df['weight'].quantile(0.975)]


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars='cardio',value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active','overweight'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    # df_cat = df_cat.groupby('cardio')

    # Draw the catplot with 'sns.catplot()'

    fig = sns.catplot(x="variable", col="cardio", data=df_cat, kind="count", hue="value")

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None



    # Set up the matplotlib figure
    fig, ax = None, None

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
