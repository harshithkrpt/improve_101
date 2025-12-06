const graph = {
  A: ['B', 'C'],
  B: ['D'],
  C: ['D', 'E'],
  D: [],
  E: []
};


const bfs = (graph, node) => {
  if(!node) return null;

  const visited = new Set();
  const queue = [node];
  visited.add(node);
  while(queue.length > 0) {
    const pNode = queue.shift();
    console.log(pNode);
    for(let nei of graph[pNode]) {
      if(!visited.has(nei)) {
        visited.add(nei);
        queue.push(nei);
      }
    }
  }
}

bfs(graph, 'A');