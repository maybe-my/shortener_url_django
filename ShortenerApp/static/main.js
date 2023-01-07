function copyToClipboard() {
    let copyText = document.getElementById("copy-able");
    copyText.select();
    copyText.setSelectionRange(0, 99999); /*For mobile devices*/
    document.execCommand("copy");
}


$("#copy-btn").click(function () {
    $("div.success").fadeIn(300).delay(1500).fadeOut(900);
});


function checkEmail(event) {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    let email = document.getElementById('email_input').value;
    let isEmailValid = re.test(String(email).toLowerCase());

    if (email.length < 1) {
        $("div#cant-be-empty").fadeIn(300).delay(1500).fadeOut(900);
        event.preventDefault();
        return false;

    } else if (isEmailValid === false) {
        $("div#invalid-email").fadeIn(300).delay(1500).fadeOut(900);
        event.preventDefault();
        return false;
    }
}

$('#verification').on('keyup', function () {
    var foo = $(this).val().split(" ").join("");
    if (foo.length > 0) {
        foo = foo.match(new RegExp('.{1,3}', 'g')).join(" ");
    }
    $(this).val(foo);
});