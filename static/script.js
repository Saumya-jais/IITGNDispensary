// Add your JavaScript code here

// Clear form fields function
function clearForm() {
    document.getElementById('loginForm').reset();
  }
  
  // Show registration modal function
  $(document).ready(function() {
    $('#createAccountLink').click(function() {
      $('#registrationModal').modal('show');
    });
  });
  
  // Handle new user registration form submission
  $(document).ready(function() {
    $('#registrationForm').submit(function(event) {
      event.preventDefault(); // Prevent default form submission
  
      // Collect form data
      var firstName = $('#firstName').val();
      var lastName = $('#lastName').val();
      var newEmail = $('#newEmail').val();
      var newPassword = $('#newPassword').val();
      var authority = $('#authority').val();
  
      // Perform validation
      if (firstName.trim() === '' || lastName.trim() === '' || newEmail.trim() === '' || newPassword.trim() === '' || authority.trim() === '') {
        alert('Please fill in all fields.');
        return;
      }
  
      // Display form data
      console.log('First Name: ' + firstName);
      console.log('Last Name: ' + lastName);
      console.log('Email: ' + newEmail);
      console.log('Password: ' + newPassword);
      console.log('Authority: ' + authority);
  
      // You can add AJAX call here to send registration data to the server
      // For demonstration, we are just displaying form data in the console
  
      // Clear form fields after submission
      $('#registrationForm').trigger('reset');
      // Close the modal
      $('#registrationModal').modal('hide');
    });
  });
  
