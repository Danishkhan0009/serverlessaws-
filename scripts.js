var API_ENDPOINT = "https://8q97rsrsph.execute-api.ap-south-1.amazonaws.com/hiii"; // Change this

function getInputData() {
    return {
        "studentid": $('#studentid').val(),
        "name": $('#name').val(),
        "class": $('#class').val(),
        "age": $('#age').val()
    };
}

$("#savestudent").click(function() {
    $.ajax({
        url: API_ENDPOINT,
        type: 'POST',
        data: JSON.stringify(getInputData()),
        contentType: 'application/json',
        success: function(response) {
            $("#studentSaved").html("Student data saved!");
        },
        error: function() {
            alert("Failed to save student.");
        }
    });
});

$("#updatestudent").click(function() {
    $.ajax({
        url: API_ENDPOINT,
        type: 'PUT',
        data: JSON.stringify(getInputData()),
        contentType: 'application/json',
        success: function(response) {
            $("#studentSaved").html("Student data updated!");
        },
        error: function() {
            alert("Failed to update student.");
        }
    });
});

$("#deletestudent").click(function() {
    $.ajax({
        url: API_ENDPOINT,
        type: 'DELETE',
        data: JSON.stringify({ "studentid": $('#studentid').val() }),
        contentType: 'application/json',
        success: function(response) {
            $("#studentSaved").html("Student data deleted!");
        },
        error: function() {
            alert("Failed to delete student.");
        }
    });
});

$("#getstudents").click(function() {
    $.ajax({
        url: API_ENDPOINT,
        type: 'GET',
        contentType: 'application/json',
        success: function(response) {
            $("#studentTable tbody").empty();
            $.each(response, function(i, data) {
                $("#studentTable tbody").append("<tr>\
                    <td>" + data.studentid + "</td>\
                    <td>" + data.name + "</td>\
                    <td>" + data.class + "</td>\
                    <td>" + data.age + "</td>\
                </tr>");
            });
        },
        error: function() {
            alert("Failed to load student data.");
        }
    });
});
