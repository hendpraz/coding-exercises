class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        def thirdOfEl(elem):
            return elem[2]
        
        def secondOfEl(elem):
            return elem[1]
        
        i = 0
        for trip in trips:
            trip.append(i)
            i += 1
        
        trips_by_start = sorted(trips, key=secondOfEl)
        trips_by_end = sorted(trips, key=thirdOfEl, reverse=True)
        
        print(trips_by_start)
        print(trips_by_end)
        
        current_passanger = 0
        is_valid = True
        for trip in trips_by_start:
            trip_passanger = trip[0]
            trip_start_loc = trip[1]
            trip_end_loc = trip[2]
            trip_key = trip[3]
            
            if len(trips_by_end) != 0:
                last_idx = len(trips_by_end) - 1
                closest_droppoint_loc = trips_by_end[last_idx][2]
                closest_droppoint_passanger = trips_by_end[last_idx][0]
                closest_droppoint_key = trips_by_end[last_idx][3]

                while (trip_start_loc >= closest_droppoint_loc) and (trip_key != closest_droppoint_key):
                    current_passanger -= closest_droppoint_passanger
                    trips_by_end.pop()
                    
                    if len(trips_by_end) == 0:
                        break
                        
                    last_idx = len(trips_by_end) - 1
                    closest_droppoint_loc = trips_by_end[last_idx][2]
                    closest_droppoint_passanger = trips_by_end[last_idx][0]
                    closest_droppoint_key = trips_by_end[last_idx][3]
                    
            current_passanger += trip_passanger
            is_valid = (current_passanger <= capacity)
            
            if not is_valid:
                break
        
        return is_valid
