/*
for data mockup
---------------
https://mockaroo.com/

Host a json file in goolge
--------------------------
http://myjson.com/

Generate a random User
------------------------
https://randomuser.me/
*/

// JavaScript AJAX
$('#js-btn').click(function(){

    // Create a AJAX request
    let http = new XMLHttpRequest();

    // Prepare
    http.open('GET','https://api.myjson.com/bins/kj1gg',true);

    // Send the request
    http.send();

    // Track the Request
    http.onreadystatechange = () => {
        // response is ready and it is OK status
        if(http.readyState === 4 && http.status === 200){
            let theData = http.responseText;
            let persons = JSON.parse(theData);
            displayTableData(persons);
        }
    };

});

// JQuery AJAX
$('#jquery-btn').click(function() {
    $.ajax({
        method : 'GET',
        url : 'https://api.myjson.com/bins/uq03s',
        success : function(data) {
            displayTableData(data);
            console.log(data)
        }
    });
});


// display Table Data
let displayTableData = (persons) => {
    let tableRow = '';
    for(let person of persons){
        tableRow += `<tr>
                        <td>${person.id}</td>
                        <td>${person.first_name}</td>
                        <td>${person.last_name}</td>
                        <td>${person.gender}</td>
                        <td>${person.email}</td>
                        <td>${person.ip_address}</td>
                     </tr>`;
        $('#table_body').empty().append(tableRow);
    }

};