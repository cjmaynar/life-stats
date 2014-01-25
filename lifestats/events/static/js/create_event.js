$(document).ready(function() {
    $("#id_occurrences").datepicker();
    $("#id_category").typeahead({
        name: 'categories',
        remote: '/events/typeahead',
        limit: 10
    });

    //Fix positioning issue with the typeahead hint
    $('.tt-hint').addClass('form-control');
});
