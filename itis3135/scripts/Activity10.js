$(document).ready(function() {


        // preload the image for each link
        $("#image_list a").each( (index, link) => {
                const image = new Image();
                image.src = link.href;
        });
        // set up the event handlers for each link
        $("#image_list a").click( evt => {
                const link = evt.currentTarget;

                $("#main_image").fadeOut(1000, function() {
                $("#main_image").attr("src", link.href).fadeIn(1000);
                });

                $("#caption").fadeOut(1000,function() {
                $("#caption").text(link.title).fadeIn(1000);
                });
                evt.preventDefault();
        });
    			// get the image URL and caption for each image and animate the caption

            // cancel the default action of each link


    // move the focus to the first link
        $("li:first-child a").focus();
}); // end ready