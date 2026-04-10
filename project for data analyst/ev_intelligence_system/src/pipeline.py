import pandas as pd
from .ev_api import fetch_ev_data
from .youtube_api import fetch_videos, fetch_comments
from .storage import save_data
from .format_selector import choose_format


def run_pipeline():

    fmt = choose_format()

    # ev data
    ev_df = fetch_ev_data()
    save_data(ev_df, "ev_dataset", fmt)

    # youtube videos
    topics = ["Tesla review", "Nissan Leaf review", "EV comparison", "electric car range"]
    all_videos_dfs = []

    for topic in topics:
        try:
            videos_df = fetch_videos(query=topic)
            all_videos_dfs.append(videos_df)
        except Exception as e:
            print(f"Error fetching for {topic}: {e}")
            continue

    if all_videos_dfs:
        combined_videos_df = pd.concat(all_videos_dfs, ignore_index=True)
        if "video_id" in combined_videos_df.columns:
            combined_videos_df.drop_duplicates(subset=["video_id"], inplace=True)
    else:
        combined_videos_df = pd.DataFrame()

    save_data(combined_videos_df, "youtube_videos", fmt)

    # youtube comments
    all_comments = []

    if "video_id" in combined_videos_df.columns:
        for vid in combined_videos_df["video_id"]:
    
            try:
                comments = fetch_comments(vid)
                all_comments.extend(comments)
            except:
                continue

    comments_df = pd.DataFrame(all_comments)

    save_data(comments_df, "youtube_comments", fmt)

    print("\n Data Injection Completed")