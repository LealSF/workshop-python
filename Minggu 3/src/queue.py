from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")    # Menambhakan item Terry pada urutan akhir
queue.append("Graham")   # Menambhakan item Graham pada urutan akhir
queue.popleft()          # The first to arrive now leaves Eric

queue.popleft()          # The second to arrive now leaves John

queue                    # Remaining queue in order of arrival