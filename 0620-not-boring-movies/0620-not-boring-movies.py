import pandas as pd
def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    filtered_cinema=cinema[(cinema['id']% 2!=0)&(cinema['description']!='boring')]
    result = filtered_cinema.sort_values(by='rating',ascending=False)
    return result