// - has cycle in undirected graph 

const graph = {
  A: ['B'],
  B: ['A', 'C'],
  C: [],
  D: ['E'],
  E: ['D'],
  F: []
};


const hasCycle = (graph) => {
  const visited = new Set();

  const dfs = (node, parent) => {
    visited.add(node);
    for(let nei of graph[node]) {
      if(!visited.has(nei)) {
        if(dfs(nei, node)) return true;
      }
      else if(nei !== parent) {
        return true;
      }
    }
    return false;
  }

  for(let node in graph) {
    if(!visited.has(node)) {
       if(dfs(node, null)) return true;
    }
  }



  return false;
}



const hasCycleDirected = (graph) => {
    const WHITE = 0;
    const GREY = 1;
    const BLACK = 2;
    const states = {};
    for(let n in graph) {
        states[n] = WHITE;
    }

    const dfs = (node) => {
        states[node] = GREY;
        for(let nei of graph[node]) {
            if(states[nei] == WHITE) {
                if(dfs(nei)) return true;
            }
            else if(states[nei] === GREY) {
                return true;
            }
        }
        states[node] = BLACK;

        return false;
    }

    for(let n in graph) {
        if(states[n] == WHITE) {
            if(dfs(n)) {
                return true;
            }
        }
    }

    return false;
}