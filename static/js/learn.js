var resp = document.getElementById("resp");
var card = document.getElementById("card");
var circ = document.getElementById("circ");
var repr = document.getElementById("repr");

resp.addEventListener("click", function() {
    var style = window.getComputedStyle(respinfo).getPropertyValue('display');
    if(style == 'none'){
        $("#respinfo").css('display','block');
    }else{
        $("#respinfo").css('display','none');
    }
});

card.addEventListener("click", function() {
    var style = window.getComputedStyle(cardinfo).getPropertyValue('display');
    if(style == 'none'){
        $("#cardinfo").css('display','block');
    }else{
        $("#cardinfo").css('display','none');
    }
});

circ.addEventListener("click", function() {
    var style = window.getComputedStyle(circinfo).getPropertyValue('display');
    if(style == 'none'){
        $("#circinfo").css('display','block');
    }else{
        $("#circinfo").css('display','none');
    }
});

repr.addEventListener("click", function() {
    var style = window.getComputedStyle(reprinfo).getPropertyValue('display');
    if(style == 'none'){
        $("#reprinfo").css('display','block');
    }else{
        $("#reprinfo").css('display','none');
    }
});