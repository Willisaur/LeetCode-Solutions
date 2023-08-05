import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    authors = views[views["author_id"] == views["viewer_id"]]
    unique_authors = pd.DataFrame(authors["author_id"].unique())
    print(unique_authors)
    unique_authors.columns = ["id"]
    unique_authors = unique_authors.sort_values("id")

    return unique_authors
