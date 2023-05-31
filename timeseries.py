from plotnine import *
import pandas as pd


def term_to_datetime(term):
    season, year = term.split(' ')
    if season == 'Spring':
        month = '01'
    elif season == 'Summer':
        month = '07'
    else:  # Fall
        month = '12'
    return pd.to_datetime(f'{year}-{month}-01')

def make_timeseries(data, selected_subjects):
    filtered_data = data[data['subject'].isin(selected_subjects)]

    # Convert filtered_data['subject'] to a Series if it's not already
    if isinstance(filtered_data['subject'], pd.DataFrame):
        filtered_data['subject'] = filtered_data['subject'].iloc[:, 0]

    counts = filtered_data.groupby(['term', 'subject']).size().reset_index(name='counts')
    counts['term_date'] = counts['term'].apply(term_to_datetime)
    counts['term'] = pd.Categorical(
        counts['term'],
        categories=counts.sort_values('term_date')['term'].unique(),
        ordered=True
    )

    # Plot data
    p = (
        ggplot(counts) +
        aes(x='term', y='counts', group='subject', color='subject') +
        geom_line() + 
        theme_bw() +
        theme(axis_text_x=element_text(angle=45))  # Rotate x-axis labels
    )

    
    return p

if __name__ == "__main__":
    data = pd.read_csv('processed_data/data.csv')
    #Choose only ALST and BIOL
    selected_subjects = ['ALST', 'BIOL']
    print(make_timeseries(data, selected_subjects))