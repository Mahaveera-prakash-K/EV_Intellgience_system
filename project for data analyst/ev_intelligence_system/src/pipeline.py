from .ev_api import fetch_ev_data
from .format_selector import choose_format
from .Storage import save_dataset

def run_pipeline():
    print("Starting EV Dataset Pipeline...")
    
    # Fetch Data 
    df = fetch_ev_data()
    
    # Ask user for format
    fmt = choose_format()
    
    # Save Data
    save_dataset(df, fmt)
    
    print("Pipeline finished.")
