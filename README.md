# CodingTestStudy

C++ - 바킹덕 강의

<b>코드 작성팁</b>

double (실수) / long long (정수) - 범위를 벗어나지 않게 하기 위해서는 이 변수를 주로 사용해도 좋다.
실수를 비교할 때는 등호로 비교하면 안됨 -> 오차범위가 있기 때문에 (ex) abs(a-b) < 1e-12 일 때 같다고 함
C++ String을 처리할 때는 getline을 쓰는 게 좋음 -> cin은 공백문자를 구분하지 못하므로
sync_with_stdio를 쓴 이후로는 무조건 cin/cout만 쓰고 printf/scanf를 쓰면 안됨 - ios::sync_with_stdio(0), cin.tie(0)

<b>배열</b>

배열은 메모리 상에 원소를 연속하게 배치한 자료구조이라서 k번째 원소의 위치를 바로 계산할 수 있음. k번째 원소를 O(1)에 확인하거나 변경 가능
메모리는 다른 자료구조와 다르게 추가적으로 소모되는 메모리의 양이 거의 없음
메모리 상에 데이터들이 붙어있으니까 Cache hit rate가 높음
메모리 상에 연속한 구간을 잡아야 하니 할당에서 다소 제약이 있음

C++에서 배열 초기화
a[21] b[21][21]
fill(a,a+21,0);
for (int i=0; i<21; i++)
  fill(b[i],b[i]+21,0);
  
 <b>연결리스트</b>
 k번째 원소를 확인/변경하기 위해 O(k)가 필요함
 임의의 위치에 원소를 추가/제거는 O(1)
 원소들이 메모리 상에 연속해있지 않아 Cache hit rate가 낮지만 할당이 다소 쉬움
