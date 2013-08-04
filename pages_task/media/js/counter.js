$(document).ready(function(){
$('#textnote_form').append("<p id='counter'>Total characters: <span id='count_value'>0</span></p>");
$("#main_form" ).append( "<p id='counter'>Total characters: <span id='count_value'>0</span></p>" );
$('#id_note_value').keyup(function(){
        var val=document.getElementsByName('note_value')[0].value;
        var lent = val.length

            $('#count_value').text(lent);

});
    });