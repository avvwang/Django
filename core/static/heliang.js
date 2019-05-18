$(document).ready(function () {
    $('#example').DataTable({
        "serverSide": true,
        "ajax": {
            "type": "POST",
            "contentType":'application/json; charset=UTF-8',
            "url": "http://127.0.0.1:8000/core/movies",
            "dataSrc": function (json) {
                for (var i = 0, ien = json.data.length; i < ien; i++) {
                    console.log(json.data)
                    json.data[i][1] = '<input value=' + json.data[i][1] + ">";
                }
                return json.data;
            },
            data: function(d) {
                 // return JSON.stringify(d);
                 var str = {
                         "draw": d.draw,
                         "start": d.start,
                         "length": d.length,
                         "search": d.search.value
                 };
                 return JSON.stringify(str);
               },
        }
    })
})
;

function main() {
    $.ajax({
        url: "movies",
        typr: "post",
        data: {"code": 200},
        success: function (data) {

        },
        error: function () {

        }

    })

}