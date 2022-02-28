function additionFunction()
{
    let first_number = parseInt(document.getElementById('firstnumber').value);
    let second_number = parseInt(document.getElementById('secondnumber').value);

    const calcvalue = first_number + second_number;
    alert("The sum of your two numbers is " + calcvalue);
}