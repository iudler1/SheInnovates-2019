function createBullets(n) {
    var bullets = "";
    for (var i = 0; i < n; i++) {
      bullets += "•";
    }
    return bullets;
  }
  
  
  $(document).ready(function() {
    var timer = "";
    $(".pass").attr("type", "text").removeAttr("name");
    $("body").on("keyup", ".pass", function(e) {
      clearTimeout(timer);
      timer = setTimeout(function() {
        $(".pass").val(createBullets($(".pass").val().length));
      }, 200);
    });
  });
  