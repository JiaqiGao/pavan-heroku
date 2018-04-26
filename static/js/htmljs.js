$(document).ready(function(){
    var scroll_start = 0;
    var startchange = $('#graphic2');
    var offset = startchange.offset();
    if (startchange.length){
      $(document).scroll(function() {
      scroll_start = $(this).scrollTop();
      if(scroll_start > offset.top) {
          $(".navbar").css('background-color', 'rgba(0,0,0,0.9)');
          $("ul.nav").css('background-color', 'transparent');
          $("#pavan-brand").css('background-color', 'transparent');
       } else {
          $('.navbar').css('background-color', 'transparent');
          $("ul.nav").css('background-color', 'rgba(0,0,0,0.9)');
          $("#pavan-brand").css('background-color', 'transparent');
       }
      });
    }
});

var twitter = document.getElementById("twitter");

twitter.addEventListener("click", function() {
    var style = window.getComputedStyle(twitterinfo).getPropertyValue('display');
    if(style == 'none'){
        $("#twitterinfo").css('display','inline-block');
        $("#twitterinfo").css('padding','3px');
    }else{
        $("#twitterinfo").css('display','none');
    }
});


var bg = document.getElementById("graphic1");


var bgImageArray = ["0.jpg", "1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"],
    base = "static/media/homepage/New_Delhi_",
    secs = 6;
    bgImageArray.forEach(function(img){
        new Image().src = base + img;
});

function backgroundSequence() {
    window.clearTimeout();
    var k = 0;
    for (var i = 0; i < bgImageArray.length; i++) {
        setTimeout(function(){
            bg.style.background = "url(" + base + bgImageArray[k] + ") center center fixed";
            bg.style.backgroundSize ="cover";
            if ((k + 1) === bgImageArray.length) { setTimeout(function() { backgroundSequence() }, (secs * 1000))} else { k++; }
        }, (secs * 1000) * i)
    }
}
backgroundSequence();