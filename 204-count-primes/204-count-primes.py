class Solution:
    def countPrimes(self, n: int) -> int:
        sieve = [True] * n
        # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
        m = int(n ** 0.5)
        for i in range(2, m + 1):
            if sieve[i] == True:           # i가 소수인 경우
                for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                    sieve[j] = False

        return len([i for i in range(2, n) if sieve[i] == True])

            