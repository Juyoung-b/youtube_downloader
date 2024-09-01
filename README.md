# youtube_downloader

# Requirements

```
pip install pytubefix
```

git clone first

Download a single video:
```
python youtube_downloader.py <YouTube URL> [output path]
```
Download audio only:

```
python youtube_downloader.py <YouTube URL> [output path] --audio-only
```

Download video with captions:
```
python youtube_downloader.py <YouTube URL> [output path] --download-captions
```

Download a playlist:

```
python youtube_downloader.py <Playlist URL> [output path] --playlist
```

Download a playlist as audio only:

```
python youtube_downloader.py <Playlist URL> [output path] --playlist --audio-only
```
