const graph = {
  A: ['B', 'C'],
  B: ['D'],
  C: ['D', 'E'],
  D: [],
  E: []
};


const bfs = (graph, node) => {
  if(!node) return null;

  const dist = {};
  const queue = [node];
  dist[node] = 0;
  while(queue.length > 0) {
    const pNode = queue.shift();
    for(let nei of graph[pNode]) {
      if(dist[nei] === undefined) {
        queue.push(nei);
        dist[nei] = dist[pNode] + 1;
      }
    }
  }

  return dist;
}

console.log(bfs(graph, 'A'));


const bfsPathTracker = (graph, start, target) => {
  if(!start || !target) return null;

  const vis = new Set([start]);
  const q = [start];
  const parent = {
    [start]: null
  };

  while(q.length) {
    const cur = q.shift();

    if(cur === target) break;

    for(let nei of graph[cur]) {
      if(!vis.has(nei)) {
        vis.add(nei);
        parent[nei] = cur;
        q.push(nei);
      }
    }
  }

  if(parent[target] === undefined) return null;

  let cur = target;
  const res = [];
  while(cur != null) {
    res.push(cur);
    cur = parent[cur];
  }

  return res.reverse();
}


console.log(bfsPathTracker(graph, 'A', 'E'));