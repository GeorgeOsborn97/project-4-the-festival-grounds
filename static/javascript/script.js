$('#room-search').click(function(){
    $('#card-row > div').each(function () {
         if( $(this).attr("id").indexOf(document.getElementById("room-search-input").value) == -1){
            console.log($(this).attr("id"))
            $(this).hide()
         }
    })
    console.log(document.getElementById("room-search-input").value)
})

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
  const alertComment = document.getElementById('liveAlertComment')
  const roomId = document.getElementById('roomId').innerHTML
  const conversationId = document.getElementById('conversationId').innerHTML
  const commentId = document.getElementById('commentId').innerHTML
  console.log(roomId)
  const alert = (message, type, location, id, post) => {
    const wrapper = document.createElement('div')
    wrapper.innerHTML = [
      `<div class="alert alert-${type} alert-dismissible" role="alert">`,
      `   <div>${message}</div>`,
      '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
      ` <a href="/delete_${location}/${id}"><button class="button-style" style="background-color: #e61b1b">delete ${location}</button></a>`,
      '</div>'
    ].join('')

    post.append(wrapper)
  }

  const roomAlertTrigger = document.getElementById('delRoomBtn')
  if (roomAlertTrigger) {
    roomAlertTrigger.addEventListener('click', () => {
      alert('You are about to Delete this room, are you sure?', 'danger', 'room', roomId, alertPlaceholder)
    })
    console.log('hello')
  }
  const conversationAlertTrigger = document.getElementById('delconversationBtn')
  if (conversationAlertTrigger) {
    conversationAlertTrigger.addEventListener('click', () => {
      alert('You are about to Delete this conversation, are you sure?', 'danger', 'conversation', conversationId, alertPlaceholder)
    })
    console.log('hello')
  }
  const commentAlertTrigger = document.getElementById('delcommentBtn')
  if (commentAlertTrigger) {
    commentAlertTrigger.addEventListener('click', () => {
      alert('You are about to Delete this comment, are you sure?', 'danger', 'comment', commentId, alertComment)
    })
    console.log('hello')
  }
})

$('room_view').ready(function () {
  var CommentDiv = $('div.comment');
  var length = CommentDiv.length;
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