import bar_chart_race as bcr
import pandas as pd

df_clean=pd.read_excel('net_worth_timeseries_cleaned.xlsx')
df_clean.rename({'Column1':'Year'},axis=1,inplace=True)
df_clean.set_index('Year',inplace=True)



# --- STEP 7: Generate Bar Chart Race ---
bcr.bar_chart_race(
    df=df_clean,
    filename='net_worth_barchart_race.mp4',
    orientation='h',
    sort='desc',
    n_bars=10,
    fixed_order=False,
    fixed_max=True,
    steps_per_period=200,
    interpolate_period=True,
    label_bars=True,
    bar_size=0.95,
    period_label={'x': .99, 'y': .1, 'ha': 'right', 'va': 'center'},
    period_fmt='Year: {x:.0f}',
    period_summary_func=lambda v, r: {'x': .99, 'y': .15,
        's': f'Total Net Worth: ₹{int(v.sum()):,} Cr', 'ha': 'right', 'size': 8},
    perpendicular_bar_func='mean',
    figsize=(6, 4),
    dpi=144,
    cmap='dark12',
    title='Top 10 Indian Companies by Net Worth (Year-wise)',
    bar_label_size=7,
    tick_label_size=7,
    scale='linear',
    bar_kwargs={'alpha': .8},
    filter_column_colors=True
)

print("✅ Bar chart race video saved as net_worth_barchart_race.mp4")
