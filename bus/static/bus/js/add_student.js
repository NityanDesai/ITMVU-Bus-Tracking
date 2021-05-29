
let form = document.getElementById('form');

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
    var phone = document.forms['myForm']["parent_mobile_no"].value;
    if (phone < 6000000000 || phone > 9999999999) {
        // e.preventDefault();
        element = document.getElementById("id_parent_mobile_no");
        document.getElementsByClassName('formerror')[0].innerHTML = "*Phone number is not valid!";
        returnval = false;
    }
    return returnval;
}