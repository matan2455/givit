
function set_for_coordination() {
    document.getElementById("coordination-div").hidden = false;
}

function hide_form(){
    document.getElementById("coordination-form").hidden = true;
    document.getElementById("coordination-div").hidden = true;
}

function enableInputs(){
    inputs = document.getElementByType('input');
    inputs.foreach(input => input.disabled = "false");
}

function implement_filters(){
    //TODO - implement chosen filters - issue #61
}
