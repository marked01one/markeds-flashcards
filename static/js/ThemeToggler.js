let current_state = "light";

$("a.theme-toggler").click(function (e) { 
    if (current_state == "light"){
        $("a.theme-toggler").html("🌑 Dark Theme");
        $('link.themes').attr('href', dark_css);
        current_state = "dark";
    }
    else if (current_state == "dark"){
        $("a.theme-toggler").html("☀️ Light Theme");
        $('link.themes').attr('href', light_css);
        current_state = "light";
    };
});
