$(".btn-info").on("click", e => {
  var text = $("#correctme").val()
  if (text) {
  $.post("/", {"text": text} ,function (data) {
    var newtext = text;
    data.flaggedTokens.map(e => {   
    newtext = newtext.replace(new RegExp(`${e.token}`), e.suggestions[0].suggestion)  
    })
    $("#theoutput").val(newtext)
  })
  } 
})