$(document).ready(function() {

  // button for sign-up event

  $('.btn-request').click(function() {

    // hide any message
    $("#form-alert").toggle(false);

    var args = {
        sender_name: $('[name="sender_name"]').val(),
        subdomain: $('[name="subdomain"]').val(),
        company_name: $('[name="company_name"]').val(),
        company_afm: $('[name="company_afm"]').val(),
        email: $('[name="email"]').val(),
        phone: $('[name="phone"]').val(),
        product: $('[name="product"]').val(),
      }

    // all mandatory
    if(!(args.sender_name && args.company_name && args.company_afm && args.subdomain && args.email
        && args.phone)) {
       frappe.msgprint("Όλα τα πεδία είναι απαραίτητα. Παρακαλώ προσπάθησε ξανά.");
       return;
    }

		// email is valid
		if(!valid_email(args.email)) {
			frappe.msgprint('Παρακαλώ εισάγετε μία έγκυρη διεύθυνση email.');
			return false;
		}

    		// subdomain in one word
		if(args.subdomain.search(/^[a-z0-9][-a-z0-9]*[a-z0-9]$/)===-1) {
			frappe.msgprint("Το subdomain πρέπει να περιέχει μόνο λατινικούς χαρακτήρες και αριθμούς. Παρακαλώ προσπάθησε ξανά.");
			return false;
		}

		var MAX_LENGTH = 20;
		if(args.subdomain.length > MAX_LENGTH) {
			frappe.msgprint("Sub-domain can not have more than " + MAX_LENGTH + " characters.");
			return false;
		}

    // compose the message
    var message = "Company: " + args.company_name + "\n"
        + "AFM: " + args.company_afm + "\n"
        + "Name: " + args.sender_name + "\n"
        + "Subdomain: " + args.subdomain + "\n"
        + "Email: " + args.email + "\n"
        + "Phone: " + args.phone + "\n"
        + "Product: " + args.product

    erpnext.send_message({
      subject:"Νέα εγγραφή" + args.product,
      sender: $('[name="email"]').val(),
      status: 'Open',
      message: message,
      callback: function(r) {
            // print return message
        msgprint(r.message);

if(r.message==="okay") {
			frappe.msgprint("Η εγγραφή σας πραγματοποιήθηκε. Θα ενημερωθείτε μέσω email για τα στοιχεία της σύνδεσή σας.");
			
		}


            // clear all inputs
        $(':input').val('');
      }
    });
  });

});

var msgprint = function(txt) {
    $("#form-alert").html(txt).toggle(true);
}