from pytube import YouTube
import os


def download_video(link, user_resolution):
    '''Download video from YouTube. Enter the YouTube link and wanted resolution.'''

    # YouTube link
    video_link = YouTube(link)

    # Video title
    title = video_link.title
    print(f"Your YouTube video title: {title}")

    # Filters
    #mp4_filter = video_link.streams.filter(file_extension="mp4")
    #print(mp4_filter)

    # Add user's resolution a "p" to detect resolution
    user_resolution = user_resolution + "p"

    try:
        # Get the resolutions of the video
        #video_filter = video_link.streams.filter(res=f"{user_resolution}")
        print(f"Your resolution is: {user_resolution}")
        
        # Highest resolution of the video
        highest_resolution = video_link.streams.get_highest_resolution().resolution
        print(f"This video's highest resolution is {highest_resolution}")

        # Option to raise the user's resolution
        change_resolution = input("Do you want keep your resolution? [Y/N]> ")

        if change_resolution.lower() == "y":

            # Keep user's resolution
            user_resolution == user_resolution

        else:

            # Equal highest resolution with user's input
            if highest_resolution == "720p":
                user_resolution = highest_resolution

    except:
        print("Your video could not be downloaded")

    # Get audio only
    #video_link.streams.get_audio_only()

    print(f"Final resolution: {user_resolution}")
    print("Downloading...")

    # Download
    download = video_link.streams.filter(res=f"{user_resolution}").first().download()

    rename_video(download)

    # Get current working directory
    path = os.getcwd()

    print(f"\nYour video has been download!\nAnd has been saved in your current directory {path}")


def rename_video(download):
    '''Rename your downloaded video'''

    # User input to choice if he want rename or not his video
    rename_yt = input("Do you want rename your video? [Y/N]> ")

    if rename_yt.lower() == "y":
        # Video's new name
        new_name = input("Enter your new video's name: ")
        # Rename video file with OS
        os.rename(download, new_name + ".mp4")

    else:
        # End function
        return


download_video("link", "resolution")
