
$('.carousel').carousel({
    interval: 7000,
    pause: "false"
});

$('.rslides').responsiveSlides({
    speed: 500,
    namespace: "rslides",
    before: function(){
        $('.events').append("<li>before event fired.</li>");
    },
    after: function(){
        $('.events').append("<li>after event fired.</li>");
    }
});


