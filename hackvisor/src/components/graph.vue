<template>
    <div ref="graphContainer" class="graph-container"></div>
</template>

<script>
import * as d3 from "d3";

export default {
    name: "Graph",
    mounted() {
        this.createGraph();
    },
    methods: {
        createGraph() {
            const width = 800;
            const height = 600;

            const svg = d3
                .select(this.$refs.graphContainer)
                .append("svg")
                .attr("width", width)
                .attr("height", height);

            const nodes = [
                { id: 1, name: "Node 1" },
                { id: 2, name: "Node 2" },
                { id: 3, name: "Node 3" },
                { id: 4, name: "Node 4" },
            ];

            const links = [
                { source: 1, target: 2 },
                { source: 2, target: 3 },
                { source: 3, target: 4 },
                { source: 4, target: 1 },
            ];

            const simulation = d3
                .forceSimulation(nodes)
                .force(
                    "link",
                    d3.forceLink(links).id((d) => d.id).distance(100)
                )
                .force("charge", d3.forceManyBody().strength(-300))
                .force("center", d3.forceCenter(width / 2, height / 2));

            const link = svg
                .append("g")
                .selectAll("line")
                .data(links)
                .enter()
                .append("line")
                .attr("stroke", "#999")
                .attr("stroke-width", 2);

            const node = svg
                .append("g")
                .selectAll("circle")
                .data(nodes)
                .enter()
                .append("circle")
                .attr("r", 10)
                .attr("fill", "steelblue")
                .call(
                    d3
                        .drag()
                        .on("start", (event, d) => {
                            if (!event.active) simulation.alphaTarget(0.3).restart();
                            d.fx = d.x;
                            d.fy = d.y;
                        })
                        .on("drag", (event, d) => {
                            d.fx = event.x;
                            d.fy = event.y;
                        })
                        .on("end", (event, d) => {
                            if (!event.active) simulation.alphaTarget(0);
                            d.fx = null;
                            d.fy = null;
                        })
                );

            const label = svg
                .append("g")
                .selectAll("text")
                .data(nodes)
                .enter()
                .append("text")
                .text((d) => d.name)
                .attr("font-size", 12)
                .attr("dx", 12)
                .attr("dy", 4);

            simulation.on("tick", () => {
                link
                    .attr("x1", (d) => d.source.x)
                    .attr("y1", (d) => d.source.y)
                    .attr("x2", (d) => d.target.x)
                    .attr("y2", (d) => d.target.y);

                node.attr("cx", (d) => d.x).attr("cy", (d) => d.y);

                label.attr("x", (d) => d.x).attr("y", (d) => d.y);
            });
        },
    },
};
</script>

<style>
.graph-container {
    width: 100%;
    height: 100%;
}
</style>