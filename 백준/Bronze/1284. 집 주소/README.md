# [Bronze III] 집 주소 - 1284 

[문제 링크](https://www.acmicpc.net/problem/1284) 

### 성능 요약

메모리: 31256 KB, 시간: 40 ms

### 분류

사칙연산, 구현, 수학

### 문제 설명

<p>재석이는 대문에 붙이는 (주소를 나타내는) 호수판 제작업체의 직원이다. 고객에게 전달할 호수판은 숫자와 숫자 사이 그리고 왼쪽 오른쪽으로 적당히 여백이 들어가 줘야하고 숫자마다 차지하는 간격이 조금씩 상이하다. 다행이도 규칙은 매우 간단하다. </p>

<ol>
	<li><span style="font-family:Arial,"Helvetica Neue",Helvetica,Tahoma,sans-serif">각 숫자 사이에는 1cm의 여백이 들어가야한다.</span></li>
	<li><span style="font-family:Arial,"Helvetica Neue",Helvetica,Tahoma,sans-serif">1은 2cm의 너비를 차지해야한다. 0은 4cm의 너비를 차지해야한다. 나머지 숫자는 모두 3cm의 너비를 차지한다.</span></li>
	<li><span style="font-family:Arial,"Helvetica Neue",Helvetica,Tahoma,sans-serif">호수판의 경계와 숫자 사이에는 1cm의 여백이 들어가야한다.</span></li>
</ol>

<p><img alt="120.png" src="" style="height:121px; width:213px"></p>

<p><span style="font-family:Arial,"Helvetica Neue",Helvetica,Tahoma,sans-serif">예를 들어 위의 120 같은 경우, </span> 각 숫자 사이에 여백이 1cm 씩 2개 들어간다. 1은 2cm, 2는 3cm, 0은 4cm를 차지한다. 오른쪽, 왼쪽 경계에서 각각 여백이 1cm씩 차지한다. 따라서 총 2 + 2 + 3 + 4 + 1 + 1 = 13(cm) 가 된다.</p>

<p>재석이는 고객에게 전달해야할 호수판의 너비가 얼마나 되는지 궁금해졌다. 재석이를 도와주자!</p>

### 입력 

 <p>호수판에 들어갈 숫자 N의 범위는 1 ≤ N ≤ 9999 이다.</p>

<p>입력은 마지막에 0이 들어오기 전까지 계속해서 줄 단위로 주어진다.</p>

<p>또한, 마지막의 0은 처리하지 않는다.</p>

### 출력 

 <p>각 입력마다 얼마만큼 너비를 차지하는지 정수로 출력하면 된다.</p>

<p>각 출력은 줄바꿈으로 구분되어야한다.</p>

