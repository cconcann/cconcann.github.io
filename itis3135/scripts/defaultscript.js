



dateTime();

function dateTime() {
    var today = new Date();
    var day = today.getDay();
    var daylist = ["Sunday", "Monday", "Tuesday", "Wednesday ", "Thursday", "Friday", "Saturday"];
    var date = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate();
    var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
    var dateTime = date + ' ' + time;
    document.getElementById("dateTime").innerHTML = dateTime + ' <br> Day :- ' + daylist[day];
}

function testFunction()
{
    alert("this is a test");
}