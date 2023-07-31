# [Bronze III] 최댓값 - 2566 

[문제 링크](https://www.acmicpc.net/problem/2566) 

### 성능 요약

메모리: 31256 KB, 시간: 40 ms

### 분류

구현

### 문제 설명

<p><그림 1>과 같이 9×9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램을 작성하시오.</p>

<p>예를 들어, 다음과 같이 81개의 수가 주어지면</p>

<table class="table table-bordered td-center th-center table-center-40">
	<tbody>
		<tr>
			<th> </th>
			<th>1열</th>
			<th>2열</th>
			<th>3열</th>
			<th>4열</th>
			<th>5열</th>
			<th>6열</th>
			<th>7열</th>
			<th>8열</th>
			<th>9열</th>
		</tr>
		<tr>
			<th>1행</th>
			<td>3</td>
			<td>23</td>
			<td>85</td>
			<td>34</td>
			<td>17</td>
			<td>74</td>
			<td>25</td>
			<td>52</td>
			<td>65</td>
		</tr>
		<tr>
			<th>2행</th>
			<td>10</td>
			<td>7</td>
			<td>39</td>
			<td>42</td>
			<td>88</td>
			<td>52</td>
			<td>14</td>
			<td>72</td>
			<td>63</td>
		</tr>
		<tr>
			<th>3행</th>
			<td>87</td>
			<td>42</td>
			<td>18</td>
			<td>78</td>
			<td>53</td>
			<td>45</td>
			<td>18</td>
			<td>84</td>
			<td>53</td>
		</tr>
		<tr>
			<th>4행</th>
			<td>34</td>
			<td>28</td>
			<td>64</td>
			<td>85</td>
			<td>12</td>
			<td>16</td>
			<td>75</td>
			<td>36</td>
			<td>55</td>
		</tr>
		<tr>
			<th>5행</th>
			<td>21</td>
			<td>77</td>
			<td>45</td>
			<td>35</td>
			<td>28</td>
			<td>75</td>
			<td>90</td>
			<td>76</td>
			<td>1</td>
		</tr>
		<tr>
			<th>6행</th>
			<td>25</td>
			<td>87</td>
			<td>65</td>
			<td>15</td>
			<td>28</td>
			<td>11</td>
			<td>37</td>
			<td>28</td>
			<td>74</td>
		</tr>
		<tr>
			<th>7행</th>
			<td>65</td>
			<td>27</td>
			<td>75</td>
			<td>41</td>
			<td>7</td>
			<td>89</td>
			<td>78</td>
			<td>64</td>
			<td>39</td>
		</tr>
		<tr>
			<th>8행</th>
			<td>47</td>
			<td>47</td>
			<td>70</td>
			<td>45</td>
			<td>23</td>
			<td>65</td>
			<td>3</td>
			<td>41</td>
			<td>44</td>
		</tr>
		<tr>
			<th>9행</th>
			<td>87</td>
			<td>13</td>
			<td>82</td>
			<td>38</td>
			<td>31</td>
			<td>12</td>
			<td>29</td>
			<td>29</td>
			<td>80</td>
		</tr>
	</tbody>
</table>

<p>이들 중 최댓값은 90이고, 이 값은 5행 7열에 위치한다.</p>

### 입력 

 <p>첫째 줄부터 아홉 번째 줄까지 한 줄에 아홉 개씩 수가 주어진다. 주어지는 수는 100보다 작은 자연수 또는 0이다.</p>

### 출력 

 <p>첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 위치한 행 번호와 열 번호를 빈칸을 사이에 두고 차례로 출력한다. 최댓값이 두 개 이상인 경우 그 중 한 곳의 위치를 출력한다.</p>

