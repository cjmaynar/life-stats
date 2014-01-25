$(document).ready(function() {
    nv.addGraph(function() {
        var chart = nv.models.discreteBarChart()
            .x(function(d) { return d.label })
            .y(function(d) { return d.value })
            .staggerLabels(true)
            .tooltips(false)
            .showValues(true);

        d3.select('#frequent-events svg')
        .datum(frequentevents())
        .transition().duration(500)
        .call(chart);

        nv.utils.windowResize(chart.update);

        return chart;
    });

    function frequentevents() {
        var events;
        $.ajax({
            async: false,
            type: 'GET',
            url: '/events/data',
            data: {'graph': 'frequent'}
        }).done(function(data) {
            events = data;
        });

        console.log(events);
        return events;
    }
});
