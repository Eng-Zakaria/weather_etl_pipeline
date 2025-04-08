import argparse
from main import run_pipeline

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Weather Data Pipeline")
    parser.add_argument('--days', type=int, default=7,
                      help='Number of days of historical data to fetch')
    parser.add_argument('--lat', type=float, 
                      help='Latitude for location')
    parser.add_argument('--long', type=float,
                      help='Longitude for location')
    
    args = parser.parse_args()
    
    location = None
    if args.lat and args.long:
        location = {
            "latitude": args.lat,
            "longitude": args.long,
            "timezone": "auto"
        }
    
    run_pipeline(days=args.days)