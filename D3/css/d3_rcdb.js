

let margin = {top: 10, right: 10, bottom: 20, left: 40},
    width = 900 - margin.left - margin.right,
    height = 675 - margin.top - margin.bottom;

const svg = d3.select("#grouped-bar")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")"
          );

d3.csv("../WebScraping/CSVs/rcdb_w_years_dtformat_clean.csv").then(function(coasterInfo) {
  console.log(coasterInfo);

    coasterInfo.forEach(d => {
    console.log(d)
    
    })
    })

  


let x = d3.scaleBand()
    /*.domain(coasterInfo.map(d => d[groupKey]))*/
    .rangeRound([margin.left, width - margin.right])
    .paddingInner(0.1)

let x1 = d3.scaleBand()
    .domain(keys)
    .rangeRound([0, x0.bandwidth()])
    .padding(0.05)

let y = d3.scaleLinear()
    .domain([0, d3.max(data, d => d3.max(keys, key => d[key]))]).nice()
    .rangeRound([height - margin.bottom, margin.top])

color = d3.scaleOrdinal()
    .range(["#98abc5","#6b486b"])

let xAxis = g => g
    .attr("transform", `translate(0,${height - margin.bottom})`)
    .call(d3.axisBottom(x0).tickSizeOuter(0))
    .call(g => g.select(".domain").remove())

let yAxis = g => g
    .attr("transform", `translate(${margin.left},0)`)
    .call(d3.axisLeft(y).ticks(null, "s"))
    .call(g => g.select(".domain").remove())
    .call(g => g.select(".tick:last-of-type text").clone()
        .attr("x", 3)
        .attr("text-anchor", "start")
        .attr("font-weight", "bold")
        .text(data.y)
    )

  svg.append("g")
    .selectAll("g")
    .data(coasterInfo)
    .join("g")
    /*.attr("transform", coaster => `translate(${(coaster['Design'])}`)
    .selectAll("rect")
    .data(type => type.map(key => ({key, value: d[key]})))
    .join("rect")
      .attr("x", d => x(d.key))
      .attr("y", d => y(d.value))
      .attr("width", x.bandwidth())
      .attr("height", d => y(0) - y(d.value))
      .attr("fill", d => color(d.key));*/

  svg.append("g")
      .call(xAxis);

  svg.append("g")
      .call(yAxis);

  svg.append("g")
      .call(legend);


const g = svg
      .attr("transform", `translate(${width},0)`)
      .attr("text-anchor", "end")
      .attr("font-family", "sans-serif")
      .attr("font-size", 10)
    .selectAll("g")
    .data(color.domain().slice().reverse())
    .join("g")
      .attr("transform", (d, i) => `translate(0,${i * 20})`);

  g.append("rect")
      .attr("x", -19)
      .attr("width", 19)
      .attr("height", 19)
      .attr("fill", color);

  g.append("text")
      .attr("x", -24)
      .attr("y", 9.5)
      .attr("dy", "0.35em")
      .text(d => d);


console.log(groupKey);
})


