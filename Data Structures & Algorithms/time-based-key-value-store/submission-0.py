class TimeMap:

    def __init__(self):
        self.res = defaultdict(dict) 

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        self.res[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.res:
            return ""

        for t in range(timestamp, -1, -1):

            if t in self.res[key]:

                return self.res[key][t]

        return ""
        
