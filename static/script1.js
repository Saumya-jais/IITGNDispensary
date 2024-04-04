
document.getElementById("showDoctor").addEventListener("click", function() {
    window.location.href = "/doctor1.html";
});
    // fetch('/get_doctors')
    // .then(response => response.json())
    // .then(data => {
    //     let table = '<table><tr><th>Doctor_ID</th><th>First_Name</th><th>Middle_Name</th><th>Last_Name</th><th>DOB</th><th>Gender</th><th>Email</th><th>Specialization</th><th>Experience</th><th>Street_Number</th><th>Street_Name</th><th>Apartment_Number</th><th>City</th><th>Pincode</th><th>Action</th></tr>';
    //     data.forEach(doctor => {
    //         table += `<tr><td>${doctor.Doctor_ID}</td><td>${doctor.First_Name}</td><td>${doctor.Middle_Name}</td><td>${doctor.Last_Name}</td><td>${doctor.DOB}</td><td>${doctor.Gender}</td><td>${doctor.Email}</td><td>${doctor.Specialization}</td><td>${doctor.Experience}</td><td>${doctor.Street_Number}</td><td>${doctor.Street_Name}</td><td>${doctor.Apartment_Number}</td><td>${doctor.City}</td><td>${doctor.Pincode}</td><td><button onclick="editDoctor(${doctor.Doctor_ID})">Edit</button><button onclick="deleteDoctor(${doctor.Doctor_ID})">Delete</button></td></tr>`;
    //     });
    //     table += '</table>';
    //     document.getElementById('doctorTable').innerHTML = table;
    // });


// function editDoctor(id) {
//     // Implement edit functionality
// }

// function deleteDoctor(id) {
//     // Implement delete functionality
// }
