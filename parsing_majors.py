import pandas as pd

if __name__ == "__main__":
    # Read the data (assuming it's a csv file)
    df = pd.read_csv('processed_data/data.csv')

    # Extract year from the term
    df['year'] = df['term'].str.extract('(\d+)').astype(int)

    # Initialize an empty dataframe to store the result
    result_df = pd.DataFrame(columns=['year', 'subject', 'majors_enrolled'])

    # Iterate over years and subjects
    for (year, subject), group in df.groupby(['year', 'subject']):
        # Filter rows where 'course_title' contains 'Senior'
        senior_courses = group[group['course_title'].str.contains('Senior')]
        
        # Sum the enrollments of senior courses
        majors_enrolled = senior_courses['enrollment'].sum()

        # Append the result to the result dataframe
        new_row = pd.DataFrame({'year': [year], 'subject': [subject], 'majors_enrolled': [majors_enrolled]})
        result_df = pd.concat([result_df, new_row])

    # Convert 'year' and 'majors_enrolled' to int as they are originally numbers
    result_df['year'] = result_df['year'].astype(int)
    result_df['majors_enrolled'] = result_df['majors_enrolled'].astype(int)

    result_df.to_csv('processed_data/enrolled_majors.csv', index=False)