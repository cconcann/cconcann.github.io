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

function swapPic()
{
    var Image_Id = document.getElementById('babyPic');
        Image_Id.src = "images/dog.jpg";
}

function swapName()
{
    document.getElementById('name').innerHTML = "Christopher Concannon 💪 ITIS3135 💪 The Crimson Caniacs!!!!";
}

function getPolygonSides()
{
    var sidecount = parseInt(prompt("The Crystal Crocodile would like you to input a number between 1 and 10, and will tell you what polygon has that number of sides!"));
    var validSides = validateEntry(sidecount);
    var polygonResults = getShape(validSides);
    alert(polygonResults);
    document.getElementById('_polygonResults').innerHTML = "Your polygon is a" + polygonResults + ".";

}

function getShape(_sideCount)
{
    var listOfPolygons = new Array("nothing real","digon", "triangle","square", "pentagon", "hexagon", "heptagon","octagon","nonagon","decagon");
    return listOfPolygons[_sideCount -1];
}



function validateEntry(_sideCount)
{
    while(isNaN(_sideCount))
    {
        alert("Apologies but your input is out of bounds");
        _sideCount = prompt("Please input a number between 1 and 10 for sides");
    }
    return _sideCount;
}