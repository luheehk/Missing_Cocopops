import musicbrainzngs as mb

# MusicBrainz API
mb.set_useragent("MyMusicApp", "1.0", "arcshin87@gmail.com") 

artist_name = "Bing Crosby"
track_title = "White Christmas"

# 25 version, info of every version 
search_results = mb.search_recordings(artist=artist_name, recording=track_title)

if "recording-list" in search_results:
    recordings = search_results["recording-list"]

    for i, recording in enumerate(recordings):
        mbid = recording["id"]
        # can see the title to check it is the correct result
        title = recording["title"]

        release_list = recording.get("release-list", [])
        
        for release in release_list:
            release_date = release.get("date", "N/A")
            release_group_id = release.get("release-group", {}).get("id", "N/A")
            release_group_title = release.get("release-group", {}).get("title", "N/A")
            release_group_type = release.get("release-group", {}).get("type", "N/A")

            print(f"MBID: {mbid}")
            print(f"  버전 {i + 1}:")
            print(f"    제목: {title}")
            print(f"    릴리즈 날짜: {release_date}")
            print(f"    릴리스 그룹 ID: {release_group_id}")
            print(f"    릴리스 그룹 제목: {release_group_title}")
            print(f"    앨범 종류: {release_group_type}")
            print()

else:
    print("검색 결과가 없습니다.")