# [Bronze III] 미국 스타일 - 2712 

[문제 링크](https://www.acmicpc.net/problem/2712) 

### 성능 요약

메모리: 31256 KB, 시간: 40 ms

### 분류

사칙연산, 구현, 수학

### 문제 설명

<p style="text-align: center;"><iframe allowfullscreen="" frameborder="0" height="315" src="https://www.youtube.com/embed/9bZkp7q19f0" width="560"></iframe></p>

<p>싸이가 강남 스타일로 2012년 10월 4일 현재 빌보드 핫100 차트 2위에 2주 연속 랭크되고 있다. 싸이는 곧 다시 미국으로 가서 해외 활동할 예정이라고 한다.</p>

<p>하지만 미국은 한국과 사용하는 단위 체계가 다르다. 한국은 미터법을 사용하지만, 미국은 미국 단위계를 사용한다. 싸이를 위해 단위를 바꾸어 주는 프로그램을 작성하시오.</p>

<p>아래 표를 참고해서 계산하면 되고, 킬로그램 <-> 파운드, 리터 <-> 갤런만 변환하면 된다.</p>

<table class="table table-bordered" style="width:100%">
	<thead>
		<tr>
			<th style="width:34%">종류</th>
			<th style="width:33%">미터법</th>
			<th style="width:33%">미국 단위계</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>무게</td>
			<td>1.000 킬로그램</td>
			<td>2.2046 파운드</td>
		</tr>
		<tr>
			<td> </td>
			<td>0.4536 킬로그램</td>
			<td>1.0000 파운드</td>
		</tr>
		<tr>
			<td>부피</td>
			<td>1.0000 리터</td>
			<td>0.2642 갤런</td>
		</tr>
		<tr>
			<td> </td>
			<td>3.7854 리터</td>
			<td>1.0000 갤런</td>
		</tr>
	</tbody>
</table>

### 입력 

 <p>첫째 줄에 테스트 케이스의 개수 T(1<=T<=1,000)가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있다. 첫 번째 숫자는 값이고, 두 번째 등장하는 문자는 단위이다. 값은 소수일 수도 있고, 이 경우 소수점 아래 최대 넷째 자리까지 주어진다. 단위는 kg, lb, l, g 중 하나이며, 순서대로 킬로그램, 파운드, 리터, 갤런이다.</p>

### 출력 

 <p>각 테스트 케이스에 대해서 바꾼 값과 단위를 출력한다. 값은 반올림해서 소수점 4째자리까지 출력한다. 단위는 kg, lb, l, g중 하나이며, 설명은 입력 설명에 있다.</p>

