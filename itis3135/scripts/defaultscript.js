function testFunction()
{
    alert("this is a test");
}

function displayDateTime() 
{
    let today = new Date();
    let month = today.getMonth();
    let monthWord = new Array('January', 'February', 'March', 'April', 'May', 'June', 
    'July', 'August', 'September', 'October', 'November', 'December');
    document.getElementById('datetime').innerHTML = "The current time is: " + today.getHours() + ":" + today.getMinutes() + ".  Todays date is: " + monthWord[month] + " " + today.getDate() + ", " + today.getFullYear() + ".";
}

function greeting()
{
    let userName = document.getElementById('firstname').value;
    let userFeeling = document.getElementById('feeling').value;
    document.getElementById("greeting").innerHTML = "Welcome, " + userName + "!  Thankyou for telling us you are feeling " + userFeeling + ".";
}


function calculateTax()
{
    let sales = parseInt(document.getElementById('sales').value);
    const finalValue = sales + (sales * 0.13);
    document.getElementById('salesOutput').innerHTML = "Your total after tax is: $" + finalValue + ".";
}