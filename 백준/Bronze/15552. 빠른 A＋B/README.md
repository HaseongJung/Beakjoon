# [Bronze IV] 빠른 A+B - 15552 

[문제 링크](https://www.acmicpc.net/problem/15552) 

### 성능 요약

메모리: 31256 KB, 시간: 1188 ms

### 분류

구현, 사칙연산, 수학

### 문제 설명

<p>본격적으로 for문 문제를 풀기 전에 주의해야 할 점이 있다. 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.</p>

<p>C++을 사용하고 있고 <code>cin</code>/<code>cout</code>을 사용하고자 한다면, <code>cin.tie(NULL)</code>과 <code>sync_with_stdio(false)</code>를 둘 다 적용해 주고, <code>endl</code> 대신 개행문자(<code>\n</code>)를 쓰자. 단, 이렇게 하면 더 이상 <code>scanf</code>/<code>printf</code>/<code>puts</code>/<code>getchar</code>/<code>putchar</code> 등 C의 입출력 방식을 사용하면 안 된다.</p>

<p>Java를 사용하고 있다면, <code>Scanner</code>와 <code>System.out.println</code> 대신 <code>BufferedReader</code>와 <code>BufferedWriter</code>를 사용할 수 있다. <code>BufferedWriter.flush</code>는 맨 마지막에 한 번만 하면 된다.</p>

<p>Python을 사용하고 있다면, <code>input</code> 대신 <code>sys.stdin.readline</code>을 사용할 수 있다. 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 <code>.rstrip()</code>을 추가로 해 주는 것이 좋다.</p>

<p>또한 입력과 출력 스트림은 별개이므로, 테스트케이스를 전부 입력받아서 저장한 뒤 전부 출력할 필요는 없다. 테스트케이스를 하나 받은 뒤 하나 출력해도 된다.</p>

<p>자세한 설명 및 다른 언어의 경우는 <a href="http://www.acmicpc.net/board/view/22716">이 글</a>에 설명되어 있다.</p>

<p><a href="http://www.acmicpc.net/blog/view/55">이 블로그 글</a>에서 BOJ의 기타 여러 가지 팁을 볼 수 있다.</p>

### 입력 

 <p>첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다. 다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.</p>

### 출력 

 <p>각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.</p>

