/**
 * Created with PyCharm.
 * User: Sergey Zlobov
 * Date: 24.07.13
 * Time: 15:44
 * To change this template use File | Settings | File Templates.
 */
$('#id_note_value').keyup(function(){
        var val=document.getElementsByName('note_value')[0].value;
        var lent = val.length

            $('#count_value').text(lent);

});