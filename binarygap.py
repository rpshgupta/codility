def solution(N):
  return len(max(bin(N)[2:].strip('0').strip('1').split('1')))
