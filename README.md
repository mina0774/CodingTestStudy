# CodingTestStudy

C++ - 바킹덕 강의

<b>코드 작성팁</b>

double (실수) / long long (정수) - 범위를 벗어나지 않게 하기 위해서는 이 변수를 주로 사용해도 좋다.  <br>
실수를 비교할 때는 등호로 비교하면 안됨 -> 오차범위가 있기 때문에 (ex) abs(a-b) < 1e-12 일 때 같다고 함  <br>
C++ String을 처리할 때는 getline을 쓰는 게 좋음 -> cin은 공백문자를 구분하지 못하므로  <br>
sync_with_stdio를 쓴 이후로는 무조건 cin/cout만 쓰고 printf/scanf를 쓰면 안됨 - ios::sync_with_stdio(0), cin.tie(0)  <br>

<b>배열</b>

배열은 메모리 상에 원소를 연속하게 배치한 자료구조이라서 k번째 원소의 위치를 바로 계산할 수 있음. k번째 원소를 O(1)에 확인하거나 변경 가능  <br>
메모리는 다른 자료구조와 다르게 추가적으로 소모되는 메모리의 양이 거의 없음  <br>
메모리 상에 데이터들이 붙어있으니까 Cache hit rate가 높음 <br> 
메모리 상에 연속한 구간을 잡아야 하니 할당에서 다소 제약이 있음  <br>

C++에서 배열 초기화  <br>
a[21] b[21][21]  <br>
fill(a,a+21,0);  <br>
for (int i=0; i<21; i++)  <br>
  fill(b[i],b[i]+21,0); <br>
  
 <b>연결리스트</b>
 
 k번째 원소를 확인/변경하기 위해 O(k)가 필요함  <br>
 임의의 위치에 원소를 추가/제거는 O(1) (추가, 제거하고 싶은 위치의 주소를 알고 있을 경우에만 해당) <br>
 원소들이 메모리 상에 연속해있지 않아 Cache hit rate가 낮지만 할당이 다소 쉬움 <br>
 
 코딩테스트에서는 C++에 있는 STL list를 활용하면 됨 (STL list는 Doubley Linked List 구조) <br> <br>
 
 만약, STL list를 사용을 못한다면 -> 야매 연결리스트 <br>
 const int MX=1000005; <br>
 int dat[MX], pre[MX], nxt[MX]l <br>
 int unused =1; <br>
 fill(pre, pre+MX, -1); <br>
 fill(nxt, nxt+MX, -1); <br>
 // dat[i]는 i번지의 원소의 값 <br>
 // pre[i]는 i번지 원소 이전의 인덱스 <br>
 // nxt[i]는 i번지 원소 다음의 인덱스 <br>
 // pre, nxt의 값이 -1이면 해당 원소의 이전/다음 원소가 존재하지 않는다는 의미, unused는 현재 사용되지 않는 인덱스 <br>
 // 0번지는 값이 들어가지 않고 시작점을 나타내기 위한 dummy node <br>
 
 void insert(int addr, int num){
    dat[unused]=num;
    pre[unused]=addr;
    nxt[unused]=nxt[addr];
    if(nxt[addr]!=-1) pre[nxt[addr]]=unused; // 요걸 빠뜨림
    nxt[addr]=unused;
    unused++;
 }
 
 void erase(int addr){
    nxt[pre[addr]]=nxt[addr];
    if(nxt[addr] != -1) pre[nxt[addr]]=pre[addr]; // 더미노드로 인해 pre[addr]은 -1이 아님이 보장되지만, nxt[addr]은 -1일수도 있음
 }
 
STL list
백준 1406번 에디터

<b>스택</b>

백준 10828번 스택

<b>큐</b>

head는 가장 앞에 있는 원소의 인덱스 <br>
tail은 가장 뒤에 있는 원소의 인덱스 +1 <br>
dat[head]부터 dat[tail-1]번지 -> 큐의 원소들이 들어있는 자리 <br>
큐의 크기: tail-head <br>
백준 10845번 큐

<b>덱</b>

백준 10866번 덱

<b>스택의 활용 - 수식의 괄호쌍 </b>
공백을 추가한 문자열을 입력받을 때는 string a; getline(cin,a); <br>
백준 4949번 균형잡힌 세상 <br>
