/*$('#room-search').click(function(event){
    $('#card-row > div').each(function () {
         if( $(this).attr("id").indexOf(document.getElementById("room-search-input").value) == -1){
            console.log($(this).attr("id"))
            $(this).hide()
         }
    })
    console.log(document.getElementById("room-search-input").value)
})*/

$("#room-search").click(function() {
    var value = $('#room-search-input').val().toLowerCase();
    $('div[data-role="test"]').filter(function() {
        $(this).toggle($(this).find('h5').text().toLowerCase().indexOf(value) > -1)
    });
});

