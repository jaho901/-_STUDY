
import sys
sys.stdin = open('12100.txt')

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

## 상하좌우로 이동했을 때의 변화를 모두 직접 4개로 나눠 함수 생성

## DFS로 4**5의 모든 경우를 탐색

## 백트래킹! 조건 하나 주는것!!

## 그때마다 최대값을 최신화

