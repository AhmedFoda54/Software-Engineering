function validate_form(){

let fname = document.forms["myform"]["fname"].value;
let lname = document.forms["myform"]["lname"].value;

if (fname === "") {
    alert("First name must be filled out");
    return false;
}

if (lname === "") {
    alert("Last name must be filled out");
    return false;
}

}