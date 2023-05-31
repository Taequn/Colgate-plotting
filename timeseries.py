from plotnine import *
import pandas as pd




def make_timeseries(data, selected_subjects):
    filtered_data = data[data['subject'].isin(selected_subjects)]

    # Convert filtered_data['subject'] to a Series if it's not already
    if isinstance(filtered_data['subject'], pd.DataFrame):
        filtered_data['subject'] = filtered_data['subject'].iloc[:, 0]

    counts = filtered_data.groupby(['term', 'subject']).size().reset_index(name='counts')

    p = (
        ggplot(counts, aes(x='term', y='counts', color='subject', group='subject')) +
        geom_line() +
        scale_x_discrete(limits=sorted(counts['term'].unique())) +
        theme_bw() +
        theme(axis_text_x=element_text(rotation=90, hjust=1))
    )
    return p

if __name__ == "__main__":
    data = pd.read_csv('processed_data/data.csv')
    #Choose only ALST and BIOL
    selected_subjects = ['ALST', 'BIOL']
    print(make_timeseries(data, selected_subjects))