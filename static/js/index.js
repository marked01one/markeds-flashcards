let current_state = "light";

$("h1.page-header").click(function (e) { 
    if (current_state == "light"){
        $('link.themes').attr('href', "static/css/dark.css");
        current_state = "dark";
    }
    else if (current_state == "dark"){
        $('link.themes').attr('href', "static/css/light.css");
        current_state = "light";
    };
});
