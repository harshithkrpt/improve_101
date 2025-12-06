const graph = {
  A: ['B', 'C'],
  B: ['D'],
  C: ['D'],
  D: []
};

const dfs = (graph, start, visited = new Set()) => {
  if(visited.has(start)) return;
  visited.add(start);
  console.log(start);
  for(let nei of graph[start]) {
    dfs(graph, nei, visited);
  }
}

dfs(graph, 'A');

function dfsIter(graph, start) {
  const stack = [start];
  const visited = new Set();

  while (stack.length) {
    const node = stack.pop();
    if (visited.has(node)) continue;
    visited.add(node);

    console.log(node);

    for (const nei of graph[node]) {
      stack.push(nei);
    }
  }
}


dfsIter(graph, 'A');