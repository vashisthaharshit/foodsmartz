import pandas as pd

def popularity_based(count=10):
    df = pd.read_csv('C:\\Users\\harshit.vashistha\\Desktop\\Recommendation project\\foodsmartz\\recommendation\\dataset\\recommendation_data')

    df.drop(columns=['Unnamed: 0'], inplace=True)
    df.drop_duplicates(subset=['name', 'location'], inplace=True)
    popular_rest = df[df['votes'] > 250].sort_values('rate', ascending=False)
    popular_rest = popular_rest[popular_rest['rate'] > 3.5].head(count)
    return popular_rest
