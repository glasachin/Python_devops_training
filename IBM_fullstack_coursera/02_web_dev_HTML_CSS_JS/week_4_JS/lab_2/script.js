function temperature()
{
    var cels = document.getElementById("c").value;
    var faren = (cels*9/5)+32;
    document.getElementById("f").value = faren;
}

function weight()
{
    var kg = document.getElementById("k").value;
    var pound = kg*2.2;
    document.getElementById("p").value = pound.toFixed(2);
}

function distance()
{
    var km = document.getElementById("km").value;
    var miles = km * 0.62137;
    document.getElementById("mi").value = miles.toFixed(2);
}