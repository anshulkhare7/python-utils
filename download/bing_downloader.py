"""
Bing Image Downloader for Celebrity Face Portraits

This script downloads face portrait images of specified celebrities using the Bing Image Downloader Ext (forked version with more features).
It creates a structured dataset with separate folders for each person.

Requirements:
    - Python 3.12+
    - bing-image-downloader-ext package

Installation:
    pip install bing-image-downloader-ext

Usage:
    # Download with default personalities and count
    python bing_downloader.py
    
    # Download specific personalities
    python bing_downloader.py -p "Elon Musk, Barack Obama, Bill Gates"
    
    # Download with custom count
    python bing_downloader.py -c 10
    
    # Custom output directory
    python bing_downloader.py -o "my_dataset"
    
    # Combine all options
    python bing_downloader.py -p "Elon Musk, Barack Obama" -c 8 -o "celebrity_images"

Arguments:
    -p, --personality: Comma-separated list of personalities to download (optional)
    -c, --count: Number of images to download per person (default: 5)
    -o, --output: Output directory for dataset (default: "dataset")

Output Structure:
    dataset/
    ├── Elon_Musk/
    │   └── Elon Musk face portrait photo/
    │       ├── Image_0001.jpg
    │       ├── Image_0002.jpg
    │       └── ...
    ├── Donald_Trump/
    │   └── Donald Trump face portrait photo/
    │       ├── Image_0001.jpg
    │       └── ...
    └── ...

Default Personalities:
    - Elon Musk, Donald Trump, Narendra Modi, Tom Hanks, Tom Cruise
"""

import argparse
from bing_image_downloader import downloader


class BingImageDownloader:
    """Class for downloading celebrity face portrait images from Bing."""
    
    def __init__(self):
        self.default_people = ["Elon Musk", "Donald Trump", "Narendra Modi", "Tom Hanks", "Tom Cruise"]
        self.timeout = 60
        self.adult_filter_off = True
        self.force_replace = False
        self.verbose = True
    
    def download_images(self, people, count=5, output_dir="dataset"):
        """
        Download face portrait images for specified people.
        
        Args:
            people (list): List of personality names to download images for
            count (int): Number of images to download per person (default: 5)
            output_dir (str): Base output directory for the dataset (default: "dataset")
        """
        for person in people:
            print(f"Downloading {count} images for: {person}")
            try:
                downloader.download(
                    person + " face portrait photo",
                    limit=count,
                    output_dir=f"{output_dir}/{person.replace(' ', '_')}",
                    adult_filter_off=self.adult_filter_off,
                    force_replace=self.force_replace,
                    timeout=self.timeout,
                    verbose=self.verbose
                )
                print(f"✓ Successfully downloaded images for {person}")
            except Exception as e:
                print(f"✗ Error downloading images for {person}: {str(e)}")


def main():
    """Main function to handle command-line arguments and execute downloads."""
    parser = argparse.ArgumentParser(
        description="Download celebrity face portrait images from Bing",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python bing_downloader.py
  python bing_downloader.py -p "Elon Musk, Barack Obama"
  python bing_downloader.py -c 10
  python bing_downloader.py -o "my_dataset"
  python bing_downloader.py -p "Bill Gates" -c 8 -o "celebrity_images"
        """
    )
    
    parser.add_argument(
        "-p", "--personality",
        type=str,
        help="Comma-separated list of personalities to download (e.g., 'Elon Musk, Barack Obama')"
    )
    
    parser.add_argument(
        "-c", "--count",
        type=int,
        default=5,
        help="Number of images to download per person (default: 5)"
    )
    
    parser.add_argument(
        "-o", "--output",
        type=str,
        default="dataset",
        help="Output directory for dataset (default: 'dataset')"
    )
    
    args = parser.parse_args()
    
    # Initialize the downloader
    image_downloader = BingImageDownloader()
    
    # Parse personalities
    if args.personality:
        people = [name.strip() for name in args.personality.split(",")]
    else:
        people = image_downloader.default_people
    
    print(f"Starting download for {len(people)} personalities with {args.count} images each...")
    print(f"Personalities: {', '.join(people)}")
    print(f"Output directory: {args.output}")
    print("-" * 50)
    
    # Download images
    image_downloader.download_images(people, args.count, args.output)
    
    print("-" * 50)
    print("Download process completed!")


if __name__ == "__main__":
    main()