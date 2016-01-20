$(document).ready(function() {

  // button for sign-up event

  $('.btn-request').click(function() {

    // hide any message
    $("#form-alert").toggle(false);

    var args = {
        sender_name: $('[name="sender_name"]').val(),
        company_name: $('[name="company_name"]').val(),
        email: $('[name="email"]').val(),
        phone: $('[name="phone"]').val(),
        product: $('[name="product"]').val(),
      }

    // all mandatory
    if(!(args.sender_name && args.company_name && args.email
        && args.phone)) {
       msgprint("All fields are necessary. Please try again.");
       return;
    }

    // email is valid
    if(!valid_email(args.email)) {
        msgprint('Please enter a valid email id');
        return;
    }

    // compose the message
    var message = "Company: " + args.company_name + "\n"
        + "Name: " + args.sender_name + "\n"
        + "Email: " + args.email + "\n"
        + "Phone: " + args.phone + "\n"
        + "Product: " + args.product

    erpnext.send_message({
      subject:'New Website Query',
      sender: $('[name="email"]').val(),
      status: 'Open',
      message: message,
      callback: function(r) {
            // print return message
        msgprint(r.message);

            // clear all inputs
        $(':input').val('');
      }
    });
  });

});

var msgprint = function(txt) {
    $("#form-alert").html(txt).toggle(true);
}
