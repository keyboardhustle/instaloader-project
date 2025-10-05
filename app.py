#!/usr/bin/env python3
"""
Instaloader Application
A simple Instagram downloader using Instaloader
"""

import instaloader
import sys
import os

def main():
    """Main function to run the Instaloader application"""
    
    # Create an instance of Instaloader
    L = instaloader.Instaloader(
        dirname_pattern='/app/downloads/{target}',
        download_videos=True,
        download_video_thumbnails=True,
        download_geotags=True,
        download_comments=True,
        save_metadata=True,
        compress_json=False
    )
    
    print("Instaloader Application Started")
    print("================================")
    
    # Get target profile from environment variable or use default
    target = os.getenv('INSTAGRAM_TARGET', 'instagram')
    
    print(f"Target profile: {target}")
    
    try:
        # Download profile
        print(f"Downloading profile: {target}")
        L.download_profile(target, profile_pic_only=False)
        print("Download completed successfully!")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
