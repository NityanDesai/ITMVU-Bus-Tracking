
let form = document.getElementById('form');
// let busno = document.getElementById('busno');
// let drivername = document.getElementById('drivername');
// let phone = document.getElementById('phone');

form.onsubmit = validateForm;

function clearErrors() {
    errors = document.getElementsByClassName('formerror');
    for (let item of errors) {
        item.innerHTML = "";
    }
}

function validateForm(e) {
    var returnval = true;
    clearErrors();

    //perform validation and if validation fails, set the value of returnval to false
    var busno = document.forms["myForm"]["busno"].value;
    if (busno < 1 || busno > 100) {
        // e.preventDefault();
        element = document.getElementById("busno");
        document.getElementsByClassName('one')[0].innerHTML = "*This bus isn't available!";
        returnval = false;
    }

    var phone = document.forms['myForm']["phone"].value;
    if (phone < 6000000000 || phone > 9999999999) {
        // e.preventDefault();
        element = document.getElementById("phone");
        document.getElementsByClassName('two')[0].innerHTML = "*Phone number is not valid!";
        returnval = false;
    }
    return returnval;
}