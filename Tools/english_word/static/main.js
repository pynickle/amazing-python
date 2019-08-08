$("#button").click(function () {
    $("#navbar-item").animate(0, function () {
        if ($("#navbar-item").is(":visible")) {
            $("#button").attr("class", "navbar-burger burger")
            $("#navbar-item").attr("class", "navbar-menu")
        } else {
            $("#button").attr("class", "navbar-burger burger is-active")
            $("#navbar-item").attr("class", "navbar-menu is-active")
        }
    })
})