import pandas as pd
import plotly.express as px
import statsmodels.api as sm

def plot_graph(response):
    
    dframe = pd.DataFrame(response)
    dframe['Season'] = dframe['Season'].astype(str)
    print(dframe.head())

    full_trendline = sm.OLS(
        dframe['Ratings'], sm.add_constant(dframe['Episodes'])
    ).fit().fittedvalues

    fig = px.scatter(
        dframe, x='Episodes', y='Ratings', color='Season', size='Votes',
        trendline='ols'
    )
    fig.add_scatter(
        x=dframe['Episodes'], y=full_trendline, mode='lines', name='Trend'
    )

    fig.update_traces(marker_coloraxis=None)

    fig.update_layout(
        plot_bgcolor='#fff', margin=dict(l=5, r=5, b=5, t=5),
        xaxis_title_standoff=0.0,
        legend=dict(orientation='h', yanchor='bottom', y=-0.15)
    )
    fig.update_xaxes(
        rangemode='tozero',
        linewidth=2, linecolor='#aaa', mirror=True,
        ticks='inside', dtick=5
    )
    fig.update_yaxes(
        linewidth=2, linecolor='#aaa', mirror=True,
        gridwidth=1, gridcolor='#bbb'
    )

    return fig.to_json()