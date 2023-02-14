/*$('#room-search').click(function(event){
    $('#card-row > div').each(function () {
         if( $(this).attr("id").indexOf(document.getElementById("room-search-input").value) == -1){
            console.log($(this).attr("id"))
            $(this).hide()
         }
    })
    console.log(document.getElementById("room-search-input").value)
})*/

var alertNotUserPlaceholder = document.getElementById('liveAlertNotUser')
var NotUseralert = (message, type) => {
  var NotUserwrapper = document.createElement('div')
  NotUserwrapper.innerHTML = [
    `<div class="alert alert-${type} alert-dismissible" role="alert">`,
    `   <div>${message}</div>`,
    '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
    '</div>'
  ].join('')

  alertNotUserPlaceholder.append(NotUserwrapper)
}

$('room_view').ready(function () {
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
})

$('room_view').ready(function () {
  var CommentDiv = $('div.comment'); //let's cache the array
  var length = CommentDiv.length; //let's cache the  length
    for(var x=0; x < length; x++) {
      CommentDiv.eq(x).prop('id', x);
      if ( x % 2 === 0) {
        CommentDiv.eq(x).prop('class', 'comment row justify-content-start');
      }
      else{
        CommentDiv.eq(x).prop('class', 'comment row justify-content-end');
      }
    }
})