
$(document).ready(function() {

        if ($("#percent_change").data < 0) {
            console.log($("#percent_change").data);
            $("percent_change").className = "text-warning";
        }
});

/*var divId = "percent_change"
jQuery(document).ready(checkContainer);

function changecolor(id) {

    var c = document.querySelectorAll("div i");
    for (i in c) {
        if (document.getElementById("percent_change") < 0) {
            c[i].className = "text-warning";
            c.className = "fa fa-level-down";
        }

    }
}
//"when this id is ready, read the data, do logic, change cla" s"

/* if (document.getElementById("percent_change").onload) {

    var data = $('ticker').data
    if data>0 {
        $('ticker').addClass
    }
}

console.log('this is a test')
console.log(data)

function changeActive(id) {
    var c = document.querySelectorAll("ul a");
    for (i in c)
    {
        c[i].className = 'a black';
    }
    //update it at last
    document.getElementById(id).className = "active a red";
} */