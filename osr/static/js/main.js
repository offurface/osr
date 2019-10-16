$(document).ready(function() {
  window.answers = [];
  $('.questions').tabslet({
    animation: true,
  });
  $('.answer').click(function(e){
    e.preventDefault()

    window.answers.push(
      $(this).data()
    );

    $('.questions').trigger('next');
  });

  $('.questions').on("_before", function(e) {
    var parent = $(e.currentTarget.children[0]);
    var length = parent.children().length;
    var activeEl = $($(parent).find('.active')[0]);
    var activeIndex = activeEl.index() + 1;
    var status = activeIndex * 100 / length;
    var numberQ = (activeIndex + 1) <= length ? activeIndex + 1 : 1;

    $("#progressBar").css("width", status + "%");
    if (activeIndex == length) {
      $("#questionsWrapper").fadeOut(0);
      $("#beginTestWrapper").fadeIn(0);
      $("#preloader").fadeIn(0);

      $.ajax({
        type: "POST",
        url: parent.data("url"),
        data: JSON.stringify({
          answers: window.answers
        }),
        beforeSend: function (xhr) {
          xhr.setRequestHeader('X-CSRFToken', Cookies.get('csrftoken'));
        },
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function (msg) {
          console.log(msg)
          window.location.href = msg.link
        }
      });
      return;
    }

    $("#numberQuestion").html(numberQ);

  });

  $(".date-mask").mask("99.99.9999", {autoclear: true});
  $(".testologist-mask").mask("99-999", { autoclear: true });
  $(".phone-mask").mask("+7 (999) 999-99-99", {autoclear: true});
  $(".testologist-mask-not-clean").mask("99-999", { autoclear: false });

  $(".beginTestingSubmit").on("submit", function (e) {
    e.preventDefault();

    $("#preloader").fadeIn(0);

    $.ajax({
      type: this.method,
      url: this.action,
      data: $(this).serialize(),
      beforeSend: function (xhr) {
        xhr.setRequestHeader('X-CSRFToken', Cookies.get('csrftoken'));
      },
      success: function (msg) {
        closeBeginTestWrapper();
        $("#preloader").fadeOut(500);
      }
    });

    closeBeginTestWrapper()
  });

  $(".beginTestingClick").on("click", function (e) {
    e.preventDefault();

    var form = $(this).parents("form")[0];

    $("#preloader").fadeIn(0);

    $.ajax({
      type: 'POST',
      url: form.action,
      data: "code=reset",
      beforeSend: function (xhr) {
        xhr.setRequestHeader('X-CSRFToken', Cookies.get('csrftoken'));
      },
      success: function (msg) {
        closeBeginTestWrapper();
        $("#preloader").fadeOut(500);
      }
    });
    closeBeginTestWrapper()
  });

  function closeBeginTestWrapper() {
    $("#beginTestWrapper").fadeOut(0, function () {
      $("#questionsWrapper").fadeIn(0);
    });
  }

  $('.searchType-form').on('submit', function(e) {
    e.preventDefault();
    var form = this,
        $form = $(form);
    $.ajax({
      type: form.method,
      url: form.action,
      data: $(form).serialize(),
      beforeSend: function (xhr) {
        xhr.setRequestHeader('X-CSRFToken', Cookies.get('csrftoken'));
      },
      success: function (msg) {
        $form.siblings(".searchType-result-wrap").html(msg.html);
      }
    });
  });

  // Страница поиска
  $('#searchTypeWrapper').tabslet({
    controls: {
      prev: '.prev',
      next: '.next'
    }
  });

  $( ".s-text__principle" ).click(function(){
    $(this).find(".s-text__principle-content").slideToggle();
  });

  $('.valid-user').on('click', function() {
    var id = $(this).data('id'),
        url = $(this).data('url'),
        checked = this.checked,
        $this = $(this);

    $this.next().css('opacity', '1');

    $.ajax({
      type: 'POST',
      url: url,
      data: "user_id=" + id,
      beforeSend: function (xhr) {
        xhr.setRequestHeader('X-CSRFToken', Cookies.get('csrftoken'));
      },
      success: function (msg) {
        $this.next().css('opacity', '0');
        var count = $('#count-user').data('value');
        if (checked){
          count++;
        }
        else{
          count--;
        }
        $this.parents('label').toggleClass('removed');
        $('#count-user').data('value', count);
        $('#count-user').html('ДОПУЩЕНО: ' + count);
      }
    });
  })
});
