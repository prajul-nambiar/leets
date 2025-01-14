import time

class TokenBucket:
    def __init__(self, capacity, fill_rate):
        self.capacity = capacity       # Maximum number of tokens the bucket can hold
        self.fill_rate = fill_rate     # Rate at which tokens are added (tokens/second)
        self.last_time = time.time()   # Last time we checked the token count
        self.token = capacity          # Current token count, start with a full bucket

    def limit_calc(self, token=1):
        now = time.time()
        # Calculate how many tokens have been added since the last check
        time_diff = now - self.last_time
        self.token = min(self.capacity, self.token + time_diff * self.fill_rate )
        self.last_time = now

        #check if we have enough tokens for this request
        if self.token >= token:
            self.token -= token
            return True
        return False

#Usage Exmaple

limiter = TokenBucket(capacity=10,fill_rate=1)  # 10 tokens, refill 1 token per second

for _ in range(15):
    print(limiter.limit_calc())                 # Will print True for the first 10 requests, then False
    time.sleep(0.1)                             # Wait a bit between requests

time.sleep(5)                                   # Wait for 5 sec to the tokens to reloaded into bucket and then check
print(limiter.limit_calc())

