$(document).ready(function() {
    $("#slider").bxSlider({
        auto: true,
        minSlides: 1,
        maxSlides: 1,
        slideWidth: 800,
        slideMargin: 20,
        pager: true,
        speed: 8000,
        pagerType: 'short',
        captions: true,
        pagerSelector: '#id_paper',
        randomStart: true

    });
});