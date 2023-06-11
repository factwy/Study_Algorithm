# Daily challenge in 2023.06.11
# 1146. Snapshot Array
class SnapshotArray:
    def __init__(self, length: int):
        self.arr = []
        for _ in range(length):
            self.arr.append({})
        self.id = 0
    def set(self, index: int, val: int) -> None:
        self.arr[index][self.id] = val
        return None
    def snap(self) -> int:
        self.id += 1
        return self.id - 1      
    def get(self, index: int, snap_id: int) -> int:
        key = set(self.arr[index].keys())
        for i in range(snap_id, -1, -1):
            if i in key:
                return self.arr[index][i]
        return 0
