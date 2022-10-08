ivans_record_in_seconds = float(input())
distance_in_meters = float(input())
needed_time_in_seconds_for_one_meter = float(input())

needed_distance = distance_in_meters * needed_time_in_seconds_for_one_meter
for_every_15m = (distance_in_meters // 15) * 12.5
total_time_world_record = needed_distance + for_every_15m
needed_time_to_beat_the_world_records = total_time_world_record - ivans_record_in_seconds

if total_time_world_record < ivans_record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time_world_record:.02f} seconds.")
else:
    print(f"No, he failed! He was {needed_time_to_beat_the_world_records:.02f} seconds slower.")