menu = [
    {
        "type": "list",
        "name": "action",
        "message": "Spotify downloader manager",
        "choices": [
            {"name": "Download from uri/url", "value": "download_playlist"},
            {"name": "Manage my playlists", "value": "manage_playlists"},
            {"name": "Quit", "value": "quit"},
            {
                "name": "Current download path",
                "disabled": "download_base_path",
            },
            {
                "name": "You can change the download path changing",
                "disabled": "hades.py > download_base_path",
            },
            ],
    },
]