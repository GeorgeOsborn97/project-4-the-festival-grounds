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

const alertPlaceholder = document.getElementById('liveAlertPlaceholder')
const roomId = document.getElementById('roomId').innerHTML
console.log(roomId)
const alert = (message, type) => {
  const wrapper = document.createElement('div')
  wrapper.innerHTML = [
    `<div class="alert alert-${type} alert-dismissible" role="alert">`,
    `   <div>${message}</div>`,
    '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
    ` <a href="/delete_room/${roomId}"><button class="btn btn-danger">delete Room</button></a>`,
    '</div>'
  ].join('')

  alertPlaceholder.append(wrapper)
}

const alertTrigger = document.getElementById('liveAlertBtn')
if (alertTrigger) {
  alertTrigger.addEventListener('click', () => {
    alert('You are about to Delete this room, are you sure?', 'danger')
  })
  console.log('hello')
}