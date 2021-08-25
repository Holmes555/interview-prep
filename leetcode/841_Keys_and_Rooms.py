from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        room_ids = {i for i in range(1, len(rooms))}
        q = [*rooms[0]]

        while q:
            key = q.pop()
            if key in room_ids:
                room_ids.remove(key)
            else:
                continue
            q.extend(rooms[key])

        return not room_ids
