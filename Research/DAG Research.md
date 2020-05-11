# DAG Research

방향성 비순환 그래프(DAG; Directed Acyclic Graph)란 개별 요소들이 특정한 방향을 향하고 있으며, 서로 순환하지 않는 구조로 짜여진 그래프이다.

DAG는 무한히 많은 꼭짓점(v)과 간선(e)으로 구성되며 각 간선은 하나의 꼭짓점에서 다른 꼭짓점으로 방향을 잇게 되는데 어떤 꼭짓점 v에서 시작하여 다시 꼭짓점 v로 되돌아 오는 경로는 존재하지 않는다.

## 순환 그래프 vs 비순환 그래프

### 순환 그래프

![Negative Graph](https://steemitimages.com/640x0/https://steemitimages.com/DQmUJaKxfxSgvZwWyfxvMv74UT3qZeHP6Ewoo6EgbhWgpuo/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202018-03-23%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2011.07.31.png)

A -> B -> C -> A의 사이클이 발생하여 계속적으로 반복될 수 있는 상황이 발생 가능하다.

순환 그래프의 경우 그래프 처리에 있어서 두 가지 어려움이 생긴다. 첫 번째는 긍정적인 위상(S, A, B, C, D와 같은 위상)을 가져야 산출이 쉽다는 점이다. 두 번째는 계속적으로 반복될 수 있는 상황이 발생하는 사이클이 없어야 한다는 점이다.

### 비순환 그래프

![Directed Acyclic Graph](https://steemitimages.com/DQmR2YCjhtSzW5DfpraEjRLfqyzcAVdtBY74CBEkuRYiXve/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202018-03-23%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2011.53.14.png)

비순환 그래프에서는 계속적으로 순환될 수 있는 구간이 없기 때문에, 순환 그래프에서 발생할 수 있는 문제점이 없다. 비순환 그래프의 위와 같은 정렬을 위상 정렬(Topologically sorted)이라고 한다.

DAG는 비순환 그래프이다. 즉, DAG 알고리즘에서는 순환하는 사이클이 존재하지 않고 일방향성만 가진다.

### 위상 정렬

위상 정렬이란, 작업을 실제로 한 번에 하나씩 순서대로 처리한다면 어떤 순서로 작업해야 하느냐를 표현한 것으로 작업의 순서대로 노드를 일렬로 정렬하는 것이다.

노드의 순서가 무조건 한 방향으로만 향해야 한다. 역방향 노드가 있다면 올바른 작업의 순서가 될 수 없다.

위상 정렬은 시작값에 따라 여러 가지로 표현될 수 있고 결론적으로 답이 하나로 유효하지 않다.

방향 그래프에서 들어오는 엣지를 incomming 나가는 엣지를 outgoing이라고 하고 들어오는 엣지의 개수를 indegree, 나가는 엣지의 개수를 outdegree라고 정의해 본다.

```pseudocode
topologicalSort1(G){
    for <- 1 to n {
        진입 간선이 없는 임의의 정점 u를 선택한다.                                                                  
        A[i]<-u;
        정점 u와 진출간선을 모두 제거한다.
    }
    // 배열 A[1...n]에는 정점들이 위상 정렬 되어있다.
}
```

![topologicalSort1](https://t1.daumcdn.net/cfile/tistory/23089C3D5924F0D324)

1. 모든 노드들에 대해서 indegree가 0인 노드를 찾는다.
2. 이러한 노드가 2개 이상 존재하면 그 중 하나를 선택한다.
3. 선택한 노드 A와 A에서 나가는 엣지를 그래프에서 제거한다.
4. 남은 그래프에 대해 [1] ~ [3] 과정을 반복한다.
5. 마지막에 남은 노드까지 도달하게 되면 모든 노드가 위상 정렬 된다.

```pseudocode
topologicalSort2(G){
    for each v->V
        visited[v] <- NO;
    make an empty linked list R;
    for each v->V // 정점의 순서는 상관 없음
        if(visited[v] = NO) then
            DFS-TS(v,R);
}
 
DFS-TS(v, R){
    visited[v] <- YES;
    for each x adjacent to v do
        if(visited[x] == NO) then
            DFS-TS(x,R);
    add v at the front of the linked list R;
}
```

![topologicalSort2_0](https://t1.daumcdn.net/cfile/tistory/2549094F5924F38B33)

![topologicalSort2_1](https://t1.daumcdn.net/cfile/tistory/220241475924F43A19)

![topologicalSort2_2](https://t1.daumcdn.net/cfile/tistory/240B68485924F47D16)

1. 모든 노드들에 대해서 visited를 NO로 설정한다.
2. Empty Linked List인 R을 만든다.
3. 아직 방문하지 않은 아무 노드 하나를 선택해서 그 노드에서 출발하는 DFS를 수행한다.
4. DFS는 방문한 노드를 체크하고 그 노드와 인접한 노드 x에 대해 해당 노드가 방문되지 않았다면 다시 DFS를 수행한다.
5. DFS 탐색이 끝나면 Linked List R에 해당 노드를 추가한다.
6. Linked List R에 노드가 모두 추가되면 위상 정렬된 Linked List R을 얻을 수 있다.

## DAG 알고리즘의 특성

- 시간의 제약없이 실시간으로 그리고 병렬적으로 꼭짓점을 생성해 나갈 수 있다. 따라서, 알고리즘 내에서 데이터 처리 속도가 굉장히 빠르다.
- DAG 알고리즘이 적용된 블록체인에는 블록이 없기 때문에 채굴자들의 트랜잭션 승인을 기다릴 필요가 없다. 블록 생성 없이 트랜잭션이 다른 트랜잭션을 검증하는 형태기 때문에 매우 빠른 속도로 절차가 수행되며 검증과정이 병렬적으로 이루어지기 때문에 트랜잭션이 많을 수록 즉, 사용자가 많을 수록 검증절차가 더 빨라진다.
- 위의 특징으로 인해 채굴에 대한 보상을 위해 거두어가던 수수료는 발생하지 않는다.
- 일반적인 블록체인에서는 사용량이 많아질 수록 블록 대비 트랜잭션 수가 넘쳐나는 병목현상이 발생하게 되지만 DAG는 사용량이 많아질 수록 새로운 트랜잭션을 검증할 이전 트랜잭션이 많아지므로 오히려 검증의 신뢰도와 속도가 증가한다.
- DAG 원장은 Total Ordering 방식이 아닌 Partial Ordering 방식으로 서로 연결된 트랜잭션끼리만 그 쓰여진 순서를 정의할 수 있다. 그렇기 때문에 현재의 전체 원장 상태라는 것이 존재하지 않고 이 때문에 확정합의를 하기 어렵다. 확정합의를 하기 위해서는 모두가 동일한 상태를 가지고 있어야 하는데 그러려면 새로운 트랜잭션의 생성을 멈추고 현재 상태가 모든 네트워크 구성원들에게 전파되기를 기다려야 한다. 그러나 이렇게 되면 DAG의 장점인 속도와 확장성에 제동이 걸리기 때문에 대부분 비확정합의 프로토콜을 채택하고 있다. 그러나 비확정합의 프로토콜은 거래 결과가 뒤집어 질 수 있는 큰 리스크가 존재하기 때문에 DAG와 확정합의의 융합이 반드시 필요하다.

## 참고문헌

1. 방향성 비순환 그래프 | hash.kr | http://wiki.hash.kr/index.php/%EB%B0%A9%ED%96%A5%EC%84%B1_%EB%B9%84%EC%88%9C%ED%99%98_%EA%B7%B8%EB%9E%98%ED%94%84
2. DAG 알고리즘이란 무엇인가? DAG(Directed Acyclic Graph)는 과연 솔루션이 될 수 있을까? | cryptodreamers | steemit | https://steemit.com/dag/@cryptodreamers/dag-dag-directed-acyclic-graph
3. [알고리즘] DAG와 위상 순서 | 마스터누누 | https://new93helloworld.tistory.com/182