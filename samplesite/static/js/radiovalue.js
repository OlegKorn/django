alert('dfsdfs')

$(document).ready(function() {
  alert('dsdfsdf')
  var radio = $('.for-replace')
  var input = $('.replaced')

  radio.change(function() {
    if ($(this).is(':checked')) {
      alert($(this).val())
      //input.html($(this).val())
    } 
  })
})