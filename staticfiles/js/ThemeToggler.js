$("a.theme-toggler").click( () => { 
    
    if ($('link.themes').attr('href') == "/static/css/light.css")
    {
        $("a.theme-toggler").html("🌑 Dark Theme");
        $('link.themes').attr('href', dark_css);
    }
    else if ($('link.themes').attr('href') == "/static/css/dark.css")
    {
        $("a.theme-toggler").html("☀️ Light Theme");
        $('link.themes').attr('href', light_css);
    };
});
