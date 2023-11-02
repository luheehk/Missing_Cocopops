import musicbrainzngs as mb

mb.set_useragent("MyMusicApp", "1.0", "arcshin87@gmail.com")  

artist_name = "Bill Withers"
track_title = "Ain't No Sunshine"

search_results = mb.search_recordings(artist=artist_name, recording=track_title)

# save as a txt. file
output_filename = "music_results.txt"

with open(output_filename, "w", encoding="utf-8") as output_file:
    if "recording-list" in search_results:
        recordings = search_results["recording-list"]

        for i, recording in enumerate(recordings):
            mbid = recording["id"]
            title = recording["title"]

            release_list = recording.get("release-list", [])
            
            for release in release_list:
                release_date = release.get("date", "N/A")
                release_group_id = release.get("release-group", {}).get("id", "N/A")
                release_group_title = release.get("release-group", {}).get("title", "N/A")
                release_group_type = release.get("release-group", {}).get("type", "N/A")

                output_file.write(f"MBID: {mbid}\n")
                output_file.write(f"  버전 {i + 1}:\n")
                output_file.write(f"    제목: {title}\n")
                output_file.write(f"    릴리즈 날짜: {release_date}\n")
                output_file.write(f"    릴리스 그룹 ID: {release_group_id}\n")
                output_file.write(f"    릴리스 그룹 제목: {release_group_title}\n")
                output_file.write(f"    앨범 종류: {release_group_type}\n\n")

    else:
        output_file.write("검색 결과가 없습니다.")

print(f"결과가 {output_filename} 파일에 저장되었습니다.")
