$(document).ready(function() {
    $("#slider").bxSlider({
        auto: true,
        minSlides: 1,
        maxSlides: 1,
        slideWidth: 300,
        slideMargin: 20,
        pager: true,
        speed: 4000,
        pagerType: 'short',
        captions: true,
        pagerSelector: '#id_paper',
        randomStart: true

    });
});