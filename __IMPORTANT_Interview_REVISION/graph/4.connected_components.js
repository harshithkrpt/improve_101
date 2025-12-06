
const graph = {
    A: ['B'],
    B: ['A'],
    C: [],
    D: ['E'],
    E: ['D'],
    F: []
};



function connectedComponents(graph) {
    const vis = new Set();
    let count = 0;

    function explore(graph, node) {
        const q = [node];
        vis.add(node);
        while (q.length) {
            const p = q.shift();
            for (let g of graph[p]) {
                if (!vis.has(g)) {
                    vis.add(g);
                    q.push(g);
                }
            }
        }
    }

    for (let n in graph) {
        if (!vis.has(n)) {
            count++;
            explore(graph, n, vis);
        }
    }

    return count;
}

console.log(connectedComponents(graph));


