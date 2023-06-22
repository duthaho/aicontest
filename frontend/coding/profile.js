var Profile = (function () {
  $(".delete-bot")
    .off("click")
    .on("click", function (e) {
      e.preventDefault();
      JBase.send(window.location.href, {
        type: "DELETE",
        data: {
          bot_id: e.target.dataset.botId,
        },
        success: function (response) {
          location.reload();
        },
      });
    });

  $(".btn-paging li")
    .off("click")
    .on("click", function (e) {
      e.preventDefault();
      if (e.currentTarget.classList.contains("disabled")) {
        return;
      }
      window.location.href = JBase.set_url_param(
        window.location.href,
        "page",
        e.target.dataset.page
      );
    });
})();
