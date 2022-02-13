





function testFunction()
{
    alert("this is a test");
}

function displayDatetime() 
{
    let today = new Date();
    let month = today.getMonth();
    let monthWord = new Array('January', 'February', 'March', 'April', 'May', 'June', 
    'July', 'August', 'September', 'October', 'November', 'December');
    document.getElementById('datetime').innerHTML = "The current time is: " + today.getHours() + ":" + today.getMinutes() + ".  Todays date is: " + monthWord[month] + " " + today.getDate() + ", " + today.getFullYear() + ".";
}