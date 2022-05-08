let person1 = "toobin";
let person2 = "sorkin";
let person3 = "chua";
let person4 = "sampson";
$(document).ready(function () {
    $("#nav_list li").click(function () {
        var person = $(this).children('a').attr("title");

        if (person == person1) {

            $.ajax({
                type: "get",
                url: "toobin.json",
                beforeSend: function () {
                    $("#team").html("Loading...");
                },
                timeout: 10000,
                error: function (xhr, status, error) {
                    alert("Error: " + xhr.status + " - " + error);
                },
                dataType: "json",
                success: function (data) {
                    $("main").html("");
                    $.each(data, function () {
                        $.each(this, function (key, value) {
                            $("main").append($('<h1>' + value.title + '</h1>' + '<h2>' + value.month + '</h2>' + '<h3>' + value.speaker + '</h3>' + "<img src=" + value.image + ">" + '<p>' + value.text + '</p>'));

                        })
                    });
                }
            });
        };

        if (person == person2) {

            $.ajax({
                type: "get",
                url: "sorkin.json",
                beforeSend: function () {
                    $("#team").html("Loading...");
                },
                timeout: 10000,
                error: function (xhr, status, error) {
                    alert("Error: " + xhr.status + " - " + error);
                },
                dataType: "json",
                success: function (data) {
                    $("main").html("");
                    $.each(data, function () {
                        $.each(this, function (key, value) {
                            $("main").append('<h1>' + value.title + '</h1>' + '<h2>' + value.month + '</h2>' + '<h3>' + value.speaker + '</h3>' + '<img src="' + value.image + '">'  + '<p>' + value.text + '</p>');

                        })
                    });
                }
            });
        };

        if (person == person3) {

            $.ajax({
                type: "get",
                url: "chua.json",
                beforeSend: function () {
                    $("#team").html("Loading...");
                },
                timeout: 10000,
                error: function (xhr, status, error) {
                    alert("Error: " + xhr.status + " - " + error);
                },
                dataType: "json",
                success: function (data) {
                    $("main").html("");
                    $.each(data, function () {
                        $.each(this, function (key, value) {
                            $("main").append('<h1>' + value.title + '</h1>' + '<h2>' + value.month + '</h2>' + '<h3>' + value.speaker + '</h3>' + '<img src="' + value.image + '">'  + '<p>' + value.text + '</p>');

                        })
                    });
                }
            });
        };

        if (person == person4) {

            $.ajax({
                type: "get",
                url: "sampson.json",
                beforeSend: function () {
                    $("#team").html("Loading...");
                },
                timeout: 10000,
                error: function (xhr, status, error) {
                    alert("Error: " + xhr.status + " - " + error);
                },
                dataType: "json",
                success: function (data) {
                    $("main").html("");
                    $.each(data, function () {
                        $.each(this, function (key, value) {
                            $("main").append('<h1>' + value.title + '</h1>' + '<h2>' + value.month + '</h2>' + '<h3>' + value.speaker + '</h3>' + '<img src=' + value.image + '>'  + '<p>' + value.text + '</p>');

                        })
                    });
                }
            });
        };

    });
}); // end ready