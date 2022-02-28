function additionFunction()
{
    let first_number = parseInt(document.getElementById('firstnumber').value);
    let second_number = parseInt(document.getElementById('secondnumber').value);

    const calcvalue = first_number + second_number;
    alert("The sum of your two numbers is " + calcvalue);
}

function subtractionFunction()
{
    let first_number = parseInt(document.getElementById('firstnumber').value);
    let second_number = parseInt(document.getElementById('secondnumber').value);

    const calcvalue = first_number - second_number;
    alert("The difference of your two numbers is " + calcvalue);
}

function multiplicationFunction()
{
    let first_number = parseInt(document.getElementById('firstnumber').value);
    let second_number = parseInt(document.getElementById('secondnumber').value);

    const calcvalue = first_number * second_number;
    alert("The total of your two numbers is " + calcvalue);
}

function divisionFunction()
{
    let first_number = parseInt(document.getElementById('firstnumber').value);
    let second_number = parseInt(document.getElementById('secondnumber').value);

    const calcvalue = first_number / second_number;
    alert("The remainder of your two numbers is " + calcvalue);
}