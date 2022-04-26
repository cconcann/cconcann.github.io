var person = [];
var salary = [];

function displayResults() 
{
    var averageSalary = salary[0];
    var maxSalary = salary[0];
    var x = salary.length;

    for (var i=0; i < x; i++) 
    {
        if (maxSalary < salary[i]) 
        {
            maxSalary = salary[i];
        }
    }

    for (var i=1; i < x; i++) 
    {
        averageSalary += salary[i];
    }
        averageSalary = parseInt(averageSalary / x);

    if (person.length > 0) 
    {
        var textHighest = "The highest salary is $" + maxSalary;
        var average = "The average salary is $" + averageSalary;
    }
    else 
    {
        textHighest = "The list is empty. Please add an employee to the list"
        average = ""
    }    

    document.getElementById("results1").innerHTML = textHighest;
    document.getElementById("results2").innerHTML = average;
}


function displaySalary() 
{    
    var disSalary = "";
    for (var i = 0; i < person.length; i++) 
    {
        disSalary += "<tr><td>" + person[i] + "</td><td>" + salary[i] + "</td></tr>";
    }
    disSalary += "</table>";    

    return document.getElementById("results_table").innerHTML = disSalary;
}

function addSalary() 
{    
    var entrySalary = document.getElementById("employee").value;

    if(document.getElementById("salary").value < 0 || "")
    {
        alert("input salary is not valid, please input a positive integer");
    }
    
    if (person.includes(entrySalary) == true) 
    {
        alert(entrySalary + " is already in the list");
    }
    else 
    {
        person.push(entrySalary);
        salary.push(document.getElementById("employee").value);

        /* switch (entrySalary) 
        {
            case "Steven Steve":
                salary.push(60000);
                break;
            
            case "Chris Cannon":
                salary.push(999999999);
                break;
            
            case "Adam Appleseed":
                salary.push(20000);
                break;

            case "Britney Bees":
                salary.push(44000);
                break;

            case "Daniel Dave":
                salary.push(75000);
                break;
        }
        */
    }
    document.getElementById("employee").focus();
}

function reset() {
    person = [];
    salary = [];
    document.getElementById("employee").focus();
}