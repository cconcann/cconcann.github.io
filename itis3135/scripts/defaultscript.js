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

function calculateShipping()
{
    let shipping = parseInt(document.getElementById('shipping').value);
    const finalShipping = shipping + (shipping * 0.10);
    document.getElementById('shippingOutput').innerHTML = "Your total for shipping is: $" + finalShipping + ".";
}

function showPic()
{
    var Image_Id = document.getElementById('babyPic');
        Image_Id.src = "images/baby.jpg";
}