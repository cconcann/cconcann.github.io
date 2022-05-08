$(document).ready(function() {
    $("#slider").bxSlider({
        auto: true,
        minSlides: 1,
        maxSlides: 1,
        slideWidth: 800,
        slideMargin: 60,
        pager: true,
        speed: 750,
        pagerType: 'short',
        captions: true,
        pagerSelector: '#id_paper',
        randomStart: true,
        adaptiveHeight: true,
        pause: 5000
    });
});